using Newtonsoft.Json;

namespace FoxyFaceVRCFTInterface.Core.Config;

public class FoxyFaceConfig
{
    [JsonProperty(PropertyName = "DontTouchThisField-ConfigVersion")]
    public string ConfigVersion { get; set; } = "";

    public ushort FoxyFacePort { get; init; } = 54321;
    public ushort SearchFoxyFaceTimeoutSeconds { get; init; } = 60;
    public bool ShowAllLogs { get; init; } = false;
}