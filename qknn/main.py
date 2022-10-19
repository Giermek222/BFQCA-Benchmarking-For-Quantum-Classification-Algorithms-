from Quantum_knn.QKNN_Classifier import QKNeighborsClassifier
from Encoding.Amplitude_encoding import Amplitude_Encoding
from qiskit import BasicAer
from qiskit.utils import QuantumInstance, algorithm_globals

from Data.iris_data import load_iris

seed = 42
algorithm_globals.random_seed = seed

train_size = 32
test_size = 16
n_features = 4  # all features

# Use iris data set for training and test data
X_train, X_test, y_train, y_test = load_iris(train_size, test_size, n_features)

quantum_instance = QuantumInstance(BasicAer.get_backend('qasm_simulator'),
                                   shots=1024,
                                   optimization_level=1,
                                   seed_simulator=seed,
                                   seed_transpiler=seed)

encoding_map = Amplitude_Encoding(n_features=n_features)

qknn = QKNeighborsClassifier(
    n_neighbors=3,
    quantum_instance=quantum_instance,
    encoding_map=encoding_map
)

qknn.fit(X_train, y_train)
print(f"real labels are      {y_test}")
print(f"Testing accuracy: "
      f"{qknn.score(X_test, y_test):0.2f}")
