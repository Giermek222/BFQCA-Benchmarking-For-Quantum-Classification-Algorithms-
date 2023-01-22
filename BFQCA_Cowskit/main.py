from backend.request import make_request, send_request
from backend.argparser import parse_args, check_debug_mode, construct_instances_from_args
from backend.files import get_logs_folder_path, get_log_file_path, get_file_realpath, add_custom_folders_to_path
from backend.benchmark import debug_dataset_info, train_algorithm, benchmark_training, benchmark_test, benchmark_inference
from backend.commands import construct_debug_launch_command, run_command

from backend.argparser import Namespace
from backend.logger import Log, LogLevel

Log.level = LogLevel.DEBUG

def main(path_to_main_file: str, args: Namespace) -> None:
    add_custom_folders_to_path(path_to_main_file)
    dataset, algorithm = construct_instances_from_args(args)

    debug_dataset_info(dataset)
    benchmark_cache = train_algorithm(dataset, algorithm)
    benchmark_cache = benchmark_training(benchmark_cache, dataset, algorithm)
    benchmark_cache = benchmark_test(benchmark_cache, dataset, algorithm)
    benchmark_cache = benchmark_inference(benchmark_cache,dataset, algorithm, args.tries, args.latency_percentile)

    body = make_request(args, benchmark_cache)
    send_request(body)

    return body

def log(path_to_main_file):
    logs_folder_path = get_logs_folder_path(path_to_main_file)
    logs_file_path = get_log_file_path(logs_folder_path, "main")

    with open(logs_file_path, "w") as log_file:
        command = construct_debug_launch_command(path_to_main_file)
        try:
            run_command(command, log_file)
        except Exception as e:
            Log.error(f"Errors encountered, check {logs_file_path} for details.")
            log_file.write(str(e))

if __name__ == "__main__":
    args = parse_args()
    path_to_main_file = get_file_realpath(__file__)

    if check_debug_mode(args):
        log(path_to_main_file)
    else:
        main(path_to_main_file, args)
