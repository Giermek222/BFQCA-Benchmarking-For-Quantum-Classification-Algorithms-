import cowskit
import argparse
from typing import Tuple

ALGORITHM_CHOICES = ["qknn", "qvm", "qcnn", "custom"]
DATASET_CHOICES = ["Iris", "Palmer Penguin", "Pima Indians Diabetic", "custom"]
ENCODING_CHOICES = ["angle", "amplitude", "binary", "custom"]

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
                prog = 'CowSkit Hook',
                description = 'Launch algorithms and receive benchmark results')

    parser.add_argument('-a','--algorithm', 
                        required=True,
                        choices=ALGORITHM_CHOICES,  
                        help=f"Name of the algorithm to use. Possible values: {ALGORITHM_CHOICES}"
    )
    parser.add_argument('-d','--dataset', 
                        required=True,
                        choices=DATASET_CHOICES,  
                        help=f"Name of the dataset to use. Possible values: {DATASET_CHOICES}"
    )
    parser.add_argument('-e','--encoding', 
                        required=False,
                        choices=ENCODING_CHOICES, 
                        default="amplitude",
                        help=f"Name of the encoding to use. Possible values: {ENCODING_CHOICES}"
    )
    parser.add_argument('-af','--algorithm_file', 
                        default="",
                        help="Name of the file to construct algorithm when 'custom' is selected." \
                            "File must contain a class named exactly like the file, that overrides cowskit.algorithms.Algorithm class"
    )
    parser.add_argument('-df','--dataset_file', 
                        default="",
                        help="Name of the file to generate dataset when 'custom' is selected." \
                            "File must contain a class named exactly like the file, that overrides cowskit.datasets.Dataset class"
    )
    parser.add_argument('-ef','--encoding_file',
                        default="",
                        help="Name of the file to use as the encoding when 'custom' is selected." \
                            "File must contain a class named exactly like the file, that overrides cowskit.encodings.Encoding class"
    )
    parser.add_argument('-t','--tries',
                        default=1,
                        help="Determines how many times algorithm is benchmarked. Default is 1."
    )
    parser.add_argument('-i','--include_all',
                        default=False,
                        help="Determines whether to include dataset loading and encoding in the benchmarking results. Default is False"
    )
    parser.add_argument('-l','--latency_percentile',
                        default=90,
                        help="Latency percentile to report. Default is 90"
    )

    return parser.parse_args()


def parse_dataset(dataset:str, dataset_file:str = "") -> cowskit.datasets.Dataset:
    if dataset == "Iris":
        dataset = cowskit.datasets.IrisDataset("./cowskit_library/cowskit/files/iris.dataset") # cowskit.files.IRIS_DATASET
    elif dataset == "lines":
        dataset = cowskit.datasets.LinesDataset(shape=[3,3], line_len=2)
    elif dataset == "custom":
        name = dataset_file.split(".py")[0]
        file = __import__(name)
        dataset = getattr(file, name)()
    else:
        raise Exception(f"No dataset with name: {dataset}")

    return dataset

def parse_algorithm(algorithm:str, algorithm_file:str = "") -> cowskit.algorithms.Algorithm:
    if algorithm == "qknn":
        algorithm = cowskit.algorithms.KNearestNeighbors(n_neighbors=4)
    elif algorithm == "qvm":
        algorithm = cowskit.models.VariationalModel()
    elif algorithm == "qcnn":
        algorithm = cowskit.models.ConvolutionalModel()
    elif algorithm == "custom":
        name = algorithm_file.split(".py")[0]
        file = __import__(name)
        algorithm = getattr(file, name)()
    else:
        raise Exception(f"No algorithm with name: {algorithm}")

    return algorithm

def parse_encoding(encoding: str, encoding_file: str = "") -> cowskit.encodings.Encoding:
    if encoding == "binary":
        encoding = cowskit.encodings.BinaryEncoding()
    elif encoding == "angle":
        encoding = cowskit.encodings.AngleEncoding()
    elif encoding == "amplitude":
        encoding = cowskit.encodings.AmplitudeEncodingV2(n_features=4)
    elif encoding == "custom":
        name = encoding_file.split(".py")[0]
        file = __import__(name)
        encoding = getattr(file, name)()
    else:
        raise Exception(f"No encoding with name: {encoding}")

    return encoding

def parse_flags(override:bool = False) -> Tuple[argparse.Namespace, cowskit.datasets.Dataset, cowskit.encodings.Encoding, cowskit.algorithms.Algorithm]:
    args = parse_args()

    if override:
        args.dataset = "Iris"
        # args.encoding = "amplitude"
        args.algorithm = "qknn"

    dataset = parse_dataset(args.dataset, args.dataset_file)
    encoding = parse_encoding(args.encoding, args.encoding_file)
    algorithm = parse_algorithm(args.algorithm, args.algorithm_file)

    algorithm.encoding = encoding

    return [args, dataset, encoding, algorithm]