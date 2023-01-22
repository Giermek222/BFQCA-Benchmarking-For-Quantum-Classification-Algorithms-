import os
import sys

from backend.logger import Log

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
    Log.info("Quantum Benchmarking initializing...")

    algorithms_path = f"{path_to_main_file}/custom_algorithms"
    datasets_path = f"{path_to_main_file}/custom_datasets"

    Log.debug("Temporarily added ", algorithms_path, " to system PATH")
    Log.debug("Temporarily added ", datasets_path, " to system PATH")

    sys.path.append(algorithms_path)
    sys.path.append(datasets_path)

