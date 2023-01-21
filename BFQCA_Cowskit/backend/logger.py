from enum import Enum

class LogLevel(Enum):
    FATAL   = 0
    ERROR   = 1
    WARNING = 2
    INFO    = 3
    DEBUG   = 4

class Log:
    level = LogLevel.INFO
    def debug(*args):
        if Log.level.value >= LogLevel.DEBUG.value:
            print("[DEBUG] " + "".join(str(arg) for arg in args))
    def info(*args):
        if Log.level.value >= LogLevel.INFO.value:
            print("[INFO] " + "".join(str(arg) for arg in args))
    def warning(*args):
        if Log.level.value >= LogLevel.WARNING.value:
            print("[WARN] " + "".join(str(arg) for arg in args))
    def error(*args):
        if Log.level.value >= LogLevel.ERROR.value:
            print("[ERROR] " + "".join(str(arg) for arg in args))
    def fatal(*args):
        if Log.level.value >= LogLevel.FATAL.value:
            print("[FATAL] " + "".join(str(arg) for arg in args))