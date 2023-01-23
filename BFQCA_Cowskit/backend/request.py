import requests
import numpy as np
from typing import Dict
from backend.logger import Log

def make_request(args, benchmark_cache: Dict[str, float]):
    dataset_name = args.dataset
    algorithm_name = args.algorithm

    Log.debug("Benchmarking cache:")
    for key,value in benchmark_cache.items():
        Log.debug(f" '{key}': {value}")

    body = {
        "problem_name": dataset_name,
        "algorithm_name": algorithm_name,
        "training_accuracy": benchmark_cache["training_accuracy"],
        "training_precision": benchmark_cache["training_precision"],
        "training_recall": benchmark_cache["training_recall"],
        "training_f1_score": benchmark_cache["training_f1_score"],
        "training_loss": benchmark_cache["training_loss"],
        "test_accuracy": benchmark_cache["test_accuracy"],
        "test_precision": benchmark_cache["test_precision"],
        "test_recall": benchmark_cache["test_recall"],
        "test_f1_score": benchmark_cache["test_f1_score"],
        "test_loss": benchmark_cache["test_loss"],
        "maxLatency": benchmark_cache["max_latency_ms"],
        "minLatency": benchmark_cache["min_latency_ms"],
        "avgLatency": benchmark_cache["avg_latency_ms"],
        "latencyPercentile": benchmark_cache["percentile_latency_ms"],
        "time": benchmark_cache["training_time_ms"]
    }

    Log.debug("Request body:")
    for key,value in body.items():
        Log.debug(f" '{key}': {value}")

    return body

def send_request(body) -> None:
    URL = "http://localhost:3001/benchmarks/execute"

    try:
        response = requests.post(url = URL, json=body, verify=False)
        Log.debug(response)
    except Exception as e:
        Log.error(e)