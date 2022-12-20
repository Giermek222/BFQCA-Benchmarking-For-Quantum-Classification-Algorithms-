import subprocess
import os

LOG_FILE = "log_lib_make.txt"

try:
    import wheel
    command_line = "cd cowskit_library && " \
                    "python setup.py bdist_wheel && " \
                    "python -m pip install dist/cowskit-1.0.0-py3-none-any.whl"
except Exception as e:
    command_line = "python -m pip install --upgrade pip && " \
                    "python -m pip install wheel && " \
                    "cd quantumAI && " \
                    "python setup.py bdist_wheel && " \
                    "python -m pip install dist/cowskit-1.0.0-py3-none-any.whl"

with open(LOG_FILE, "w") as logfile:
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
        print(f"Script execution failed, check {LOG_FILE} for details")
        print(e.with_traceback())


