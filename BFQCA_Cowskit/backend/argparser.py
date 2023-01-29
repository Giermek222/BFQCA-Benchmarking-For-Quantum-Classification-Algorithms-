import cowskit
from argparse import Namespace, ArgumentParser
from typing import Tuple

from backend.logger import Log

PREDEFINED_ALGORITHMS = ['qgenetic', 'qgenetic_acc', 'qgenetic_prob', 'qvm', 'qcnn', 'qknn', 'noise']
PREDEFINED_DATASETS = ['iris', 'palmer_penguin', 'pima_indians_diabetic', 'lines']

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
    parser.add_argument('-t', '--tries',
                        default = 10,
                        type=int,
                        help = 'Determines how many times algorithm is benchmarked. Default: 10.'
    )
    parser.add_argument('-l', '--latency_percentile',
                        default = 95,
                        type=int,
                        help = 'Latency percentile to report. Default: 90'
    )
    parser.add_argument('-debug', '--debug',
                        action = 'store_true',
                        help = 'Turns on logs collection'
    )
    parser.add_argument('-s', '--size',
                        default=10,
                        type=int,
                        help='If noisy dataset is used, determines the amount of data generated')
    parser.add_argument('-is', '--input_shape',
                        default=2,
                        type=int,
                        help='If noisy dataset is used, determines its 2nd dimension')
    parser.add_argument('-os', '--output_shape',
                        default=1,
                        type=int,
                        help='If noisy dataset is used, determines its 2nd dimension. 1 creates -1/1 distribution for binary classification')

    return parser.parse_args()


def parse_dataset(dataset_name: str, amount, input_shape, output_shape) -> cowskit.datasets.Dataset:
    dataset_name = dataset_name.lower()

    if dataset_name == 'iris':
        dataset = cowskit.datasets.IrisDataset()
    elif dataset_name == 'lines':
        dataset = cowskit.datasets.LinesDataset()
    elif dataset_name == 'palmer_penguin':
        dataset = cowskit.datasets.PalmerPenguinDataset()
    elif dataset_name == 'pima_indians_diabetic':
        dataset = cowskit.datasets.DiabetesDataset()
    elif dataset_name == 'noisy':
        dataset = cowskit.datasets.NoisyDataset(amount, input_shape, output_shape)
    else:
        try:
            file = __import__(dataset_name)
            dataset = getattr(file, dataset_name)()
        except Exception as e:
            Log.error(f'No dataset with name: {dataset_name}')
            raise e

    Log.info("Loaded dataset: ", dataset_name)

    return dataset

def parse_algorithm(algorithm_name: str, dataset: cowskit.datasets.Dataset) -> cowskit.algorithms.Algorithm:
    algorithm_name = algorithm_name.lower()

    if algorithm_name == 'qknn':
        algorithm = cowskit.algorithms.KNearestNeighbors(dataset)
    elif algorithm_name == 'qgenetic':
        algorithm = cowskit.algorithms.GeneticAlgorithm(dataset)
    elif algorithm_name == 'qgenetic_acc':
        algorithm = cowskit.algorithms.AccuracyGeneticAlgorithm(dataset)
    elif algorithm_name == 'qgenetic_prob':
        algorithm = cowskit.algorithms.ProbabilityGeneticAlgorithm(dataset)
    elif algorithm_name == 'qvm':
        algorithm = cowskit.models.VariationalModel(dataset)
    elif algorithm_name == 'qcnn':
        algorithm = cowskit.models.ConvolutionalModel(dataset)
    else:
        try:
            file = __import__(algorithm_name)
            algorithm = getattr(file, algorithm_name)(dataset)
        except Exception as e:
            Log.error(f'No algorithm with name: {algorithm_name}')
            raise e

    Log.info("Loaded algorithm: ", algorithm_name)

    return algorithm

def construct_instances_from_args(args: Namespace) -> Tuple[cowskit.datasets.Dataset, cowskit.algorithms.Algorithm]:

    dataset = parse_dataset(args.dataset, args.size, args.input_shape, args.output_shape)
    algorithm = parse_algorithm(args.algorithm, dataset)

    return dataset, algorithm

def check_debug_mode(args: Namespace) -> bool:
    return True if args.debug else False

