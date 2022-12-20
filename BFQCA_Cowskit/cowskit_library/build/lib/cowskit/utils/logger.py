from enum import Enum

class LoggerLevel(Enum):
    DEBUG   = 0
    INFO    = 1
    WARNING = 2
    ERROR   = 3
    FATAL   = 4

class Logger:
    level = LoggerLevel.INFO
    def debug(*args):
        if Logger.level.value >= LoggerLevel.DEBUG.value:
            print("[DEBUG] " + "".join(str(arg) for arg in args))
    def info(*args):
        if Logger.level.value >= LoggerLevel.DEBUG.value:
            print("[INFO] " + "".join(str(arg) for arg in args))
    def warning(*args):
        if Logger.level.value >= LoggerLevel.DEBUG.value:
            print("[WARN] " + "".join(str(arg) for arg in args))
    def error(*args):
        if Logger.level.value >= LoggerLevel.DEBUG.value:
            print("[ERROR] " + "".join(str(arg) for arg in args))
    def fatal(*args):
        if Logger.level.value >= LoggerLevel.DEBUG.value:
            print("[FATAL] " + "".join(str(arg) for arg in args))