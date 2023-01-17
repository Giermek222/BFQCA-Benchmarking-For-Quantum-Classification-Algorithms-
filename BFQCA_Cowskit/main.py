from backend.request import make_request, send_request
from backend.argparser import parse_args, check_debug_mode, construct_instances_from_args, Namespace
from backend.files import get_logs_folder_path, get_log_file_path, get_file_realpath, add_custom_folders_to_path
from backend.benchmark import benchmark_training, benchmark_test, benchmark_inference
from backend.commands import construct_debug_launch_command, run_command
from backend.log import Log, LogLevel

Log.level = LogLevel.DEBUG

def main(path_to_main_file: str, args: Namespace) -> None:
    
    add_custom_folders_to_path(path_to_main_file)
    dataset, algorithm, encoding = construct_instances_from_args(args)

    training_time_ms, training_loss, training_accuracy = benchmark_training(dataset, algorithm, encoding, args.include_dataset_loading)
    test_time_ms, test_loss, test_accuracy = benchmark_test(dataset, algorithm, encoding, args.include_dataset_loading)
    latencies = benchmark_inference(dataset, algorithm, encoding, args.tries, args.include_dataset_loading)

    body = make_request(
        args,
        training_accuracy,
        test_accuracy,
        training_loss,
        test_loss,
        latencies,
        training_time_ms
    )

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
