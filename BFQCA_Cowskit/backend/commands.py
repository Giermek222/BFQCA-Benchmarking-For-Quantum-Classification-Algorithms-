import os
import sys
import subprocess

def construct_debug_launch_command(path_to_main_file: str) -> str:
    args = sys.argv[1:]

    if args.count('-debug'):
        args.remove('-debug')
    if args.count('--debug'):
        args.remove('--debug')

    command = f"python \"{path_to_main_file}/main.py\" {' '.join(args)}"

    return command

def run_command(command: str, log_file) -> None:
    subprocess.run(command,
                    shell=True,
                    check=True,
                    stdout=log_file,
                    stderr=log_file,
                    cwd=os.getcwd(),
                    env=os.environ.copy())