import json
import time

from src.stream.core.StreamReadOnly import StreamReadOnly
from src.stream.postprocessing.BlendShapesFrame import BlendShapesFrame
from src.stream.postprocessing.GeneralBlendShapeEnum import GeneralBlendShapeEnum
from src.stream.vrcft.UnifiedExpressionEnum import UnifiedExpressionEnum
from src.stream.vrcft.VrcftInterfaceOptions import VrcftInterfaceOptions


class VrcftPacketEncoderStream(StreamReadOnly[bytes]):
    def __init__(self, stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]], options: VrcftInterfaceOptions):
        self.__stream: StreamReadOnly[BlendShapesFrame[GeneralBlendShapeEnum]] = stream
        self.__options: VrcftInterfaceOptions = options
        self.__last_timestamp: int = time.perf_counter_ns() // 1_000_000

    def poll(self, timeout: float | None = None) -> bytes:
        start_time = time.perf_counter_ns()
        while True:
            if timeout > 0.0:
                need_wait = timeout - (time.perf_counter_ns() - start_time) / 1_000_000_000
                if need_wait <= 0.0:
                    raise TimeoutError()
            else:
                need_wait = timeout

            timed_blend_shapes = self.__stream.poll(need_wait)

            if timed_blend_shapes.blend_shapes:
                break

        packet_timestamp = time.perf_counter_ns() // 1_000_000
        if packet_timestamp <= self.__last_timestamp:
            packet_timestamp = self.__last_timestamp + 1

        self.__last_timestamp = packet_timestamp

        return self.__encode_object_to_json(
                {"Timestamp": packet_timestamp, "Config": self.__options.to_packet_format_dict(),
                 "Values": self.__mediapipe_to_vrcft_name(timed_blend_shapes.blend_shapes)})

    def generate_ping_packet(self) -> bytes:
        return self.__encode_object_to_json({"PingPacket": True, "Config": self.__options.to_packet_format_dict()})

    @staticmethod
    def __encode_object_to_json(any_object) -> bytes:
        return json.dumps(any_object, allow_nan=False, separators=(",", ":")).encode("utf-8")

    @staticmethod
    def __mediapipe_to_vrcft_name(media_pipe_dict: dict[GeneralBlendShapeEnum, float]) -> dict[
        UnifiedExpressionEnum, float]:
        eye_close_left = media_pipe_dict.get(GeneralBlendShapeEnum.EyeBlinkLeft)
        eye_open_left = 1 - eye_close_left if eye_close_left is not None else None

        eye_close_right = media_pipe_dict.get(GeneralBlendShapeEnum.EyeBlinkRight)
        eye_open_right = 1 - eye_close_right if eye_close_right is not None else None

        # @formatter:off
        new_dict = {UnifiedExpressionEnum.BrowLowererLeft: media_pipe_dict.get(GeneralBlendShapeEnum.BrowDownLeft),
                    UnifiedExpressionEnum.BrowPinchLeft: media_pipe_dict.get(GeneralBlendShapeEnum.BrowDownLeft),

                    UnifiedExpressionEnum.BrowLowererRight: media_pipe_dict.get(GeneralBlendShapeEnum.BrowDownRight),
                    UnifiedExpressionEnum.BrowPinchRight: media_pipe_dict.get(GeneralBlendShapeEnum.BrowDownRight),

                    UnifiedExpressionEnum.BrowInnerUpRight: media_pipe_dict.get(GeneralBlendShapeEnum.BrowInnerUp),
                    UnifiedExpressionEnum.BrowInnerUpLeft: media_pipe_dict.get(GeneralBlendShapeEnum.BrowInnerUp),

                    UnifiedExpressionEnum.BrowOuterUpLeft: media_pipe_dict.get(GeneralBlendShapeEnum.BrowOuterUpLeft),

                    UnifiedExpressionEnum.BrowOuterUpRight: media_pipe_dict.get(GeneralBlendShapeEnum.BrowOuterUpRight),

                    UnifiedExpressionEnum.CheekPuffLeft: media_pipe_dict.get(GeneralBlendShapeEnum.CheekPuffLeft, media_pipe_dict.get(GeneralBlendShapeEnum.CheekPuff)),
                    UnifiedExpressionEnum.CheekPuffRight: media_pipe_dict.get(GeneralBlendShapeEnum.CheekPuffRight, media_pipe_dict.get(GeneralBlendShapeEnum.CheekPuff)),

                    UnifiedExpressionEnum.CheekSquintLeft: media_pipe_dict.get(GeneralBlendShapeEnum.CheekSquintLeft),

                    UnifiedExpressionEnum.CheekSquintRight: media_pipe_dict.get(GeneralBlendShapeEnum.CheekSquintRight),

                    UnifiedExpressionEnum.EyeOpennessLeft: eye_open_left,

                    UnifiedExpressionEnum.EyeOpennessRight: eye_open_right,

                    UnifiedExpressionEnum.EyeXLeft: media_pipe_dict.get(GeneralBlendShapeEnum.EyeXLeft),
                    UnifiedExpressionEnum.EyeXRight: media_pipe_dict.get(GeneralBlendShapeEnum.EyeXRight),
                    UnifiedExpressionEnum.EyeYLeft: media_pipe_dict.get(GeneralBlendShapeEnum.EyeYLeft),
                    UnifiedExpressionEnum.EyeYRight: media_pipe_dict.get(GeneralBlendShapeEnum.EyeYRight),

                    UnifiedExpressionEnum.EyeSquintLeft: media_pipe_dict.get(GeneralBlendShapeEnum.EyeSquintLeft),

                    UnifiedExpressionEnum.EyeSquintRight: media_pipe_dict.get(GeneralBlendShapeEnum.EyeSquintRight),

                    UnifiedExpressionEnum.EyeWideLeft: media_pipe_dict.get(GeneralBlendShapeEnum.EyeWideLeft),

                    UnifiedExpressionEnum.EyeWideRight: media_pipe_dict.get(GeneralBlendShapeEnum.EyeWideRight),

                    UnifiedExpressionEnum.JawForward: media_pipe_dict.get(GeneralBlendShapeEnum.JawForward),

                    UnifiedExpressionEnum.JawLeft: media_pipe_dict.get(GeneralBlendShapeEnum.JawLeft),

                    UnifiedExpressionEnum.JawOpen: media_pipe_dict.get(GeneralBlendShapeEnum.JawOpen),

                    UnifiedExpressionEnum.JawRight: media_pipe_dict.get(GeneralBlendShapeEnum.JawRight),

                    UnifiedExpressionEnum.MouthClosed: media_pipe_dict.get(GeneralBlendShapeEnum.MouthClosed),

                    UnifiedExpressionEnum.MouthDimpleLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthDimpleLeft),

                    UnifiedExpressionEnum.MouthDimpleRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthDimpleRight),

                    UnifiedExpressionEnum.MouthFrownLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthFrownLeft),

                    UnifiedExpressionEnum.MouthFrownRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthFrownRight),

                    UnifiedExpressionEnum.LipFunnelUpperRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthFunnel),
                    UnifiedExpressionEnum.LipFunnelUpperLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthFunnel),
                    UnifiedExpressionEnum.LipFunnelLowerRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthFunnel),
                    UnifiedExpressionEnum.LipFunnelLowerLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthFunnel),

                    UnifiedExpressionEnum.MouthUpperLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthLeft),
                    UnifiedExpressionEnum.MouthLowerLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthLeft),

                    UnifiedExpressionEnum.MouthLowerDownLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthLowerDownLeft),

                    UnifiedExpressionEnum.MouthLowerDownRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthLowerDownRight),

                    UnifiedExpressionEnum.MouthPressLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthPressLeft),

                    UnifiedExpressionEnum.MouthPressRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthPressRight),

                    UnifiedExpressionEnum.LipPuckerUpperRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthPucker),
                    UnifiedExpressionEnum.LipPuckerUpperLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthPucker),
                    UnifiedExpressionEnum.LipPuckerLowerRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthPucker),
                    UnifiedExpressionEnum.LipPuckerLowerLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthPucker),

                    UnifiedExpressionEnum.MouthUpperRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRight),
                    UnifiedExpressionEnum.MouthLowerRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRight),

                    UnifiedExpressionEnum.LipSuckLowerRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRollLower),
                    UnifiedExpressionEnum.LipSuckLowerLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRollLower),

                    UnifiedExpressionEnum.LipSuckUpperRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRollUpper),
                    UnifiedExpressionEnum.LipSuckUpperLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRollUpper),

                    UnifiedExpressionEnum.MouthRaiserLower: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRaiserLower),

                    UnifiedExpressionEnum.MouthRaiserUpper: media_pipe_dict.get(GeneralBlendShapeEnum.MouthRaiserUpper),

                    UnifiedExpressionEnum.MouthCornerPullLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthSmileLeft),
                    UnifiedExpressionEnum.MouthCornerSlantLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthSmileLeft),

                    UnifiedExpressionEnum.MouthCornerPullRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthSmileRight),
                    UnifiedExpressionEnum.MouthCornerSlantRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthSmileRight),

                    UnifiedExpressionEnum.MouthStretchLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthStretchLeft),

                    UnifiedExpressionEnum.MouthStretchRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthStretchRight),

                    UnifiedExpressionEnum.MouthUpperUpLeft: media_pipe_dict.get(GeneralBlendShapeEnum.MouthUpperUpLeft),

                    UnifiedExpressionEnum.MouthUpperUpRight: media_pipe_dict.get(GeneralBlendShapeEnum.MouthUpperUpRight),

                    UnifiedExpressionEnum.NoseSneerLeft: media_pipe_dict.get(GeneralBlendShapeEnum.NoseSneerLeft),

                    UnifiedExpressionEnum.NoseSneerRight: media_pipe_dict.get(GeneralBlendShapeEnum.NoseSneerRight),

                    UnifiedExpressionEnum.HeadX: media_pipe_dict.get(GeneralBlendShapeEnum.HeadX),
                    UnifiedExpressionEnum.HeadY: media_pipe_dict.get(GeneralBlendShapeEnum.HeadY),
                    UnifiedExpressionEnum.HeadZ: media_pipe_dict.get(GeneralBlendShapeEnum.HeadZ),

                    UnifiedExpressionEnum.HeadPitch: media_pipe_dict.get(GeneralBlendShapeEnum.HeadPitch),
                    UnifiedExpressionEnum.HeadYaw: media_pipe_dict.get(GeneralBlendShapeEnum.HeadYaw),
                    UnifiedExpressionEnum.HeadRoll: media_pipe_dict.get(GeneralBlendShapeEnum.HeadRoll),

                    UnifiedExpressionEnum.CheekSuckLeft: media_pipe_dict.get(GeneralBlendShapeEnum.CheekSuckLeft),
                    UnifiedExpressionEnum.CheekSuckRight: media_pipe_dict.get(GeneralBlendShapeEnum.CheekSuckRight),

                    UnifiedExpressionEnum.TongueOut: media_pipe_dict.get(GeneralBlendShapeEnum.TongueOut),
                    UnifiedExpressionEnum.TongueUp: media_pipe_dict.get(GeneralBlendShapeEnum.TongueUp),
                    UnifiedExpressionEnum.TongueDown: media_pipe_dict.get(GeneralBlendShapeEnum.TongueDown),
                    UnifiedExpressionEnum.TongueLeft: media_pipe_dict.get(GeneralBlendShapeEnum.TongueLeft),
                    UnifiedExpressionEnum.TongueRight: media_pipe_dict.get(GeneralBlendShapeEnum.TongueRight),
                    UnifiedExpressionEnum.TongueRoll: media_pipe_dict.get(GeneralBlendShapeEnum.TongueRoll),
                    UnifiedExpressionEnum.TongueBendDown: media_pipe_dict.get(GeneralBlendShapeEnum.TongueBendDown),
                    UnifiedExpressionEnum.TongueCurlUp: media_pipe_dict.get(GeneralBlendShapeEnum.TongueCurlUp),
                    UnifiedExpressionEnum.TongueSquish: media_pipe_dict.get(GeneralBlendShapeEnum.TongueSquish),
                    UnifiedExpressionEnum.TongueFlat: media_pipe_dict.get(GeneralBlendShapeEnum.TongueFlat),
                    UnifiedExpressionEnum.TongueTwistLeft: media_pipe_dict.get(GeneralBlendShapeEnum.TongueTwistLeft),
                    UnifiedExpressionEnum.TongueTwistRight: media_pipe_dict.get(GeneralBlendShapeEnum.TongueTwistRight)
                    }
        # @formatter:on

        return {key: val for key, val in new_dict.items() if val is not None}
