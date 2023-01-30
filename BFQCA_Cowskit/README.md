
# Cowskit Library & Benchmarking

Benchmarking of quantum classification algorithms. Created with a custom library for quick quantum algorithm prototyping.

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

The built .whl file will be created inside `library/dist` folder.
Install logs can be found inside `logs` folder.
## API Reference

#### Basic usage

```http
  python main.py [-FLAGS]
```

| Flag      | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-h, --help` | `string` | Displays a help message. |
| `-a, --algorithm` | `string` | **Required**. Name of the algorithm to benchmark. |
| `-d, --dataset` | `string` | **Required**. Name of dataset to use in benchmarking. |
| `-t, --tries` | `int` | Determines how many times algorithm is benchmarked. Default is 10. |
| `-debug, --debug` | None | When present, instead of printing output to the console, whole output is collected to the logs/main.txt file. |
| `-s, --size` | `int` | If noisy dataset is used, determines the amount of data generated. |
| `-is, --input_shape` | `int` | If noisy dataset is used, determines its 2nd dimension. Generator input shape used will become [size, input_shape]. |
| `-os, --output_shape` | `int` | If noisy dataset is used, determines its 2nd dimension. 1 creates -1/1 distribution for binary classification. Generator output shape used will become [size, output_shape].  |
#### Advanced usage
Hook allows to automatically compute benchmarking results for custom implementations of quantum algorithms.
To do so, set any of the **required** flags to the name (without the extension_ of the file to execute (located inside custom_algorithms/custom_datasets folder).

Requirements:
1. File must contain a class named EXACTLY like the file name. Example: CustomAlgorithm.py has the implementation CustomAlgorithm class
2. File must be of .py extension
3. Only a selected amount of external libraries are available. See the list in requirements.py
4. A class inside the file must implement a selected interface from cowskit library. Either cowskit.algorithms.Algorithm or cowskit.datasets.Dataset
5. A class must override all marked methods (otherwise the class will raise an exception)

#### Return value

Returns a Dictionary object (example output):
```http
  {
    'problem_name': lines
    'algorithm_name': qgenetic
    'training_accuracy': 0.7375
    'training_precision': 0.6838
    'training_recall': 0.7061
    'training_f1_score': 0.6948
    'training_loss': 60.4429
    'test_accuracy': 0.6
    'test_precision': 0.6458
    'test_recall': 0.6667
    'test_f1_score': 0.6561
    'test_loss': 92.1034
    'max_latency_ms': 0.0
    'min_latency_ms': 0.0
    'avg_latency_ms': 0.0
    'percentile_latency_ms': 0.0
    'time': 32.44
  }
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `problem_name`      | `string` | Name of the dataset used |
| `algorithm_name`      | `string` | Name of the algorithm used |
| `training_accuracy`      | `float` | Training data accuracy |
| `training_precision`      | `float` | Training data precision |
| `training_recall`      | `float` | Training data recall |
| `training_f1_score`      | `float` | Training data F1 score |
| `training_loss`      | `float` | Training data loss. Categorical Crossentropy for multi-class dataset, Binary Crossentropy for binary classification |
| `test_accuracy`      | `float` | Test data accuracy |
| `test_precision`      | `float` | Test data precision |
| `test_recall`      | `float` | Test data recall |
| `test_f1_score`      | `float` | Test data F1 score |
| `test_loss`      | `float` | Test data loss. Categorical Crossentropy for multi-class dataset, Binary Crossentropy for binary classification |
| `max_latency_ms`      | `float` | Maximum latency |
| `min_latency_ms`      | `float` | Minimum latency |
| `avg_latency_ms`      | `float` | Average latency |
| `percentile_latency_ms`      | `float` | Percentile value of latency |
| `time`      | `float` | Benchmarking time (in seconds, contrary to latency) |


#### Tests

To test the pre-built algoithms, run the following command:

Windows:
```bash
  python tests.py
```
Linux/MacOS:
```bash
  python3 tests.py
```

This script will launch every combination of pre-built algorithm and dataset. All logs will be stored into `logs_tests` directory. Console output shows the pass/failure of a given combination.





