import json
import logging
import socket
import time
from threading import Event, Thread

from src.config.ConfigManager import ConfigManager

_logger = logging.getLogger(__name__)


class VrcftAutoConnect:
    __BROADCASTED_PORT: int = 57130

    def __init__(self, config_manager: ConfigManager):
        self.__config_manager = config_manager

        self.__is_started: Event = Event()
        self.__thread: Thread | None = None
        self.__socket: socket.socket | None = None

    def start(self):
        if self.__is_started.is_set():
            return

        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

            try:
                self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            except Exception:
                _logger.info("Failed to set SO_REUSEADDR")

            try:
                self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except Exception:
                _logger.info("Failed to set SO_REUSEPORT")

            self.__socket.settimeout(1.0)

            self.__socket.bind(("", self.__BROADCASTED_PORT))

            self.__thread = Thread(target=self.__start_loop, daemon=True, name="VRCFT Auto Connect")

            self.__is_started.set()
            self.__thread.start()
        except Exception:
            _logger.warning("Failed to start VRCFT Auto Connect", exc_info=True, stack_info=True)

            self.stop()

    def stop(self):
        self.__is_started.clear()

        try:
            if self.__socket is not None:
                self.__socket.close()

            if self.__thread is not None:
                self.__thread.join()
        except Exception:
            _logger.warning("Failed to stop VRCFT Auto Connect", exc_info=True, stack_info=True)

    def __start_loop(self):
        _logger.info("Starting VRCFT Auto Connect")

        while self.__is_started.is_set():
            try:
                data, addr = self.__socket.recvfrom(1024)
                json_data = json.loads(data.decode('utf8'))

                self.__config_manager.config.socket.ip = str(addr[0])
                self.__config_manager.config.socket.port = int(json_data.get("Port"))
                self.__config_manager.write()

                _logger.info(f"Auto connected to {self.__config_manager.config.socket.ip}. Data: {json_data}")
            except socket.timeout: # Linux cant release recvfrom without timeout
                continue
            except Exception:
                if self.__is_started.is_set():
                    _logger.warning("Failed to receive auto connect data", exc_info=True, stack_info=True)

                    time.sleep(0.01)

        _logger.info("Stopped VRCFT Auto Connect")
