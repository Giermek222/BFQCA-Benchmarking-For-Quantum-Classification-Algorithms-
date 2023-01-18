import sys
import os

from backend.files import get_logs_folder_path, get_log_file_path, get_file_realpath
from backend.commands import run_command

LIBRARY_FOLDER = "library"

path_to_main_file = get_file_realpath(__file__)
path_to_logs_folder = get_logs_folder_path(path_to_main_file)
uninstall_log_path = get_log_file_path(path_to_logs_folder, "uninstall")
install_log_path = get_log_file_path(path_to_logs_folder, "install")

### UNINSTALL CODE
with open(uninstall_log_path, "w") as log_file:
    command_line = "python -m pip uninstall -y cowskit"

    try:
        if "-f" not in sys.argv[1:]:
            import cowskit
        else:
            log_file.write("Force uninstall 'cowskit'")

        run_command(command_line, log_file)
        print("Module 'cowskit' has been uninstalled!")

    except ImportError as e:
        print("Module 'cowskit' was not found, so it will not be uninstalled.")
        print("If this is a mistake, error can be found in the log files.")
        log_file.write(str(e))

    except Exception as e:
        print(f"Uninstall script execution failed, check {uninstall_log_path} for details.")
        log_file.write(str(e))


# INSTALL CODE
with open(install_log_path, "w") as log_file:
    command_line = f"cd {LIBRARY_FOLDER} && "

    try:
        import wheel
    except Exception as e:
        command_line += "python -m pip install --upgrade pip && " \
                        "python -m pip install wheel && "

    command_line += "python setup.py bdist_wheel && " \
                    "python -m pip install dist/cowskit-1.0.0-py3-none-any.whl"

    try:
        run_command(command_line, log_file)
        print("Module 'cowskit' has been installed!")

    except Exception as e:
        print(f"Install script execution failed, check {install_log_path} for details.")
        log_file.write(str(e))