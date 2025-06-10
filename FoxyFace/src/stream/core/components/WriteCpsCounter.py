import time
from threading import Lock

from src.stream.core.StreamWriteOnly import StreamWriteOnly


class WriteCpsCounter(StreamWriteOnly):
    def __init__(self):
        self.__last_cps: float = 0.0
        self.__last_cps_update_ns: int = time.perf_counter_ns()
        self.__call_count: int = 0

        self.__lock: Lock = Lock()

    def put(self, value) -> bool:
        with self.__lock:
            self.__call_count += 1

        return True

    def get_cps(self) -> float:
        with self.__lock:
            current_time = time.perf_counter_ns()

            if current_time - self.__last_cps_update_ns >= 1_000_000_000:
                self.__last_cps = (self.__call_count * 1_000_000_000) / (current_time - self.__last_cps_update_ns)
                self.__last_cps_update_ns = current_time
                self.__call_count = 0

        return self.__last_cps
