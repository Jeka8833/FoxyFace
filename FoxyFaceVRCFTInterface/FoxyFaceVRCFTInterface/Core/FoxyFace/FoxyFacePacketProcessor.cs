using System.Collections.ObjectModel;
using Microsoft.Extensions.Logging;
using VRCFaceTracking;
using VRCFaceTracking.Core.Params.Expressions;

namespace FoxyFaceVRCFTInterface.Core.FoxyFace;

public class FoxyFacePacketProcessor
{
    private const string EyeRightX = "EyeXRight";
    private const string EyeRightY = "EyeYRight";
    private const string EyeRightOpenness = "EyeOpennessRight";
    private const string EyeRightPupilDiameterMm = "EyePupilDiameterMMRight";

    private const string EyeLeftX = "EyeXLeft";
    private const string EyeLeftY = "EyeYLeft";
    private const string EyeLeftOpenness = "EyeOpennessLeft";
    private const string EyeLeftPupilDiameterMm = "EyePupilDiameterMMLeft";

    private const string HeadX = "HeadX";
    private const string HeadY = "HeadY";
    private const string HeadZ = "HeadZ";
    private const string HeadPitch = "HeadPitch";
    private const string HeadYaw = "HeadYaw";
    private const string HeadRoll = "HeadRoll";


    private readonly ReadOnlyDictionary<string, int> _unifiedExpressionsDictionary =
        GenerateUnifiedExpressionsDictionary();

    private readonly bool _headRotationAllowed = UnifiedTracking.Data.GetType().GetField("Head") != null;

    public FoxyFacePacketProcessor(ILogger logger)
    {
        logger.LogInformation("Available {} unified expressions. Head Rotation Allowed: {}",
            _unifiedExpressionsDictionary.Count, _headRotationAllowed);
    }

    public void UpdateEyes(Dictionary<string, float> foxyFaceValues)
    {
        if (foxyFaceValues.TryGetValue(EyeRightX, out float eyeRightXValue))
        {
            UnifiedTracking.Data.Eye.Right.Gaze.x = eyeRightXValue;
        }

        if (foxyFaceValues.TryGetValue(EyeRightY, out float eyeRightYValue))
        {
            UnifiedTracking.Data.Eye.Right.Gaze.y = eyeRightYValue;
        }

        if (foxyFaceValues.TryGetValue(EyeRightOpenness, out float eyeRightOpennessValue))
        {
            UnifiedTracking.Data.Eye.Right.Openness = eyeRightOpennessValue;
        }

        if (foxyFaceValues.TryGetValue(EyeRightPupilDiameterMm, out float eyeRightPupilDiameterMmValue))
        {
            UnifiedTracking.Data.Eye.Right.PupilDiameter_MM = eyeRightPupilDiameterMmValue;
        }

        if (foxyFaceValues.TryGetValue(EyeLeftX, out float eyeLeftXValue))
        {
            UnifiedTracking.Data.Eye.Left.Gaze.x = eyeLeftXValue;
        }

        if (foxyFaceValues.TryGetValue(EyeLeftY, out float eyeLeftYValue))
        {
            UnifiedTracking.Data.Eye.Left.Gaze.y = eyeLeftYValue;
        }

        if (foxyFaceValues.TryGetValue(EyeLeftOpenness, out float eyeLeftOpennessValue))
        {
            UnifiedTracking.Data.Eye.Left.Openness = eyeLeftOpennessValue;
        }

        if (foxyFaceValues.TryGetValue(EyeLeftPupilDiameterMm, out float eyeLeftPupilDiameterMmValue))
        {
            UnifiedTracking.Data.Eye.Left.PupilDiameter_MM = eyeLeftPupilDiameterMmValue;
        }
    }

    public void UpdateExpression(Dictionary<string, float> foxyFaceValues)
    {
        foreach (KeyValuePair<string, float> pair in foxyFaceValues)
        {
            if (_unifiedExpressionsDictionary.TryGetValue(pair.Key, out int shapeKey))
            {
                UnifiedTracking.Data.Shapes[shapeKey].Weight = pair.Value;
            }
        }

        if (_headRotationAllowed)
        {
            if (foxyFaceValues.TryGetValue(HeadX, out float headXValue))
            {
                UnifiedTracking.Data.Head.HeadPosX = headXValue;
            }

            if (foxyFaceValues.TryGetValue(HeadY, out float headYValue))
            {
                UnifiedTracking.Data.Head.HeadPosY = headYValue;
            }

            if (foxyFaceValues.TryGetValue(HeadZ, out float headZValue))
            {
                UnifiedTracking.Data.Head.HeadPosZ = headZValue;
            }

            if (foxyFaceValues.TryGetValue(HeadPitch, out float headPitchValue))
            {
                UnifiedTracking.Data.Head.HeadPitch = headPitchValue;
            }

            if (foxyFaceValues.TryGetValue(HeadYaw, out float headYawValue))
            {
                UnifiedTracking.Data.Head.HeadYaw = headYawValue;
            }

            if (foxyFaceValues.TryGetValue(HeadRoll, out float headRollValue))
            {
                UnifiedTracking.Data.Head.HeadRoll = headRollValue;
            }
        }
    }

    private static ReadOnlyDictionary<string, int> GenerateUnifiedExpressionsDictionary()
    {
        Dictionary<string, int> unifiedExpressionsDictionary = new();

        foreach (var value in Enum.GetValues(typeof(UnifiedExpressions)))
        {
            try
            {
                unifiedExpressionsDictionary[((UnifiedExpressions)value).ToString()] = (int)value;
            }
            catch (Exception)
            {
                // ignored
            }
        }

        try
        {
            unifiedExpressionsDictionary.Remove(nameof(UnifiedExpressions.Max));
        }
        catch (Exception)
        {
            // ignored
        }

        return new ReadOnlyDictionary<string, int>(unifiedExpressionsDictionary);
    }
}