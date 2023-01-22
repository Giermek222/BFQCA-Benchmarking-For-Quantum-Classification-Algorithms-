import time
import numpy as np
from typing import Dict

from cowskit.datasets import Dataset
from cowskit.algorithms import Algorithm
from cowskit.utils import compute_accuracy, compute_precision, compute_recall, compute_f1_score, compute_crossentropy_loss

from backend.logger import Log

def debug_dataset_info(dataset: Dataset) -> None:
    train_len = dataset.get_train_data()[0].shape[0]
    test_len = dataset.get_test_data()[0].shape[0]
    X,Y = dataset.get_random_pair()

    Log.debug("Dataset info:")
    Log.debug(f"Total entries: {dataset.data.shape[0]} ({train_len} for training, {test_len} for testing)")
    Log.debug(f"Input shape: {dataset.get_input_size()} ({dataset.input_size} + {dataset.input_padding_amount} padding)")
    Log.debug(f"Output shape: {dataset.get_output_size()} ({dataset.output_size} + {dataset.output_padding_amount} padding)")
    Log.debug(f"Example pair:")
    Log.debug(f"X:")
    Log.debug(np.array2string(X, prefix=Log.debug_prefix))
    Log.debug(f"Y:")
    Log.debug(np.array2string(Y, prefix=Log.debug_prefix))


def train_algorithm(dataset: Dataset, algorithm: Algorithm) -> Dict[str, float]:
    Log.info("Start algorithm training")

    X_train, y_train = dataset.get_train_data()
    start = time.time()
    algorithm.train_safe(X_train, y_train)
    end = time.time()
    training_time_ms = round((end-start)*1000, 2)

    benchmark_cache: Dict[str, float] = {}
    benchmark_cache['training_time_ms'] = training_time_ms

    Log.info("Training finished, total time (ms): ", training_time_ms)

    return benchmark_cache

def benchmark_training(benchmark_cache: Dict[str, str], dataset: Dataset, algorithm: Algorithm) -> Dict[str, float]:
    Log.info("Computing training benchmarks")

    output_padding = dataset.output_padding_amount
    X_train, y_train = dataset.get_train_data()
    y_pred = algorithm.predict_safe(X_train, y_train.shape[1])

    training_accuracy = compute_accuracy(y_train, y_pred, output_padding)
    training_precision = compute_precision(y_train, y_pred, output_padding)
    training_recall = compute_recall(y_train, y_pred, output_padding)
    training_f1_score = compute_f1_score(y_train, y_pred, output_padding)
    training_loss = compute_crossentropy_loss(y_train, y_pred)

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

def benchmark_test(benchmark_cache: Dict[str, float], dataset: Dataset, algorithm: Algorithm) -> Dict[str, float]:
    Log.info("Computing test benchmarks")

    output_padding = dataset.output_padding_amount
    X_test, y_test = dataset.get_test_data()
    y_pred = algorithm.predict_safe(X_test, y_test.shape[1])

    test_accuracy = compute_accuracy(y_test, y_pred, output_padding)
    test_precision = compute_precision(y_test, y_pred, output_padding)
    test_recall = compute_recall(y_test, y_pred, output_padding)
    test_f1_score = compute_f1_score(y_test, y_pred, output_padding)
    test_loss = compute_crossentropy_loss(y_test, y_pred)

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

def benchmark_inference(benchmark_cache: Dict[str, float], dataset: Dataset, algorithm: Algorithm, tries:int, latency_percentile:float) -> Dict[str, float]:
    Log.info("Start inference benchmarking, tries: ", tries)

    latencies = []
    for _ in range(tries):
        X_example, y_example = dataset.get_random_pair()
        start = time.time()
        algorithm.predict_safe(X_example, y_example.shape[1])
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
