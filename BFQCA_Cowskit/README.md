
# Cowskit Library

A library dedicated for benchmarking of quantum algorithms.




## Deployment

To build & install this library, simply run the following command:

Windows:
```bash
  python make.py
```
Linux/MacOS:
```bash
  python3 make.py
```

The built .whl file will be created inside `cowskit_library/dist` folder.
Install logs can be found inside `logs` folder.
## API Reference

#### Basic usage

```http
  python hook.py [-FLAGS]
```

| Flag      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-h, --help` | `string` | Displays a help message. |
| `-a, --algorithm` | `string` | **Required**. Name of the algorithm to benchmark. |
| `-d, --dataset` | `string` | **Required**. Name of dataset to use in benchmarking. |
| `-e, --encoding` | `string` | **Required**. Name of the encoder to use when costructing the algorithm. |
| `-af, --algorithm_file` | `string` | Name of the file to construct algorithm when 'custom' is selected. |
| `-df, --dataset_file` | `string` | Name of the file to generate dataset when 'custom' is selected. |
| `-ef, --encoding_file` | `string` | Name of the file to use as the encoding when 'custom' is selected. |
| `-t, --tries` | `int` | Determines how many times algorithm is benchmarked. Default is 1. |
| `-i, --include_all` | `bool` | Determines whether to include dataset loading and encoding in the benchmarking results. Default is False. |
| `-l, --latency_percentile` | `int` | Latency percentile to report. Default is 90. |
#### Advanced usage
Hook allows to automatically compute benchmarking results for custom implementations of quantum algorithms.
To do so, set any of the **required** flags to "custom", and provide a file with the code of the algorithm/dataset/encoding.

Requirements:
1. File must contain a class named EXACTLY like the file name. Example: CustomAlgorithm.py has CustomAlgorithm class
2. File must be of .py extension
3. Only a selected amount of external libraries are available. See the list in requirements.py
4. A class inside the file must implement a selected interface from cowskit library. Either cowskit.algorithms.Algorithm, cowskit.datasets.Dataset or cowskit.encodings.Encoding

#### Return value

Returns a Dictionary object:
```http
  {
        "problemName": "name_of_the_problem",
        "algorithmName": "algorithm_name",
        "accuracyLearning": accuracy,
        "accuracyTest": test_accuracy,
        "lossLearning": loss_learning,
        "lossTest": loss_test,
        "maxLatency": max_latency,
        "minLatency": min_latency,
        "avgLatency": avg_latency,
        "latencyPercentile": percentile,
        "time": total_time
    }
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `problemName`      | `string` | Name of the dataset used |
| `algorithmName`      | `string` | Name of the algorithm used |
| `accuracyLearning`      | `float` | Learning accuracy |
| `accuracyTest`      | `float` | Test set accuracy |
| `lossLearning`      | `float` | Learning loss |
| `lossTest`      | `float` | Test set loss |
| `maxLatency`      | `float` | Maximum latency |
| `minLatency`      | `float` | Minimum latency |
| `avgLatency`      | `float` | Average latency |
| `latencyPercentile`      | `float` | Percentile value of latency |
| `time`      | `float` | Benchmarking time (in milliseconds) |










