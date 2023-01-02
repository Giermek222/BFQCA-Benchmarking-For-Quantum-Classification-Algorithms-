import requests


def make_request(dataset_name, algorithm_name, learn_accuracy, test_accuracy, learn_loss, test_loss, max_latency, min_latency, avg_latency, percentile, total_time):

    params = [
        {"name": "idk", "value": 123}
    ]

    body = {
        "problemName": dataset_name,
        "algorithmName": algorithm_name,
        "accuracyLearning": learn_accuracy,
        "accuracyTest": test_accuracy,
        "lossLearning": learn_loss,
        "lossTest": test_loss,
        "maxLatency": max_latency,
        "minLatency": min_latency,
        "avgLatency": avg_latency,
        "latencyPercentile": percentile,
        "time": total_time
    }

    print(body)

    return body

def send_request(body) -> None:
    URL = "http://localhost:3001/benchmarks/execute"

    try:
        response = requests.post(url = URL, json=body, verify=False)
        print(response)
    except Exception as e:
        print(e)