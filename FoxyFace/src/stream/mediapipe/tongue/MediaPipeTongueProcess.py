import logging.handlers
import multiprocessing
import queue
import time

import numpy

from stream.mediapipe.tongue.MediaPipeTongueModel import MediaPipeTongueModel

IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256
IMAGE_CHANNELS = 3
IMAGE_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)
IMAGE_SIZE = IMAGE_HEIGHT * IMAGE_WIDTH * IMAGE_CHANNELS


def _drain_commands(cmd_queue, process_logger):
    model = None
    try:
        while True:
            cmd = cmd_queue.get_nowait()
            if cmd[0] == "load_model":
                try:
                    model = MediaPipeTongueModel.load_model(cmd[1], cmd[2], cmd[3], cmd[4])
                except Exception:
                    process_logger.error("Failed to load model", exc_info=True, stack_info=True)
            elif cmd[0] == "stop":
                return None, False
    except queue.Empty:
        pass
    except (ValueError, OSError):
        return None, False
    return model, True


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

        new_model, should_continue = _drain_commands(cmd_queue, process_logger)
        if not should_continue:
            return

        if new_model is not None:
            model = new_model

        if model is None:
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

                time.sleep(0.05)
            except Exception:
                break
