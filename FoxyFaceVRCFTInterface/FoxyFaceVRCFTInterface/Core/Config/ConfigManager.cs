using System.Text;
using FoxyFaceVRCFTInterface.Core.Config.Migration;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace FoxyFaceVRCFTInterface.Core.Config;

public class ConfigManager
{
    private readonly MigrationManager _migrationManager;
    private readonly string _configPath;
    private readonly ILogger _logger;

    public FoxyFaceConfig Config { get; private set; }

    public ConfigManager(string configPath, ILogger logger)
    {
        _migrationManager = new MigrationManager(ModuleVersion.FileVersion, logger);

        _configPath = configPath;
        _logger = logger;

        Config = new FoxyFaceConfig();
    }

    public void LoadAndMigrateConfig()
    {
        FoxyFaceConfig? config = ReadConfig();
        if (config != null)
        {
            _migrationManager.TryMigrate(config);
            Config = config;

            _logger.LogInformation("Config loaded");
        }

        SaveConfigAsync();
    }

    public void SaveConfigAsync()
    {
        // May hang operating system if someone spam SaveConfigAsync
        Thread thread = new(() => // Parent thread can be Background, don't kill this thread when app is closing
        {
            try
            {
                _migrationManager.UpdateConfigVersion(Config);
                string configJson = JsonConvert.SerializeObject(Config, Formatting.Indented);

                TryCreateConfigFolder(_configPath);

                File.WriteAllText(_configPath, configJson, Encoding.UTF8);

                _logger.LogDebug("Config saved");
            }
            catch (Exception e)
            {
                _logger.LogWarning(e, "Failed to save config");
            }
        });

        thread.Priority = ThreadPriority.Lowest;
        thread.Start();
    }

    private FoxyFaceConfig? ReadConfig()
    {
        try
        {
            if (File.Exists(_configPath))
            {
                string jsonText = File.ReadAllText(_configPath, Encoding.UTF8);

                FoxyFaceConfig? data = JsonConvert.DeserializeObject<FoxyFaceConfig>(jsonText);
                if (data == null)
                {
                    _logger.LogWarning("Failed to load configuration, data equals null.\n" +
                                       "All configuration data from FoxyFace will be deleted, sorry");
                }

                return data;
            }
        }
        catch (Exception e)
        {
            _logger.LogWarning(e, "Failed to load configuration.\n" +
                                  "All configuration data from FoxyFace will be deleted, sorry");
        }

        return null;
    }

    private void TryCreateConfigFolder(string configPath)
    {
        try
        {
            string? directory = Path.GetDirectoryName(configPath);
            if (string.IsNullOrEmpty(directory))
            {
                _logger.LogWarning("Are you trying to create a config in the root directory?");
            }
            else
            {
                Directory.CreateDirectory(directory);
            }
        }
        catch (Exception e)
        {
            _logger.LogWarning(e, "Failed to create directory for config");
        }
    }
}