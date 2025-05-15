using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace FoxyFaceVRCFTInterface.Core.FoxyFace;

public class FoxyFaceUdpClient : IDisposable
{
    private static IPEndPoint _remoteIpEndPoint = new(IPAddress.Any, 0);

    private readonly UdpClient _udpClient;
    private readonly ILogger _logger;
    private readonly FoxyFaceUdpAutoConnect? _foxyFaceUdpAutoConnect;
    public ushort SocketPort { get; private set; }
    private long _lastTimestamp;

    public int ReceiveTimeoutMillis
    {
        get => _udpClient.Client.ReceiveTimeout;
        set => _udpClient.Client.ReceiveTimeout = value;
    }

    /// <summary>
    /// The port you passed may be different from the one on which the socket will be opened.
    /// You can get an active port via FoxyFaceUdpClient.SocketPort
    /// </summary>
    /// <exception cref="Exception">If UDP Socket can't be opened</exception>
    public FoxyFaceUdpClient(ushort port, ILogger logger)
    {
        SocketPort = port;
        _logger = logger;

        _udpClient = TryCreateUdpSocket();

        try
        {
            _foxyFaceUdpAutoConnect = new FoxyFaceUdpAutoConnect(SocketPort, logger);
        }
        catch (Exception e)
        {
            logger.LogWarning(e, "Failed to create UDP Socket for auto connect");
        }
    }

    public FoxyFaceDto.ConfigDto? TryConnect(ushort connectTimeoutSeconds)
    {
        _foxyFaceUdpAutoConnect?.TryStartBroadcasting();

        ReceiveTimeoutMillis = connectTimeoutSeconds * 1000;

        long startTime = Stopwatch.GetTimestamp();

        do
        {
            FoxyFaceDto? packet = TryRequest();

            if (packet != null) return packet.Config ?? new FoxyFaceDto.ConfigDto();
        } while (Stopwatch.GetElapsedTime(startTime).TotalSeconds < connectTimeoutSeconds);

        return null;
    }

    public FoxyFaceDto? TryRequest()
    {
        FoxyFaceDto? lastPacket = null;

        do
        {
            try
            {
                byte[] data = _udpClient.Receive(ref _remoteIpEndPoint);
                string dataStr = System.Text.Encoding.UTF8.GetString(data);
                FoxyFaceDto? currentPacket = JsonConvert.DeserializeObject<FoxyFaceDto>(dataStr);

                if (currentPacket != null && currentPacket.PingPacket)
                {
                    _foxyFaceUdpAutoConnect?.TryStopBroadcasting();
                    
                    return currentPacket;
                }

                // Timestamp == 0 when Timestamp is absent
                if (currentPacket != null &&
                    (_lastTimestamp == 0L || currentPacket.Timestamp - _lastTimestamp >= 0L ||
                     currentPacket.Timestamp - _lastTimestamp < -120_000L)) // 2 minute, bypass soft-lock
                {
                    _lastTimestamp = currentPacket.Timestamp;

                    lastPacket = currentPacket;
                }
            }
            catch (ThreadInterruptedException)
            {
                throw;
            }
            catch (SocketException e)
            {
                Thread.Sleep(1);

                _logger.LogWarning("FoxyFace UDP Socket error, is FoxyFace app opened and connected?\n" +
                                   "Disable the module via the VRCFT interface to stop spamming the logs.");
                _logger.LogDebug(e, "Additional StackTrace");

                _foxyFaceUdpAutoConnect?.TryStartBroadcasting();
            }
            catch (Exception e)
            {
                Thread.Sleep(1);

                _logger.LogWarning(e, "Process UDP packet error");
            }
        } while (_udpClient.Available > 0); // Has new data, reduce latency

        if (lastPacket == null) return null;

        _foxyFaceUdpAutoConnect?.TryStopBroadcasting();

        return lastPacket;
    }

    public void Dispose()
    {
        try
        {
            _foxyFaceUdpAutoConnect?.Dispose();
        }
        catch (Exception)
        {
            // ignored
        }

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

    /// <exception cref="Exception">If it can't create UDP Socket</exception>
    private UdpClient TryCreateUdpSocket()
    {
        for (int i = 0; i <= IPEndPoint.MaxPort; i++)
        {
            try
            {
                return new UdpClient(SocketPort);
            }
            catch (SocketException socketException)
            {
                if (socketException.SocketErrorCode != SocketError.AddressAlreadyInUse) throw;

                _logger.LogInformation("UDP port {} is busy, the next one will be used!", SocketPort);

                SocketPort++; // controlled ushort overflow 
            }
        }

        throw new Exception("All ports are busy, how?");
    }
}