import subprocess
import os
import sys

def main():
    with open("../logs/hook.txt", "w") as logfile:
        args = sys.argv[1:]
        command = "python D:\Wladek\\repos\\\inzynierka\\BFQCA-Benchmarking-For-Quantum-Classification-Algorithms-\\BFQCA_Cowskit\\hook.py "+" ".join(args)
        print(command)
        subprocess.run(command,
                        shell=True,
                        check=True,
                        stdout=logfile,
                        stderr=logfile,
                        cwd=os.getcwd(),
                        env=os.environ.copy())

if __name__ == "__main__":
    main()