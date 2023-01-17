import time
import numpy as np
from typing import Dict

from cowskit.datasets import Dataset
from cowskit.algorithms import Algorithm
from cowskit.encodings import Encoding

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,  log_loss

from backend.logger import Log


def train_algorithm(benchmark_cache: Dict[str, float], dataset: Dataset, algorithm: Algorithm, encoding: Encoding, include_dataset_loading: bool) -> Dict[str, float]:
    Log.info("Start algorithm training")

    if include_dataset_loading:
        start = time.time()
        X_train, y_train = dataset.get_train_data()
        algorithm.train(X_train, y_train)
        end = time.time()
        training_time_ms = round((end-start)*1000, 2)
    else:
        X_train, y_train = dataset.get_train_data()
        start = time.time()
        algorithm.train(X_train, y_train)
        end = time.time()
        training_time_ms = round((end-start)*1000, 2)

    benchmark_cache['training_time_ms'] = training_time_ms

    Log.info("Training finished, total time (ms): ", training_time_ms)

    return benchmark_cache

def benchmark_training(benchmark_cache: Dict[str, str], dataset: Dataset, algorithm: Algorithm, encoding: Encoding) -> Dict[str, float]:
    Log.info("Computing training benchmarks")

    X_train, y_train = dataset.get_train_data()
    y_pred = algorithm.predict(X_train)

    training_accuracy = accuracy_score(y_train.flatten(), y_pred.flatten())
    training_precision = precision_score(y_train.flatten(), y_pred.flatten())
    training_recall = recall_score(y_train.flatten(), y_pred.flatten())
    training_f1_score = f1_score(y_train.flatten(), y_pred.flatten())
    training_loss = log_loss(y_train.flatten(), y_pred.flatten())

    benchmark_cache['training_accuracy'] = training_accuracy
    benchmark_cache['training_precision'] = training_precision
    benchmark_cache['training_recall'] = training_recall
    benchmark_cache['training_f1_score'] = training_f1_score
    benchmark_cache['training_loss'] = training_loss

    Log.info(f"\tAccuracy: \t{training_accuracy}")
    Log.info(f"\tPrecision: \t{training_precision}")
    Log.info(f"\tRecall: \t{training_recall}")
    Log.info(f"\tF1 score: \t{training_f1_score}")
    Log.info(f"\tLogistic loss: \t{training_loss}")

    return benchmark_cache

def benchmark_test(benchmark_cache: Dict[str, str], dataset: Dataset, algorithm: Algorithm, encoding: Encoding):
    Log.info("Computing training benchmarks")

    start = time.time()
    X_test, y_test = dataset.get_test_data()

    algorithm.fit(X_test, y_test)
    end = time.time()
    
    test_time_ms = round((end-start)*1000, 2)
    test_loss = 1.0
    test_accuracy = algorithm.score(X_test, y_test.flatten())

    Log.info("Testing finished, total time (ms): ", test_time_ms)

    return test_time_ms, test_loss, test_accuracy

def benchmark_inference(dataset: Dataset, algorithm: Algorithm, encoding: Encoding, tries:int, include_dataset_loading: bool):
    Log.info("Start inference benchmarking, tries: ", tries)

    latencies = []
    for _ in range(tries):

        start = time.time()
        X_example, y_example = dataset.get_random_pair()

        if not include_dataset_loading:
            start = time.time()

        algorithm.predict(X_example)
        end = time.time()
        latency_ms = round((end-start)*1000, 2)
        latencies.append(latency_ms)
    
    Log.info("Inference latency benchmarking finished")
    Log.info("Latencies (ms): ", latencies)

    return latencies




def compute_benchmarks(latencies, ):
    max_latency_ms = np.max(latencies)
    min_latency_ms = np.min(latencies)
    avg_latency_ms = round(np.average(latencies), 2)
    percentile_latency_ms = round(np.percentile(latencies, args.latency_percentile), 2)