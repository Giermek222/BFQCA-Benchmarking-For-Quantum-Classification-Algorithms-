import subprocess
import os

LOG_FILE = "log_lib_delete.txt"

command_line = "python -m pip uninstall -y cowskit"

with open(LOG_FILE, "w") as logfile:
    try:
        subprocess.run(command_line,
                    shell=True,
                    check=True,
                    stdout=logfile,
                    stderr=logfile,
                    cwd=os.getcwd(),
                    env=os.environ.copy())
        print("Module 'cowskit' has been uninstalled!")
    except Exception as e:
        print(f"Script execution failed, check {LOG_FILE} for details")
        print(e.with_traceback())
