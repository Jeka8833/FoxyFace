import logging.handlers
import multiprocessing
import queue
import time

import numpy

from src.stream.mediapipe.tongue.MediaPipeTongueModel import MediaPipeTongueModel

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256
IMAGE_CHANNELS = 3
IMAGE_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)
IMAGE_SIZE = IMAGE_HEIGHT * IMAGE_WIDTH * IMAGE_CHANNELS


def _onnx_worker_loop(log_queue, cmd_queue, output_queue, frame_timestamp, frame_image,
                      frame_condition):
    process_logger = logging.getLogger("MediaPipe Tongue Process")
    process_logger.setLevel(logging.INFO)
    process_logger.handlers = [logging.handlers.QueueHandler(log_queue)]

    process_logger.info("Starting MediaPipe Tongue Process")

    timestamp = 0
    model = None
    image = None

    while True:
        parent = multiprocessing.parent_process()
        if parent is not None and not parent.is_alive():
            break

        try:
            while True:
                cmd = cmd_queue.get_nowait()
                if cmd[0] == "load_model":
                    try:
                        model = None
                        model = MediaPipeTongueModel.load_model(cmd[1], cmd[2], cmd[3], cmd[4])
                        process_logger.info(
                            f"MediaPipe Tongue model has loaded with provider: {cmd[1]}, device id: {cmd[4]}, "
                            f"intra_op_num_threads: {cmd[2]}, allow_spinning: {cmd[3]}")
                    except Exception:
                        process_logger.error("Failed to load model", exc_info=True, stack_info=True)
                elif cmd[0] == "stop":
                    return
        except queue.Empty:
            pass
        except (ValueError, OSError):
            process_logger.error("Failed to load model", exc_info=True, stack_info=True)

        if model is None:
            output_queue.put((None, None))
            time.sleep(0.5)

            continue

        if not frame_condition.acquire(timeout=0.5):
            continue
        try:
            if timestamp == frame_timestamp.value:
                frame_condition.wait(timeout=0.5)

                continue

            image = numpy.frombuffer(frame_image, dtype=numpy.uint8).reshape(IMAGE_SHAPE).copy()
            timestamp = frame_timestamp.value
        finally:
            frame_condition.release()

        try:
            tongue_out = model.run(image)
            output_queue.put((timestamp, tongue_out))
        except Exception:
            try:
                process_logger.error("Run model", exc_info=True, stack_info=True)

                output_queue.put((None, None))
                time.sleep(0.05)
            except Exception:
                break
