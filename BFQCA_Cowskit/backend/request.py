import requests
import numpy as np
from backend.log import Log

def make_request(args, learn_accuracy, test_accuracy, learn_loss, test_loss, latencies, total_time_ms):
    
    dataset_name = args.dataset,
    algorithm_name = args.algorithm,

    max_latency_ms = np.max(latencies)
    min_latency_ms = np.min(latencies)
    avg_latency_ms = round(np.average(latencies), 2)
    percentile_latency_ms = round(np.percentile(latencies, args.latency_percentile), 2)

    body = {
        "problemName": dataset_name,
        "algorithmName": algorithm_name,
        "accuracyLearning": learn_accuracy,
        "accuracyTest": test_accuracy,
        "lossLearning": learn_loss,
        "lossTest": test_loss,
        "maxLatency": max_latency_ms,
        "minLatency": min_latency_ms,
        "avgLatency": avg_latency_ms,
        "latencyPercentile": percentile_latency_ms,
        "time": total_time_ms
    }

    Log.debug(body)

    return body

def send_request(body) -> None:
    URL = "http://localhost:3001/benchmarks/execute"

    try:
        response = requests.post(url = URL, json=body, verify=False)
        Log.debug(response)
    except Exception as e:
        print(e)