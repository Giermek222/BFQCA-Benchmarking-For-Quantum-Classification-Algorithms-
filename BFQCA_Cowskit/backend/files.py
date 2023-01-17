import os
import sys

from backend.log import Log

def get_file_realpath(file: str) -> str:
    path = os.path.realpath(os.path.dirname(file))
    
    return path

def get_logs_folder_path(path_to_main_file: str) -> str:
    path = f"{path_to_main_file}/logs"

    if not os.path.exists(path_to_main_file):
        os.mkdir(path_to_main_file)

    return path

def get_log_file_path(path_to_logs_folder: str, name: str) -> str:
    path = f"{path_to_logs_folder}/{name}.txt"

    return path

def add_custom_folders_to_path(path_to_main_file: str) -> None:
    algorithms_path = f"{path_to_main_file}/custom_algorithms"
    encodings_path = f"{path_to_main_file}/custom_encodings"
    datasets_path = f"{path_to_main_file}/custom_datasets"

    Log.debug("Added ", algorithms_path, " to system PATH")
    Log.debug("Added ", encodings_path, " to system PATH")
    Log.debug("Added ", datasets_path, " to system PATH")

    sys.path.append(algorithms_path)
    sys.path.append(encodings_path)
    sys.path.append(datasets_path)

