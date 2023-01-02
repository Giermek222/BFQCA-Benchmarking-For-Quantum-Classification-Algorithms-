import subprocess
import os

UNINSTALL_LOG_FILE = "logs/lib_delete.txt"
INSTALL_LOG_FILE = "logs/lib_make.txt"
LIB_FOLDER = "cowskit_library"

### UNINSTALL CODE
command_line = "python -m pip uninstall -y cowskit"

with open(UNINSTALL_LOG_FILE, "w") as logfile:
    try:
        import cowskit
        subprocess.run(command_line,
                    shell=True,
                    check=True,
                    stdout=logfile,
                    stderr=logfile,
                    cwd=os.getcwd(),
                    env=os.environ.copy())
        print("Module 'cowskit' has been uninstalled!")

    except ImportError as e:
        print(f"Cowskit is not installed (or raised an exception), so it will not be uninstalled. Error can be found in the log files.")
        logfile.write(str(e))

    except Exception as e:
        print(f"Script execution failed, check {UNINSTALL_LOG_FILE} for details")
        logfile.write(str(e))

# WHEEL CODE
try:
    import wheel
    command_line = f"cd {LIB_FOLDER} && " \
                    "python setup.py bdist_wheel && " \
                    "python -m pip install dist/cowskit-1.0.0-py3-none-any.whl"
except Exception as e:
    command_line = f"cd {LIB_FOLDER} && " \
                    "python -m pip install --upgrade pip && " \
                    "python -m pip install wheel && " \
                    "python setup.py bdist_wheel && " \
                    "python -m pip install dist/cowskit-1.0.0-py3-none-any.whl"

# INSTALL CODE
with open(INSTALL_LOG_FILE, "w") as logfile:
    try:
        subprocess.run(command_line,
                    shell=True,
                    check=True,
                    stdout=logfile,
                    stderr=logfile,
                    cwd=os.getcwd(),
                    env=os.environ.copy())
        print("Module 'cowskit' has been installed!")

    except Exception as e:
        print(f"Script execution failed, check {INSTALL_LOG_FILE} for details")
        logfile.write(str(e))