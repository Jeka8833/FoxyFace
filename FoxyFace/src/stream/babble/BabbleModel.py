import logging
from dataclasses import dataclass

import numpy
from cv2.typing import MatLike
from onnxruntime import InferenceSession

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum

_logger = logging.getLogger(__name__)


@dataclass(slots=True, frozen=True)
class BabbleModel:
    __session: InferenceSession
    __input_name: str
    __output_names: list[str]
    is_default_model: bool
    input_size_x: int
    input_size_y: int

    def process_gray_image(self, image: MatLike) -> dict[BabbleBlendShapeEnum, float]:
        frame = (image[numpy.newaxis, numpy.newaxis, :, :] / 255.0).astype(numpy.float32)  # (1, 1, size, size)

        out = self.__session.run(self.__output_names, {self.__input_name: frame})

        arr = out[0][0].astype(float)

        return {blend_shape: arr[blend_shape.value] for blend_shape in BabbleBlendShapeEnum}

    def is_loaded_successfully(self) -> bool:
        try:
            test_image = numpy.zeros((self.input_size_y, self.input_size_x), dtype=numpy.uint8)

            self.process_gray_image(test_image)

            return True
        except Exception:
            _logger.warning("Failed to load babble model", exc_info=True, stack_info=True)

        return False
