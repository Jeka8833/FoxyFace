import unittest

from src.stream.babble.BabbleBlendShapeEnum import BabbleBlendShapeEnum
from src.stream.core.components.BufferStream import BufferStream
from src.stream.mediapipe.MediaPipeBlendShapeEnum import MediaPipeBlendShapeEnum
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.postprocessing.mixer.MixSelectEnum import MixSelectEnum
from src.stream.postprocessing.mixer.MixerProcessing import MixerProcessing
from src.stream.postprocessing.mixer.MixerProcessingOptions import MixerProcessingOptions


class MixerProcessingTest(unittest.TestCase):
    def test_midia_pipe(self):
        blend_shape_frame = BlendShapesFrame(
            {MediaPipeBlendShapeEnum.MouthUpperUpLeft: 0.5, BabbleBlendShapeEnum.MouthUpperUpLeft: 0.1}, 0)
        options = MixerProcessingOptions({GeneralBlendShapeEnum.MouthUpperUpLeft: MixSelectEnum.MediaPipe})

        single_buffer = BufferStream[BlendShapesFrame[MediaPipeBlendShapeEnum]]()
        single_buffer.put(blend_shape_frame)
        result = MixerProcessing(single_buffer, options).poll(1)

        self.assertTrue(len(result.blend_shapes) == 1)
        self.assertTrue(result.blend_shapes.get(GeneralBlendShapeEnum.MouthUpperUpLeft) == 0.5)
        self.assertTrue(result.timestamp_ns == 0)

    def test_babble(self):
        blend_shape_frame = BlendShapesFrame(
            {MediaPipeBlendShapeEnum.MouthUpperUpLeft: 0.5, BabbleBlendShapeEnum.MouthUpperUpLeft: 0.1}, 0)
        options = MixerProcessingOptions({GeneralBlendShapeEnum.MouthUpperUpLeft: MixSelectEnum.Babble})

        single_buffer = BufferStream[BlendShapesFrame[MediaPipeBlendShapeEnum]]()
        single_buffer.put(blend_shape_frame)
        result = MixerProcessing(single_buffer, options).poll(1)

        self.assertTrue(len(result.blend_shapes) == 1)
        self.assertTrue(result.blend_shapes.get(GeneralBlendShapeEnum.MouthUpperUpLeft) == 0.1)
        self.assertTrue(result.timestamp_ns == 0)

    def test_disabled(self):
        blend_shape_frame = BlendShapesFrame(
            {MediaPipeBlendShapeEnum.MouthUpperUpLeft: 0.5, BabbleBlendShapeEnum.MouthUpperUpLeft: 0.1}, 0)
        options = MixerProcessingOptions({GeneralBlendShapeEnum.MouthUpperUpLeft: MixSelectEnum.Disabled})

        single_buffer = BufferStream[BlendShapesFrame[MediaPipeBlendShapeEnum]]()
        single_buffer.put(blend_shape_frame)

        result = MixerProcessing(single_buffer, options).poll(1)

        self.assertTrue(len(result.blend_shapes) == 0)
        self.assertTrue(result.timestamp_ns == 0)

    def test_auto(self):
        blend_shape_frame = BlendShapesFrame(
            {MediaPipeBlendShapeEnum.MouthUpperUpLeft: 0.5, BabbleBlendShapeEnum.MouthUpperUpLeft: 0.1}, 0)
        options = MixerProcessingOptions({})

        single_buffer = BufferStream[BlendShapesFrame[MediaPipeBlendShapeEnum]]()
        single_buffer.put(blend_shape_frame)
        result = MixerProcessing(single_buffer, options).poll(1)

        self.assertTrue(len(result.blend_shapes) == 1)
        self.assertTrue(result.blend_shapes.get(GeneralBlendShapeEnum.MouthUpperUpLeft) == 0.5)
        self.assertTrue(result.timestamp_ns == 0)

    def test_auto_disable(self):
        blend_shape_frame = BlendShapesFrame(
            {MediaPipeBlendShapeEnum.CheekPuff: 0.5, BabbleBlendShapeEnum.CheekPuffRight: 0.1,
             BabbleBlendShapeEnum.CheekPuffLeft: 0.1}, 0)
        options = MixerProcessingOptions({})

        single_buffer = BufferStream[BlendShapesFrame[MediaPipeBlendShapeEnum]]()
        single_buffer.put(blend_shape_frame)
        result = MixerProcessing(single_buffer, options).poll(1)

        self.assertFalse(result.blend_shapes.get(GeneralBlendShapeEnum.CheekPuff) is not None and (
                result.blend_shapes.get(GeneralBlendShapeEnum.CheekPuffLeft) is not None or result.blend_shapes.get(
            GeneralBlendShapeEnum.CheekPuffRight) is not None))
        self.assertTrue(result.timestamp_ns == 0)


if __name__ == '__main__':
    unittest.main()
