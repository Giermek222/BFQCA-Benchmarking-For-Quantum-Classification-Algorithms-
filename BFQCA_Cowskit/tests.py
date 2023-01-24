import backend.files as fl
import os
import subprocess

PREDEFINED_ALGORITHMS = ['qgenetic', 'qgenetic_acc', 'qgenetic_prob', 'qvm', 'qcnn', 'qknn']
PREDEFINED_DATASETS = ['iris', 'palmer_penguin', 'pima_indians_diabetic', 'lines']

EXPECTED_FAILURE_PAIRS = [
    ['qvm','iris'],
    ['qcnn','iris'],
    ['qvm','palmer_penguin'],
    ['qcnn','palmer_penguin'],
]

for alg in PREDEFINED_ALGORITHMS:
    for ds in PREDEFINED_DATASETS:
        path = fl.get_file_realpath(__file__)
        command = f"python \"{path}/main.py\" -a {alg} -d {ds}"

        logs_folder = fl.get_logs_folder_path(path, "logs_tests")
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

            test_result = full_output.find("Request body:") != -1
            expected_test_result = [alg, ds] not in EXPECTED_FAILURE_PAIRS

            print(f"{'+' if test_result == expected_test_result else '-'} {alg} + {ds} {'passed' if test_result == True else 'failed'}{', as expected' if expected_test_result == False and test_result == False else ''}")

