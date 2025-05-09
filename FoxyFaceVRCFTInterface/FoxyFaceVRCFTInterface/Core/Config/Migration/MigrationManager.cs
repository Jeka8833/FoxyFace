using Microsoft.Extensions.Logging;

namespace FoxyFaceVRCFTInterface.Core.Config.Migration;

public class MigrationManager
{
    private readonly Version? _moduleVersion;
    private readonly ILogger _logger;

    public MigrationManager(Version? moduleVersion, ILogger logger)
    {
        _moduleVersion = moduleVersion;
        _logger = logger;

        if (_moduleVersion == null)
        {
            _logger.LogDebug("Are you know that module version is null?");
        }
    }

    public void TryMigrate(FoxyFaceConfig config)
    {
        if (_moduleVersion == null) return;

        try
        {
            Version configVersion = new(config.ConfigVersion);
            if (configVersion == _moduleVersion) return;

            try
            {
                Migrate(config, configVersion);
            }
            catch (Exception e)
            {
                _logger.LogWarning(e, "Failed to migrate configuration");
            }
        }
        catch (Exception e)
        {
            _logger.LogDebug(e, "Failed to parse version, I think user is too smart");
        }
    }

    public void UpdateConfigVersion(FoxyFaceConfig config)
    {
        if (_moduleVersion == null) return;

        config.ConfigVersion = _moduleVersion.ToString();
    }

    private void Migrate(FoxyFaceConfig config, Version configVersion)
    {
        /* Example migration
        if (_moduleVersion > configVersion)
        {
            config.EyeMapper.EyeGazeX = false;
        }*/
    }
}