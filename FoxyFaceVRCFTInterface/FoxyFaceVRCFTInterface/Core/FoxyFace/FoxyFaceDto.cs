namespace FoxyFaceVRCFTInterface.Core.FoxyFace;

public class FoxyFaceDto
{
    public long Timestamp { get; init; }
    public bool PingPacket { get; init; }
    public Dictionary<string, float>? Values { get; init; } = new();
    public ConfigDto? Config { get; init; } = new();

    public class ConfigDto
    {
        public ushort UdpReadTimeoutMs { get; init; } = 5_000;
        public bool BypassOtherModulesBlock { get; init; } = false;
    }
}