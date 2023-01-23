from enum import Enum

class LogLevel(Enum):
    FATAL   = 0
    ERROR   = 1
    WARNING = 2
    INFO    = 3
    DEBUG   = 4

class Log:
    debug_prefix = "[DEBUG] "
    info_prefix = "[INFO] "
    warning_prefix = "[WARN] "
    error_prefix = "[ERROR] "
    fatal_prefix = "[FATAL] "


    level = LogLevel.INFO
    def debug(*args):
        if Log.level.value >= LogLevel.DEBUG.value:
            print(Log.debug_prefix + "".join(str(arg) for arg in args))
    def info(*args):
        if Log.level.value >= LogLevel.INFO.value:
            print(Log.info_prefix + "".join(str(arg) for arg in args))
    def warning(*args):
        if Log.level.value >= LogLevel.WARNING.value:
            print(Log.warning_prefix + "".join(str(arg) for arg in args))
    def error(*args):
        if Log.level.value >= LogLevel.ERROR.value:
            print(Log.error_prefix + "".join(str(arg) for arg in args))
    def fatal(*args):
        if Log.level.value >= LogLevel.FATAL.value:
            print(Log.fatal_prefix + "".join(str(arg) for arg in args))