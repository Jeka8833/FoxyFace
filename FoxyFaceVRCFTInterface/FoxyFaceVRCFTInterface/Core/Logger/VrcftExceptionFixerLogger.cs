using Microsoft.Extensions.Logging;

namespace FoxyFaceVRCFTInterface.Core.Logger;

// If they fix it, it will be easier to remove this extension.
public class VrcftExceptionFixerLogger : ILogger
{
    private readonly ILogger _baseLogger;

    public VrcftExceptionFixerLogger(ILogger logger)
    {
        _baseLogger = logger;
    }

    public IDisposable? BeginScope<TState>(TState state) where TState : notnull
    {
        return _baseLogger.BeginScope(state);
    }

    public bool IsEnabled(LogLevel logLevel)
    {
        return _baseLogger.IsEnabled(logLevel);
    }

    public void Log<TState>(LogLevel logLevel, EventId eventId, TState state, Exception? exception,
        Func<TState, Exception?, string> formatter)
    {
        string AddException(TState stateF, Exception? exceptionF)
        {
            if (exceptionF != null)
            {
                return $"{formatter(stateF, exceptionF)}\n{exceptionF}";
            }

            return formatter(stateF, exceptionF);
        }

        _baseLogger.Log(logLevel, eventId, state, exception, AddException);
    }
}