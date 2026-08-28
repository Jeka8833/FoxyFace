from enum import StrEnum, unique


@unique
class UnifiedExpressionEnum(StrEnum):
    # Eye Expressions
    EyeSquintRight = "EyeSquintRight"  # Squeezes the right eye socket muscles, causing the lower eyelid to constrict a little bit as well. Basis on the mostly lower constriction of the inner parts of the orbicularis oculi and the stressing of the muscle group as the eyelid is closed.
    EyeSquintLeft = "EyeSquintLeft"  # Squeezes the left eye socket muscles, causing the lower eyelid to constrict a little bit as well. Basis on the mostly lower constriction of the inner parts of the orbicularis oculi and the stressing of the muscle group as the eyelid is closed.
    EyeWideRight = "EyeWideRight"  # Right eyelid widens beyond the eyelid's relaxed position. Basis on the action of the levator palpebrae superioris.
    EyeWideLeft = "EyeWideLeft"  # Left eyelid widens beyond the eyelid's relaxed position. Basis on the action of the levator palpebrae superioris.

    # Eyebrow Expressions
    BrowPinchRight = "BrowPinchRight"  # Inner right eyebrow pulls diagnally inwards and downwards slightly. Basis on the constriction of the corrugator supercilii muscle.
    BrowPinchLeft = "BrowPinchLeft"  # Inner left eyebrow pulls diagnally inwards and downwards slightly. Basis on the constriction of the corrugator supercilii muscle.
    BrowLowererRight = "BrowLowererRight"  # Outer right eyebrow pulls downward. Basis on depressor supercilii, procerus, and partially the upper orbicularis oculi muscles action of lowering the eyebrow.
    BrowLowererLeft = "BrowLowererLeft"  # Outer Left eyebrow pulls downward. Basis on depressor supercilii, procerus, and partially the upper orbicularis oculi muscles action of lowering the eyebrow.
    BrowInnerUpRight = "BrowInnerUpRight"  # Inner right eyebrow pulls upward. Basis on the inner grouping action of the frontal belly of the occipitofrontalis.
    BrowInnerUpLeft = "BrowInnerUpLeft"  # Inner left eyebrow pulls upward. Basis on the inner grouping action of the frontal belly of the occipitofrontalis.
    BrowOuterUpRight = "BrowOuterUpRight"  # Outer right eyebrow pulls upward. Basis on the outer grouping action of the frontal belly of the occipitofrontalis.
    BrowOuterUpLeft = "BrowOuterUpLeft"  # Outer left eyebrow pulls upward. Basis on the outer grouping action of the frontal belly of the occipitofrontalis.

    # Nose Expressions
    NasalDilationRight = "NasalDilationRight"  # Right side nose's canal dilates. Basis on the alar nasalis muscle.
    NasalDilationLeft = "NasalDilationLeft"  # Left side nose's canal dilates. Basis on the alar nasalis muscle.
    NasalConstrictRight = "NasalConstrictRight"  # Right side nose's canal constricts. Basis on the transverse nasalis muscle.
    NasalConstrictLeft = "NasalConstrictLeft"  # Left side nose's canal constricts. Basis on the transverse nasalis muscle.

    # Cheek Expressions
    CheekSquintRight = "CheekSquintRight"  # Raises the right side cheek. Basis on the main action of the lower outer part of the orbicularis oculi.
    CheekSquintLeft = "CheekSquintLeft"  # Raises the left side cheek. Basis on the main action of the lower outer part of the orbicularis oculi.
    CheekPuffRight = "CheekPuffRight"  # Puffs the right side cheek. Basis on the cheeks' ability to stretch orbitally.
    CheekPuffLeft = "CheekPuffLeft"  # Puffs the left side cheek. Basis on the cheeks' ability to stretch orbitally.
    CheekSuckRight = "CheekSuckRight"  # Sucks in the right side cheek. Basis on the cheeks' ability to stretch inwards from suction.
    CheekSuckLeft = "CheekSuckLeft"  # Sucks in the left side cheek. Basis on the cheeks' ability to stretch inwards from suction.

    # Jaw Exclusive Expressions
    JawOpen = "JawOpen"  # Opens the jawbone. Basis of the general action of the jaw opening by the masseter and temporalis muscle grouping.
    JawRight = "JawRight"  # Pushes the jawbone right. Basis on medial pterygoid and lateral pterygoid's general action of shifting the jaw sideways.
    JawLeft = "JawLeft"  # Pushes the jawbone left. Basis on medial pterygoid and lateral pterygoid's general action of shifting the jaw sideways.
    JawForward = "JawForward"  # Pushes the jawbone forward. Basis on the lateral pterygoid's ability to shift the jaw forward.
    JawBackward = "JawBackward"  # Pulls the jawbone backwards slightly. Based on the retraction of the temporalis muscle.
    JawClench = "JawClench"  # Specific jaw muscles that forces the jaw closed. Causes the masseter muscle (visible close to the back of the jawline) to visibly flex.
    JawMandibleRaise = "JawMandibleRaise"  # Raises mandible (jawbone).

    MouthClosed = "MouthClosed"  # Closes the mouth relative to JawOpen. Basis on the complex tightening action of the orbicularis oris muscle.

    # Lip Expressions
    # 'Lip Push/Pull' group
    LipSuckUpperRight = "LipSuckUpperRight"  # Upper right part of the lip gets tucked inside the mouth. No direct muscle basis as this action is caused from many indirect movements of tucking the lips.
    LipSuckUpperLeft = "LipSuckUpperLeft"  # Upper left part of the lip gets tucked inside the mouth. No direct muscle basis as this action is caused from many indirect movements of tucking the lips.
    LipSuckLowerRight = "LipSuckLowerRight"  # Lower right part of the lip gets tucked inside the mouth. No direct muscle basis as this action is caused from many indirect movements of tucking the lips.
    LipSuckLowerLeft = "LipSuckLowerLeft"  # Lower left part of the lip gets tucked inside the mouth. No direct muscle basis as this action is caused from many indirect movements of tucking the lips.

    LipSuckCornerRight = "LipSuckCornerRight"  # The right corners of the lips fold inward and into the mouth. Basis on the lips ability to stretch inwards from suction.
    LipSuckCornerLeft = "LipSuckCornerLeft"  # The left corners of the lips fold inward and into the mouth. Basis on the lips ability to stretch inwards from suction.

    LipFunnelUpperRight = "LipFunnelUpperRight"  # Upper right part of the lip pushes outward into a funnel shape. Basis on the orbicularis oris orbital muscle around the mouth pushing outwards and puckering.
    LipFunnelUpperLeft = "LipFunnelUpperLeft"  # Upper left part of the lip pushes outward into a funnel shape. Basis on the orbicularis oris orbital muscle around the mouth pushing outwards and puckering.
    LipFunnelLowerRight = "LipFunnelLowerRight"  # Lower right part of the lip pushes outward into a funnel shape. Basis on the orbicularis oris orbital muscle around the mouth pushing outwards and puckering.
    LipFunnelLowerLeft = "LipFunnelLowerLeft"  # Lower left part of the lip pushes outward into a funnel shape. Basis on the orbicularis oris orbital muscle around the mouth pushing outwards and puckering.

    LipPuckerUpperRight = "LipPuckerUpperRight"  # Upper right part of the lip pinches inward and pushes outward. Basis on complex action of the orbicularis-oris orbital muscle around the lips.
    LipPuckerUpperLeft = "LipPuckerUpperLeft"  # Upper left part of the lip pinches inward and pushes outward. Basis on complex action of the orbicularis-oris orbital muscle around the lips.
    LipPuckerLowerRight = "LipPuckerLowerRight"  # Lower right part of the lip pinches inward and pushes outward. Basis on complex action of the orbicularis-oris orbital muscle around the lips.
    LipPuckerLowerLeft = "LipPuckerLowerLeft"  # Lower left part of the lip pinches inward and pushes outward. Basis on complex action of the orbicularis-oris orbital muscle around the lips.

    # 'Upper lip raiser' group
    MouthUpperUpRight = "MouthUpperUpRight"  # Upper right part of the lip is pulled upward. Basis on the levator labii superioris muscle.
    MouthUpperUpLeft = "MouthUpperUpLeft"  # Upper left part of the lip is pulled upward. Basis on the levator labii superioris muscle.
    MouthUpperDeepenRight = "MouthUpperDeepenRight"  # Upper outer right part of the lip is pulled upward, backward, and rightward. Basis on the zygomaticus minor muscle.
    MouthUpperDeepenLeft = "MouthUpperDeepenLeft"  # Upper outer left part of the lip is pulled upward, backward, and rightward. Basis on the zygomaticus minor muscle.
    NoseSneerRight = "NoseSneerRight"  # The right side face pulls upward into a sneer and raises the inner part of the lips at extreme ranges. Based on levator labii superioris alaeque nasi muscle.
    NoseSneerLeft = "NoseSneerLeft"  # The right side face pulls upward into a sneer and raises the inner part of the lips slightly at extreme ranges. Based on levator labii superioris alaeque nasi muscle.

    # 'Lower lip depressor' group
    MouthLowerDownRight = "MouthLowerDownRight"  # Lower right part of the lip is pulled downward. Basis on the depressor labii inferioris muscle.
    MouthLowerDownLeft = "MouthLowerDownLeft"  # Lower left part of the lip is pulled downward. Basis on the depressor labii inferioris muscle.

    # 'Mouth Direction' group
    MouthUpperRight = "MouthUpperRight"  # Moves upper lip right. Basis on the general horizontal movement action of the upper orbicularis oris orbital, levator anguli oris, and buccinator muscle grouping.
    MouthUpperLeft = "MouthUpperLeft"  # Moves upper lip left. Basis on the general horizontal movement action of the upper orbicularis oris orbital, levator anguli oris, and buccinator muscle grouping.
    MouthLowerRight = "MouthLowerRight"  # Moves lower lip right. Basis on the general horizontal movement action of the lower orbicularis oris orbital, risorius, depressor labii inferioris, and buccinator muscle grouping.
    MouthLowerLeft = "MouthLowerLeft"  # Moves lower lip left. Basis on the general horizontal movement action of the lower orbicularis oris orbital, risorius, depressor labii inferioris, and buccinator muscle grouping.

    # 'Smile' group
    MouthCornerPullRight = "MouthCornerPullRight"  # Right side of the lip is pulled diagnally upwards and rightwards significantly. Basis on the action of the levator anguli oris muscle.
    MouthCornerPullLeft = "MouthCornerPullLeft"  # Left side of the lip is pulled diagnally upwards and leftwards significantly. Basis on the action of the levator anguli oris muscle.
    MouthCornerSlantRight = "MouthCornerSlantRight"  # Right corner of the lip is pulled upward slightly. Basis on the action of the levator anguli oris muscle.
    MouthCornerSlantLeft = "MouthCornerSlantLeft"  # Left corner of the lip is pulled upward slightly. Basis on the action of the levator anguli oris muscle.

    # 'Sad' group
    MouthFrownRight = "MouthFrownRight"  # Right corner of the lip is pushed downward. Basis on the action of the depressor anguli oris muscle. Directly opposes the levator muscles.
    MouthFrownLeft = "MouthFrownLeft"  # Left corner of the lip is pushed downward. Basis on the action of the depressor anguli oris muscle. Directly opposes the levator muscles.
    MouthStretchRight = "MouthStretchRight"  # Stretches the right side lips together horizontally and thins them vertically slightly. Basis on the risorius muscle.
    MouthStretchLeft = "MouthStretchLeft"  # Stretches the left side lips together horizontally and thins them vertically slightly. Basis on the risorius muscle.

    MouthDimpleRight = "MouthDimpleRight"  # Right corner of the lip is pushed backwards into the face, creating a dimple. Basis on buccinator muscle structure.
    MouthDimpleLeft = "MouthDimpleLeft"  # Left corner of the lip is pushed backwards into the face, creating a dimple. Basis on buccinator muscle structure.

    MouthRaiserUpper = "MouthRaiserUpper"  # Raises the upper part of the mouth in response to MouthRaiserLower. No muscular basis.
    MouthRaiserLower = "MouthRaiserLower"  # Raises the lower part of the mouth. Based on the complex lower pushing action of the mentalis muscle.
    MouthPressRight = "MouthPressRight"  # Squeezes the right side lips together vertically and flattens them. Basis on the complex tightening action of the orbicularis oris muscle.
    MouthPressLeft = "MouthPressLeft"  # Squeezes the left side lips together vertically and flattens them. Basis on the complex tightening action of the orbicularis oris muscle.
    MouthTightenerRight = "MouthTightenerRight"  # Squeezes the right side lips together horizontally and thickens them vertically slightly. Basis on the complex tightening action of the orbicularis oris muscle.
    MouthTightenerLeft = "MouthTightenerLeft"  # Squeezes the right side lips together horizontally and thickens them vertically slightly. Basis on the complex tightening action of the orbicularis oris muscle.

    # Tongue Expressions
    TongueOut = "TongueOut"  # Combined LongStep1 and LongStep2 into one shape, as it can be emulated in-animation

    # Based on SRanipal tracking standard's tongue tracking.
    TongueUp = "TongueUp"  # Tongue points in an upward direction.
    TongueDown = "TongueDown"  # Tongue points in a downward direction.
    TongueRight = "TongueRight"  # Tongue points in a rightward direction.
    TongueLeft = "TongueLeft"  # Tongue points in a leftward direction.

    # Based on https://www.naun.org/main/NAUN/computers/2018/a042007-060.pdf
    TongueRoll = "TongueRoll"  # Rolls up the sides of the tongue into a 'hotdog bun' shape.
    TongueBendDown = "TongueBendDown"  # Pushes tip of the tongue below the rest of the tongue in an arch.
    TongueCurlUp = "TongueCurlUp"  # Pushes tip of the tongue above the rest of the tongue in an arch.
    TongueSquish = "TongueSquish"  # Tongue becomes thinner width-wise and slightly thicker height-wise.
    TongueFlat = "TongueFlat"  # Tongue becomes thicker width-wise and slightly thinner height-wise.

    TongueTwistRight = "TongueTwistRight"  # Tongue tip rotates clockwise from POV with the rest of the tongue following gradually.
    TongueTwistLeft = "TongueTwistLeft"  # Tongue tip rotates counter-clockwise from POV with the rest of the tongue following gradually.

    # Throat/Neck Expressions
    SoftPalateClose = "SoftPalateClose"  # Visibly lowers the back of the throat (soft palate) inside the mouth to close off the throat.
    ThroatSwallow = "ThroatSwallow"  # Visibly causes the Adam's apple to pull upward into the throat as if swallowing.

    NeckFlexRight = "NeckFlexRight"  # Flexes the Right side of the neck and face (causes the right corner of the face to stretch towards.)
    NeckFlexLeft = "NeckFlexLeft"  # Flexes the left side of the neck and face (causes the left corner of the face to stretch towards.)

    # Custom MediaPipe Module Parameters
    EyeXRight = "EyeXRight"
    EyeYRight = "EyeYRight"
    EyeOpennessRight = "EyeOpennessRight"
    EyePupilDiameterMMRight = "EyePupilDiameterMMRight"

    EyeXLeft = "EyeXLeft"
    EyeYLeft = "EyeYLeft"
    EyeOpennessLeft = "EyeOpennessLeft"
    EyePupilDiameterMMLeft = "EyePupilDiameterMMLeft"

    HeadX = "HeadX"
    HeadY = "HeadY"
    HeadZ = "HeadZ"

    HeadPitch = "HeadPitch"
    HeadYaw = "HeadYaw"
    HeadRoll = "HeadRoll"
