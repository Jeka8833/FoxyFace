using System.Net.Sockets;
using System.Text;
using FoxyFaceVRCFTInterface.Core.Config.Migration;
using Microsoft.Extensions.Logging;
using Timer = System.Timers.Timer;

namespace FoxyFaceVRCFTInterface.Core.FoxyFace;

public class FoxyFaceUdpAutoConnect : IDisposable
{
    private const ushort BroadcastPort = 57130;

    private readonly UdpClient _udpClient;
    private readonly Timer _timer = new();

    /// <exception cref="Exception" />
    public FoxyFaceUdpAutoConnect(ushort port, ILogger logger)
    {
        _udpClient = new UdpClient();

        string packetText = "{\"Port\":" + port + (ModuleVersion.FileVersion == null
            ? "}"
            : ",\"InterfaceVersion\":\"" + ModuleVersion.FileVersion + "\"}");

        byte[] packet = Encoding.UTF8.GetBytes(packetText);

        _timer.Elapsed += (_, _) =>
        {
            try
            {
                _udpClient.Send(packet, packet.Length, "255.255.255.255", BroadcastPort);
            }
            catch (Exception e)
            {
                logger.LogDebug(e, "Failed to send UDP Packet");
            }
        };

        _timer.AutoReset = true;
        _timer.Interval = 1000;
    }

    public void TryStartBroadcasting()
    {
        _timer.Enabled = true;
    }

    public void TryStopBroadcasting()
    {
        _timer.Enabled = false;
    }

    public void Dispose()
    {
        _timer.Dispose();

        try
        {
            _udpClient.Close();
        }
        catch (Exception)
        {
            // ignored
        }

        _udpClient.Dispose();
    }
}