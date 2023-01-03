import cowskit
import argparse
import sys
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
                        default=10,
                        help="Determines how many times algorithm is benchmarked. Default is 10."
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


def parse_dataset(dataset_name:str, dataset_file:str = "", path:str = "./") -> Tuple[cowskit.datasets.Dataset, str]:
    if dataset_name == "Iris":
        dataset = cowskit.datasets.IrisDataset(path + "cowskit_library/cowskit/files/iris.dataset") # cowskit.files.IRIS_DATASET
    elif dataset_name == "lines":
        dataset = cowskit.datasets.LinesDataset(shape=[3,3], line_len=2)
    elif dataset_name == "custom":
        dataset_name = dataset_file.split(".py")[0]
        file = __import__(dataset_name)
        dataset = getattr(file, dataset_name)()
    else:
        raise Exception(f"No dataset with name: {dataset_name}")

    return dataset, dataset_name

def parse_algorithm(algorithm_name:str, algorithm_file:str = "") -> Tuple[cowskit.algorithms.Algorithm, str]:
    if algorithm_name == "qknn":
        algorithm = cowskit.algorithms.KNearestNeighbors(n_neighbors=4)
    elif algorithm_name == "qvm":
        algorithm = cowskit.models.VariationalModel()
    elif algorithm_name == "qcnn":
        algorithm = cowskit.models.ConvolutionalModel()
    elif algorithm_name == "custom":
        algorithm_name = algorithm_file.split(".py")[0]
        file = __import__(algorithm_name)
        algorithm = getattr(file, algorithm_name)()
    else:
        raise Exception(f"No algorithm with name: {algorithm_name}")

    return algorithm, algorithm_name

def parse_encoding(encoding_name: str, encoding_file: str = "") -> Tuple[cowskit.encodings.Encoding, str]:
    if encoding_name == "binary":
        encoding = cowskit.encodings.BinaryEncoding()
    elif encoding_name == "angle":
        encoding = cowskit.encodings.AngleEncoding()
    elif encoding_name == "amplitude":
        encoding = cowskit.encodings.AmplitudeEncodingV2(n_features=4)
    elif encoding_name == "custom":
        encoding_name = encoding_file.split(".py")[0]
        file = __import__(encoding_name)
        encoding = getattr(file, encoding_name)()
    else:
        raise Exception(f"No encoding with name: {encoding_name}")

    return encoding, encoding_name

def parse_flags(hook_path: str = "", override:bool = False) -> Tuple[argparse.Namespace, cowskit.datasets.Dataset, cowskit.encodings.Encoding, cowskit.algorithms.Algorithm]:
    args = parse_args()

    sys.path.append(hook_path+"custom_algorithms")
    sys.path.append(hook_path+"custom_encodings")
    sys.path.append(hook_path+"custom_datasets")

    if override:
        args.dataset = "Iris"
        args.encoding = "amplitude"
        args.algorithm = "qknn"

    dataset, args.dataset = parse_dataset(args.dataset, args.dataset_file, hook_path)
    encoding, args.encoding = parse_encoding(args.encoding, args.encoding_file)
    algorithm, args.algorithm = parse_algorithm(args.algorithm, args.algorithm_file)

    algorithm.encoding = encoding

    return args, dataset, encoding, algorithm