import backend.argparser as ba
import backend.files as fl
import os

import subprocess
from cowskit.datasets import LinesDataset

for alg in ba.PREDEFINED_ALGORITHMS:
    for ds in ba.PREDEFINED_DATASETS:
        path = fl.get_file_realpath(__file__)
        command = f"python \"{path}/main.py\" -a {alg} -d {ds}"

        logs_folder = fl.get_logs_folder_path(path)
        logs_file = f"{logs_folder}/test_{alg}_{ds}.txt"
        with open(logs_file, "w") as log_file:
            try:
                subprocess.run(command,
                            shell=True,
                            check=True,
                            stdout=log_file,
                            stderr=log_file,
                            cwd=os.getcwd(),
                            env=os.environ.copy())
            except: pass
        with open(logs_file, "r") as log_file:
            full_output = "".join(log_file.readlines())

            if full_output.find("Request body:") != -1:
                print(f"+ {alg} + {ds} passed")
            else:
                print(f"- {alg} + {ds} failed")

