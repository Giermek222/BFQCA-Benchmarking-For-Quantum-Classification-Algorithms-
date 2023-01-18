import cowskit
import argparse
from argparse import Namespace, ArgumentParser
from typing import Tuple

from backend.logger import Log

PREDEFINED_ALGORITHMS = ['qknn', 'qvm', 'qcnn', 'qgenetic']
PREDEFINED_DATASETS = ['iris', 'palmer_penguin', 'pima_indians_diabetic', 'lines']
PREDEFINED_ENCODINGS = ['angle', 'amplitude', 'binary']

def parse_args() -> Namespace:
    parser = ArgumentParser(
                prog = 'Cowskit Benchmark App',
                description = 'Launch algorithms, receive benchmark results')

    parser.add_argument('-a', '--algorithm', 
                        required = True, 
                        help = f'Name of the predefined/custom algorithm to use. Predefined values: {PREDEFINED_ALGORITHMS}'
    )
    parser.add_argument('-d', '--dataset', 
                        required = True,
                        help = f'Name of the predefined/custom dataset to use. Predefined values: {PREDEFINED_DATASETS}'
    )
    parser.add_argument('-e', '--encoding', 
                        required = True,
                        help = f'Name of the predefined/custom encoding to use. Predefined values: {PREDEFINED_ENCODINGS}'
    )
    parser.add_argument('-t', '--tries',
                        default = 10,
                        help = 'Determines how many times algorithm is benchmarked. Default: 10.'
    )
    parser.add_argument('-l', '--latency_percentile',
                        default = 95,
                        help = 'Latency percentile to report. Default: 90'
    )
    parser.add_argument('-i', '--include_dataset_loading',
                        action = 'store_true',
                        help = 'Determines whether to include dataset loading and encoding in the benchmarking results. Default: False'
    )
    parser.add_argument('-debug', '--debug',
                        action = 'store_true',
                        help = 'Turns on logs collection'
    )

    return parser.parse_args()


def parse_dataset(dataset_name: str) -> cowskit.datasets.Dataset:
    dataset_name = dataset_name.lower()

    if dataset_name == 'iris':
        dataset = cowskit.datasets.IrisDataset()
    elif dataset_name == 'lines':
        dataset = cowskit.datasets.LinesDataset()
    elif dataset_name == 'palmer_penguin':
        dataset = cowskit.datasets.PalmerPenguinDataset()
    elif dataset_name == 'pima_indians_diabetic':
        dataset = cowskit.datasets.DiabetesDataset()
    else:
        try:
            file = __import__(dataset_name)
            dataset = getattr(file, dataset_name)()
        except Exception as e:
            Log.error(f'No dataset with name: {dataset_name}')
            raise e

    Log.info("Loaded dataset: ", dataset_name)

    return dataset

def parse_algorithm(algorithm_name: str) -> cowskit.algorithms.Algorithm:
    algorithm_name = algorithm_name.lower()

    if algorithm_name == 'qknn':
        algorithm = cowskit.algorithms.KNearestNeighbors()
    elif algorithm_name == 'qgenetic':
        algorithm = cowskit.algorithms.GeneticAlgorithm()
    elif algorithm_name == 'qvm':
        algorithm = cowskit.models.VariationalModel()
    elif algorithm_name == 'qcnn':
        algorithm = cowskit.models.ConvolutionalModelV2()
    else:
        try:
            file = __import__(algorithm_name)
            algorithm = getattr(file, algorithm_name)()
        except Exception as e:
            Log.error(f'No algorithm with name: {algorithm_name}')
            raise e

    Log.info("Loaded algorithm: ", algorithm_name)

    return algorithm

def parse_encoding(encoding_name: str) -> cowskit.encodings.Encoding:
    encoding_name = encoding_name.lower()

    if encoding_name == 'binary':
        encoding = cowskit.encodings.BinaryEncoding()
    elif encoding_name == 'angle':
        encoding = cowskit.encodings.AngleEncoding()
    elif encoding_name == 'amplitude':
        encoding = cowskit.encodings.AmplitudeEncodingV2()
    else:
        try:
            file = __import__(encoding_name)
            encoding = getattr(file, encoding_name)()
        except Exception as e:
            Log.error(f'No encoding with name: {encoding_name}')
            raise e

    Log.info("Loaded encoding: ", encoding_name)

    return encoding

def construct_instances_from_args(args: Namespace) -> Tuple[cowskit.datasets.Dataset, cowskit.encodings.Encoding, cowskit.algorithms.Algorithm]:

    dataset = parse_dataset(args.dataset)
    algorithm = parse_algorithm(args.algorithm)
    encoding = parse_encoding(args.encoding)

    # To be removed
    if isinstance(algorithm, cowskit.algorithms.KNearestNeighbors):
        features_amount = cowskit.utils.get_shape_size(dataset.get_random_pair()[0])
        Log.info(f"Features amount: {features_amount}")
        encoding.__init__(n_features = features_amount)
        algorithm.__init__(n_neighbors = features_amount)
        algorithm.encoding = encoding
    # ===

    return dataset, algorithm, encoding 

def check_debug_mode(args: Namespace) -> bool:
    return True if args.debug else False

