import logging
import socket
import time
from threading import Event, Lock, Thread

from src.stream.vrcft.VrcftPacketEncoderStream import VrcftPacketEncoderStream

_logger = logging.getLogger(__name__)


class VRCFTUdpSocket:
    def __init__(self, packet_stream: VrcftPacketEncoderStream, target_address: tuple[str, int] = ("localhost", 54321),
                 ping_connection_time: float = 1.0):
        self.__packet_stream: VrcftPacketEncoderStream = packet_stream
        self.target_address: tuple[str, int] = target_address
        self.ping_connection_time: float = ping_connection_time

        self.__sock: socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__lock: Lock = Lock()

        self.__last_statistic_time_ns: int = time.perf_counter_ns()

        self.__packet_count: int = 0

        self.__last_pps: int = 0
        self.__has_error: bool = False

        self.__close_event: Event = Event()
        self.__thread: Thread = Thread(target=self.__loop, daemon=True, name="VRCFT UDP Socket")
        self.__thread.start()

    def has_error(self) -> bool:
        return self.__has_error

    def get_pps(self) -> float:
        self.__update_statistic()

        return self.__last_pps

    def close(self):
        self.__close_event.set()

        self.__thread.join()

        self.__sock.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __loop(self):
        while not self.__close_event.is_set():
            try:
                try:
                    data = self.__packet_stream.poll(self.ping_connection_time)
                except TimeoutError:
                    data = self.__packet_stream.generate_ping_packet()

                _logger.debug(f"Sending {data}")
                self.__sock.sendto(data, self.target_address)

                with self.__lock:
                    self.__packet_count += 1

                self.__has_error = False
            except InterruptedError:
                return
            except Exception:
                self.__has_error = True

                _logger.warning("Exception in UDP VRCFT loop", exc_info=True, stack_info=True)

                self.__close_event.wait(0.001)

    def __update_statistic(self):
        with self.__lock:
            current_time = time.perf_counter_ns()

            if current_time - self.__last_statistic_time_ns >= 1_000_000_000:
                self.__last_pps = (self.__packet_count * 1_000_000_000) / (current_time - self.__last_statistic_time_ns)

                self.__last_statistic_time_ns = current_time

                self.__packet_count = 0
