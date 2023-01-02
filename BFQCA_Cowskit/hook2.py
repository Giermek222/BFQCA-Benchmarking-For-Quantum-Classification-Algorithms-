import subprocess
import os
import sys

def main():
    with open("hook.txt", "w") as logfile:
        args = sys.argv[1:]
        command = "python hook.py "+" ".join(args)
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