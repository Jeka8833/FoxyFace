using System.Reflection;

namespace FoxyFaceVRCFTInterface.Core.Config.Migration;

public static class ModuleVersion
{
    public static readonly Version? FileVersion = GetFileVersion();

    private static Version? GetFileVersion()
    {
        try
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            Version? version = assembly.GetName().Version;
            if (version == null) return null;

            int build = version.Build == -1 ? 0 : version.Build;
            int revision = version.Revision == -1 ? 0 : version.Revision;

            return new Version(version.Major, version.Minor, build, revision);
        }
        catch (Exception)
        {
            return null;
        }
    }
}