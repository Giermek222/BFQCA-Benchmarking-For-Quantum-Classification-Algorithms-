import numpy as np
import math
from cowskit.constants import ROUND_DIGITS, MAX_QUBITS

def get_shape_size(data:np.ndarray) -> int:
    if len(data.shape) == 1:
        return 1
    features_shape = data.shape[1:]
    return np.prod(features_shape)

def compute_possibilities(n_classes: int) -> np.ndarray:
    if n_classes != 1:
        possiblities = np.eye(n_classes)
    else:
        possiblities = np.array([[-1], [1]])
    return possiblities


def sign(x: np.ndarray) -> np.ndarray:
    x[x==0] = 1
    return np.round(x / np.abs(x), 0)

def relu(x: np.ndarray) -> np.ndarray:
    return np.round((x > 0) * x, ROUND_DIGITS)

def tanh(x: np.ndarray) -> np.ndarray:
    return np.round(np.tanh(x), ROUND_DIGITS)

def sigmoid(x: np.ndarray) -> np.ndarray:
    return np.round(1 / (1 + np.exp(-x)), ROUND_DIGITS)

def softmax(x: np.ndarray) -> np.ndarray:
    return np.round((np.exp(x)/np.exp(x).sum(axis=1, keepdims = True)), ROUND_DIGITS)

def one_hot(x: np.ndarray) -> np.ndarray:
    return (x == x.max(axis=1)[:,None]).astype(int)

def fast_binary_accuracy(Y_labels:np.ndarray, Y_pred:np.ndarray):
    Y_labels_copy, Y_pred_copy = Y_labels.flatten(), Y_pred.flatten()
    N = Y_labels_copy.shape[0]
    return np.round(1/N*(Y_labels_copy == Y_pred_copy).sum(), ROUND_DIGITS)

def fast_categorical_accuracy(Y_labels:np.ndarray, Y_pred:np.ndarray):
    N = Y_labels.shape[0]
    return np.round(1/N*np.all(Y_labels==Y_pred, axis=1).sum(), ROUND_DIGITS)

def compute_confusion_matrix(Y_labels:np.ndarray, Y_pred:np.ndarray):           
    """                             truths
    \\ tr tr tr                     x y z
    la                             x
    la                     labels  y
    la                             z
    
    """
    n_classes = get_shape_size(Y_labels)

    if n_classes == 1:
        result = np.zeros((2,2))
        Y_pred_copy = sign(Y_pred.copy())
    else:
        result = np.zeros((n_classes, n_classes))
        Y_pred_copy = one_hot(Y_pred.copy())

    possibilities = compute_possibilities(n_classes)

    for x_idx, x_axis_possibility in enumerate(possibilities):
        for y_idx, y_axis_possibility in enumerate(possibilities):
            x = np.all(Y_labels==y_axis_possibility, axis=1)
            y = np.all(Y_pred_copy==x_axis_possibility, axis=1)
            result[y_idx][x_idx] = (x & y).sum()

    return result
    
def compute_accuracy(confusion_matrix: np.ndarray) -> float:
    dim = confusion_matrix.shape[0]
    
    TPTN = (confusion_matrix * np.eye(dim)).sum()
    accuracy = TPTN / confusion_matrix.sum()
    
    return np.round(accuracy, ROUND_DIGITS)

def compute_precision(confusion_matrix: np.ndarray) -> float:
    dim = confusion_matrix.shape[0]

    sum_columns = np.sum(confusion_matrix, axis = 1)
    precision = 0
    for i in range(dim):
        TP = confusion_matrix[i][i]
        TPFP = sum_columns[i]
        if TPFP == 0: TPFP = 1
        precision += TP / TPFP
    precision /= dim
    return np.round(precision, ROUND_DIGITS)

def compute_recall(confusion_matrix: np.ndarray) -> float:
    dim = confusion_matrix.shape[0]

    sum_columns = np.sum(confusion_matrix, axis = 0)
    recall = 0
    for i in range(dim):
        TP = confusion_matrix[i][i]
        TPFN = sum_columns[i]
        if TPFN == 0: TPFN = 1
        recall += TP / TPFN
    recall /= dim
    return np.round(recall, ROUND_DIGITS)

def compute_f1_score(confusion_matrix: np.ndarray) -> float:
    precision = compute_precision(confusion_matrix)
    recall = compute_recall(confusion_matrix)
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2*precision*recall/(precision+recall)

    return np.round(f1_score, ROUND_DIGITS)

def compute_binary_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.flatten(), Y_pred.flatten()
    Y_labels_copy, Y_pred_copy = (Y_labels_copy + 1)/2,(Y_pred_copy + 1)/2

    N = Y_labels_copy.shape[0]
    binary_crossentropy = -1/N * np.sum(Y_labels_copy * np.log(Y_pred_copy + 10**-100) + (1 - Y_labels_copy) * np.log(1 - Y_pred_copy + 10**-100))

    return np.round(binary_crossentropy, ROUND_DIGITS)
    
def compute_categorical_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()
    N = Y_labels_copy.shape[0]
    categorical_crossentropy = -1/N*np.sum(Y_labels_copy * np.log(Y_pred_copy + 10**-100))

    return np.round(categorical_crossentropy, ROUND_DIGITS)

def compute_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray) -> float:
    if len(Y_labels.shape) == 1 or Y_labels.shape[1] == 1:
        return compute_binary_crossentropy_loss(Y_labels, Y_pred)
    else:
        return compute_categorical_crossentropy_loss(Y_labels, Y_pred)

def float_to_bin(number:np.float32, precision = 32) -> str:
    i = np.float32(2)

    if number < 0:
        representation = "1"
        number = -number
    else:
        representation = "0"
    while(i>(1/(2**precision-2) - 10**-100)):
        if number - i > 0:
            number -= i
            representation += "1"
        else:
            representation += "0"
        i /= 2

    return representation

def bin_to_float(binary:str, precision = 32) -> np.float32:
    number = np.float32(0)
    
    i = np.float32(2)
    for idx in range(1, min(len(binary), precision)):
        if binary[idx] == "1":
            number += i
        i /= 2
    if binary[0] == "1":
        number = -number
    return number


def add_quantum_padding(X) -> None:
    data_pad_amount = get_shape_size(X)
    data_nearest_pow_of_two = int(math.pow(2, math.ceil(math.log2(data_pad_amount))))
    data_pad_amount = data_nearest_pow_of_two - data_pad_amount

    if data_pad_amount != 0:
        data_padding = np.zeros((X.shape[0], data_pad_amount))
        X_return = np.concatenate((X, data_padding), axis = 1)
    else:
        X_return = X.copy()

    assert(X.shape[1] <= MAX_QUBITS)

    return X_return, data_pad_amount
    
def remove_quantum_padding(X:np.ndarray, n_padding: int = 0):
    n_classes = get_shape_size(X) - n_padding
    X = X[:, :n_classes].copy()
    return X