namespace FoxyFaceVRCFTInterface.Core.VRCFT;

public class OtherModulesBlockBypass
{
    public bool BypassEnabled { get; set; }
    public bool EyeInPriority { get; set; }

    private readonly bool _eyeSupported;
    private readonly bool _expressionSupported;

    public OtherModulesBlockBypass(bool eyeSupported, bool expressionSupported)
    {
        _eyeSupported = eyeSupported;
        _expressionSupported = expressionSupported;
    }

    public (bool SupportsEye, bool SupportsExpression) GetSupportedStates()
    {
        if (!_eyeSupported && !_expressionSupported) return (EyeInPriority, !EyeInPriority);

        return (_eyeSupported, _expressionSupported);
    }

    public (bool eyeSuccess, bool expressionSuccess) Initialize(bool eyeAvailable, bool expressionAvailable)
    {
        if (!BypassEnabled)
        {
            return
                (eyeAvailable && _eyeSupported, expressionAvailable && _expressionSupported);
        }

        if (eyeAvailable == expressionAvailable) return (EyeInPriority, !EyeInPriority);

        return (!eyeAvailable, !expressionAvailable);
    }

    public bool IsUsingEye(bool usingEye)
    {
        return BypassEnabled ? _eyeSupported : usingEye && _eyeSupported;
    }

    public bool IsUsingExpression(bool usingExpression)
    {
        return BypassEnabled ? _expressionSupported : usingExpression && _expressionSupported;
    }
}