import requests


def make_request(problem_name, algorithm_name, learn_accuracy, test_accuracy, learn_loss, test_loss, max_latency, min_latency, avg_latency, percentile, total_time):

    params = [
        {"name": "idk", "value": 123}
    ]

    body = {
        "problem name": problem_name,
        "algorithm name": algorithm_name,
        "accuracy learning": learn_accuracy,
        "accuracy test": test_accuracy,
        "loss learning": learn_loss,
        "loss test": test_loss,
        "max latency": max_latency,
        "min latency": min_latency,
        "avg latency": avg_latency,
        "latency percentile": percentile,
        "time": total_time
    }

    print(body)

    return body

def send_request(body) -> None:
    URL = "https://localhost/benchmarks/execute"

    try:
        response = requests.post(url = URL, json=body)
        print(response)
    except Exception as e:
        print(e)