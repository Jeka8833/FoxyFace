using System.Net;
using System.Net.Sockets;
using FoxyFaceVRCFTInterface.Core.Config;
using FoxyFaceVRCFTInterface.Core.FoxyFace;
using FoxyFaceVRCFTInterface.Core.Logger;
using Microsoft.Extensions.Logging;
using VRCFaceTracking;
using VRCFaceTracking.Core.Library;

namespace FoxyFaceVRCFTInterface;

// ReSharper disable once InconsistentNaming
// ReSharper disable once UnusedType.Global
public class FoxyFaceVRCFTInterface : ExtTrackingModule
{
    // If App From Windows Store then:
    // C:\Users\[UserName]\AppData\Local\Packages\[96ba052f-0948-44d8-86c4-a0212e4ae047_4s4k90pjvq32p]\LocalCache\Roaming\VRCFaceTracking\Configs\FoxyFace\FoxyFace.json
    //
    // Where [UserName] is your Windows username
    // and [96ba052f-0948-44d8-86c4-a0212e4ae047_4s4k90pjvq32p] is the VRCFaceTracking package name, for you, it can be different, try to search similar folder
    //
    // In other cases, check the logs, where you can find the path to the configuration file.
    private static readonly string ConfigPath = Path.Combine(
        VRCFaceTracking.Core.Utils.PersistentDataDirectory, "Configs", "FoxyFace", "FoxyFace.json");

    public ILogger FoxyFaceLogger { get; private set; } = null!;
    public ILogger FoxyFaceSpamLogger { get; private set; } = null!;
    public ConfigManager ConfigManager { get; private set; } = null!;

    private FoxyFaceUdpClient _udpClient = null!;
    private FoxyFacePacketProcessor _packetProcessor = null!;

    public override (bool SupportsEye, bool SupportsExpression) Supported => (true, true);

    public override (bool eyeSuccess, bool expressionSuccess) Initialize(bool eyeAvailable, bool expressionAvailable)
    {
        FoxyFaceLogger = new VrcftExceptionFixerLogger(Logger);

        ConfigManager = new ConfigManager(ConfigPath, FoxyFaceLogger);
        ConfigManager.LoadAndMigrateConfig();

        FoxyFaceLogger.LogInformation("The FoxyFace Configuration file is located in: {}", ConfigPath);

        FoxyFaceSpamLogger = ConfigManager.Config.ShowAllLogs ? FoxyFaceLogger : new SkipSpamLogger(FoxyFaceLogger);

        try
        {
            _udpClient = new FoxyFaceUdpClient(ConfigManager.Config.FoxyFacePort, FoxyFaceSpamLogger);
        }
        catch (Exception e)
        {
            ModuleInformation.Active = false;

            FoxyFaceLogger.LogError(e, "Failed to create UDP socket, module disabled.");

            return (false, false);
        }

        FoxyFaceLogger.LogInformation("FoxyFace interface is waiting for connection.\n" +
                                      "Please try entering one of the following addresses ({}) in the \"IP: \" field " +
                                      "and then set \"Port:\" to {}.\n" +
                                      "If you fail to do so in {} seconds, the module will be disabled " +
                                      "and you will have to restart the VRCFT application to try to connect again.",
            string.Join(", ", GetLocalIpAddresses()), _udpClient.SocketPort,
            ConfigManager.Config.SearchFoxyFaceTimeoutSeconds);

        FoxyFaceDto.ConfigDto? packetConfig =
            _udpClient.TryConnect(ConfigManager.Config.SearchFoxyFaceTimeoutSeconds);

        if (packetConfig == null)
        {
            Teardown();

            ModuleInformation.Active = false;

            FoxyFaceLogger.LogInformation(
                "The FoxyFace app failed to connect to this computer in {} seconds. " +
                "Disabling the module...", ConfigManager.Config.SearchFoxyFaceTimeoutSeconds);

            return (false, false);
        }

        _udpClient.ReceiveTimeoutMillis = packetConfig.UdpReadTimeoutMs;

        ModuleInformation.Name = "FoxyFace";

        try
        {
            var stream = GetType()
                .Assembly
                .GetManifestResourceStream("FoxyFaceVRCFTInterface.Assets.foxyface-logo.png");

            ModuleInformation.StaticImages =
                stream != null ? new List<Stream> { stream } : ModuleInformation.StaticImages;
        }
        catch (Exception e)
        {
            FoxyFaceLogger.LogWarning(e, "Failed to load FoxyFace Icon");
        }

        _packetProcessor = new FoxyFacePacketProcessor(FoxyFaceSpamLogger);

        FoxyFaceLogger.LogInformation("FoxyFace app is connected successfully!");

        return (eyeAvailable, expressionAvailable);
    }

    public override void Update()
    {
        try
        {
            if (Status != ModuleState.Active)
            {
                Thread.Sleep(100);

                return;
            }

            FoxyFaceDto? packet = _udpClient.TryRequest();

            if (packet?.Values == null || packet.Values.Count == 0) return;
            
            _packetProcessor.UpdateEyes(packet.Values);
            _packetProcessor.UpdateExpression(packet.Values);
        }
        catch (ThreadInterruptedException) // VRCFT doesn't send an interrupt when it wants to stop the module ((
        {
        }
        catch (Exception e)
        {
            FoxyFaceSpamLogger.LogWarning(e, "Exception in Module Update Loop");
        }
    }

    public override void Teardown()
    {
        // ReSharper disable once ConditionalAccessQualifierIsNonNullableAccordingToAPIContract
        _udpClient?.Dispose();

        FoxyFaceLogger.LogInformation("UPD Socket Closed");
    }

    private static IOrderedEnumerable<IPAddress> GetLocalIpAddresses()
    {
        try
        {
            var hostAddresses = Dns.GetHostEntry(Dns.GetHostName())
                .AddressList
                .Where(ip => ip.AddressFamily == AddressFamily.InterNetwork);

            var allAddresses = new[] { IPAddress.Loopback }
                .Concat(hostAddresses).Distinct();

            return allAddresses.OrderBy(ip => !ip.Equals(IPAddress.Loopback))
                .ThenByDescending(ip => ip.ToString().StartsWith("192.168."));
        }
        catch (Exception)
        {
            return new[] { IPAddress.Loopback }.OrderBy(_ => 0);
        }
    }
}