import requests
import cowskit
import argparse
import time
import json

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
                prog = 'CowSkit Hook',
                description = 'Launch algorithms and receive benchmark results')

    parser.add_argument('-a','--algorithm', choices=["qknn", "qvm", "qcnn"])
    parser.add_argument('-d','--dataset', choices=["iris", "lines"])
    parser.add_argument('-e','--encoding', choices=["angle", "amplitude", "binary"])

    return parser.parse_args()


def parse_dataset(dataset:str) -> cowskit.datasets.Dataset:
    if dataset == "iris":
        dataset = cowskit.datasets.IrisDataset("./cowskit_library/cowskit/files/iris.dataset") # cowskit.files.IRIS_DATASET
    elif dataset == "lines":
        dataset = cowskit.datasets.LinesDataset(shape=[3,3], line_len=2)
    else:
        raise Exception(f"No dataset with name: {dataset}")

    return dataset

def parse_algorithm(algorithm:str) -> cowskit.algorithms.Algorithm:
    if algorithm == "qknn":
        algorithm = cowskit.algorithms.KNearestNeighbors(n_neighbors=4)
    elif algorithm == "qvm":
        algorithm = cowskit.models.VariationalModel()
    elif algorithm == "qcnn":
        algorithm = cowskit.models.ConvolutionalModel()
    else:
        raise Exception(f"No algorithm with name: {algorithm}")

    return algorithm

def parse_encoding(encoding: str) -> cowskit.encodings.Encoding:
    if encoding == "binary":
        encoding = cowskit.encodings.BinaryEncoding()
    elif encoding == "angle":
        encoding = cowskit.encodings.AngleEncoding()
    elif encoding == "amplitude":
        encoding = cowskit.encodings.AmplitudeEncodingV2(n_features=4)
    else:
        raise Exception(f"No encoding with name: {encoding}")

    return encoding

def main():
    args = parse_args()

    args.dataset = "iris"
    args.encoding = "amplitude"
    args.algorithm = "qknn"

    dataset = parse_dataset(args.dataset)
    encoding = parse_encoding(args.encoding)
    algorithm = parse_algorithm(args.algorithm)

    algorithm.encoding = encoding

    start = time.time()
    X_train, X_test, y_train, y_test = dataset.load_iris(16,32)

    algorithm.fit(X_train, y_train)
    end = time.time()
    total_time = round(end-start, 2)

    URL = "https://localhost/benchmarks/execute"

    params = [
        {"name": "idk", "value": 123}
    ]

    body = {
        "problem name": "idk",
        "algorithm name": args.algorithm,
        "accuracy learning": 1,
        "accuracy test": algorithm.score(X_test, y_test),
        "loss learning": 0,
        "loss test": 0,
        "max latency": total_time,
        "min latency": total_time,
        "avg latency": total_time,
        "latency percentile": "100",
        "time": total_time
        #"params": params
    }

    BODY = json.dumps(body, indent=4)

    print(BODY)

    try:
        response = requests.post(url = URL, json=BODY)
        print(response)
    except Exception as e:
        print(e.with_traceback())

if __name__ == "__main__":
    main()