import time
import numpy as np
from typing import Dict

from cowskit.datasets import Dataset
from cowskit.algorithms import Algorithm
from cowskit.encodings import Encoding
from cowskit.utils import compute_accuracy, compute_precision, compute_recall, compute_f1_score,  compute_categorical_crossentropy_loss

from backend.logger import Log


def train_algorithm(dataset: Dataset, algorithm: Algorithm, encoding: Encoding) -> Dict[str, float]:
    Log.info("Start algorithm training")

    X_train, y_train = dataset.get_train_data()
    start = time.time()
    algorithm.train(X_train, y_train)
    end = time.time()
    training_time_ms = round((end-start)*1000, 2)

    benchmark_cache: Dict[str, float] = {}
    benchmark_cache['training_time_ms'] = training_time_ms

    Log.info("Training finished, total time (ms): ", training_time_ms)

    return benchmark_cache

def benchmark_training(benchmark_cache: Dict[str, str], dataset: Dataset, algorithm: Algorithm, encoding: Encoding) -> Dict[str, float]:
    Log.info("Computing training benchmarks")

    X_train, y_train = dataset.get_train_data()
    Log.info(f"Training data amount: {X_train.shape[0]}")
    y_pred = algorithm.predict(X_train)

    training_accuracy = compute_accuracy(y_train, y_pred)
    training_precision = compute_precision(y_train, y_pred)
    training_recall = compute_recall(y_train, y_pred)
    training_f1_score = compute_f1_score(y_train, y_pred)
    training_loss = compute_categorical_crossentropy_loss(y_train, y_pred)

    benchmark_cache['training_accuracy'] = training_accuracy
    benchmark_cache['training_precision'] = training_precision
    benchmark_cache['training_recall'] = training_recall
    benchmark_cache['training_f1_score'] = training_f1_score
    benchmark_cache['training_loss'] = training_loss

    Log.info(f"  Accuracy:            {training_accuracy}")
    Log.info(f"  Precision:           {training_precision}")
    Log.info(f"  Recall:              {training_recall}")
    Log.info(f"  F1 score:            {training_f1_score}")
    Log.info(f"  Logistic loss:       {training_loss}")

    return benchmark_cache

def benchmark_test(benchmark_cache: Dict[str, float], dataset: Dataset, algorithm: Algorithm, encoding: Encoding) -> Dict[str, float]:
    Log.info("Computing test benchmarks")

    X_test, y_test = dataset.get_test_data()
    Log.info(f"Testing data amount: {X_test.shape[0]}")
    y_pred = algorithm.predict(X_test)
    
    test_accuracy = compute_accuracy(y_test, y_pred)
    test_precision = compute_precision(y_test, y_pred)
    test_recall = compute_recall(y_test, y_pred)
    test_f1_score = compute_f1_score(y_test, y_pred)
    test_loss = compute_categorical_crossentropy_loss(y_test, y_pred)

    benchmark_cache['test_accuracy'] = test_accuracy
    benchmark_cache['test_precision'] = test_precision
    benchmark_cache['test_recall'] = test_recall
    benchmark_cache['test_f1_score'] = test_f1_score
    benchmark_cache['test_loss'] = test_loss

    Log.info(f"  Accuracy:            {test_accuracy}")
    Log.info(f"  Precision:           {test_precision}")
    Log.info(f"  Recall:              {test_recall}")
    Log.info(f"  F1 score:            {test_f1_score}")
    Log.info(f"  Logistic loss:       {test_loss}")

    return benchmark_cache

def benchmark_inference(benchmark_cache: Dict[str, float], dataset: Dataset, algorithm: Algorithm, encoding: Encoding, tries:int, latency_percentile:float) -> Dict[str, float]:
    Log.info("Start inference benchmarking, tries: ", tries)

    latencies = []
    for _ in range(tries):
        X_example, _ = dataset.get_random_pair()
        start = time.time()
        algorithm.predict(X_example)
        end = time.time()
        latency_ms = round((end-start)*1000, 2)
        latencies.append(latency_ms)
    
    max_latency_ms = np.max(latencies)
    min_latency_ms = np.min(latencies)
    avg_latency_ms = round(np.average(latencies), 2)
    percentile_latency_ms = round(np.percentile(latencies, latency_percentile), 2)

    benchmark_cache['max_latency_ms'] = max_latency_ms
    benchmark_cache['min_latency_ms'] = min_latency_ms
    benchmark_cache['avg_latency_ms'] = avg_latency_ms
    benchmark_cache['percentile_latency_ms'] = percentile_latency_ms

    Log.info("Inference latency benchmarking finished")
    Log.info(f"  Latencies:           {latencies}")
    Log.info(f"  Max latency:         {max_latency_ms}")
    Log.info(f"  Min latency:         {min_latency_ms}")
    Log.info(f"  Avg latency:         {avg_latency_ms}")
    Log.info(f"  Percentile latency:  {percentile_latency_ms}")

    return benchmark_cache
