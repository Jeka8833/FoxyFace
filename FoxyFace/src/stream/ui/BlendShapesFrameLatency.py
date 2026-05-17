import threading
import time

from src.stream.core.StreamWriteOnly import StreamWriteOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame


class BlendShapesFrameLatency(StreamWriteOnly[BlendShapesFrame]):
    def __init__(self):
        self.__last_latency: float = 0.0
        self.__last_latency_update_ns: int = time.perf_counter_ns()

        self.__latency_sum: int = 0
        self.__latency_count: int = 0

        self.__lock = threading.Lock()

    def put(self, value: BlendShapesFrame) -> bool:
        with self.__lock:
            self.__latency_sum += time.perf_counter_ns() - value.timestamp_ns
            self.__latency_count += 1

        return True

    def get_latency(self) -> float:
        with self.__lock:
            current_time = time.perf_counter_ns()

            if current_time - self.__last_latency_update_ns >= 1_000_000_000:
                if self.__latency_count == 0:
                    self.__last_latency = 0.0
                else:
                    self.__last_latency = self.__latency_sum / (self.__latency_count * 1_000_000_000)
                self.__last_latency_update_ns = current_time
                self.__latency_sum = 0
                self.__latency_count = 0

        return self.__last_latency
