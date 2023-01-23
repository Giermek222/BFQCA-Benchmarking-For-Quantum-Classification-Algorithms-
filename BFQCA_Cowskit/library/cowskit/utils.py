import numpy as np
from cowskit.constants import ROUND_DIGITS

def get_shape_size(data:np.ndarray) -> int:
    if len(data.shape) == 1:
        return 1
    features_shape = data.shape[1:]
    return np.prod(features_shape)

def compute_possibilities(n_classes: int, n_padding: int = 0) -> np.ndarray:
    if n_classes != 1:
        possiblities = np.eye(n_classes - n_padding)
    else:
        possiblities = np.array([[-1], [1]])
    if n_padding != 0:
        possiblities = np.pad(possiblities, (0, n_padding), 'constant', constant_values=(0))
    return possiblities

def sigmoid(x) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

def softmax(x) -> np.ndarray:
    return (np.exp(x)/np.exp(x).sum(axis=1, keepdims = True))

def one_hot(x) -> np.ndarray:
    return (x == x.max(axis=1)[:,None]).astype(int)

def preprocess_labels(Y_labels:np.ndarray, Y_pred:np.ndarray, n_padding: int = 0):
    n_classes = get_shape_size(Y_labels) - n_padding
    Y_labels = Y_labels[:, :n_classes]
    Y_pred = Y_pred[:, :n_classes]

    if n_classes != 1:
        Y_pred = softmax(Y_pred)

    return Y_labels, Y_pred

def compute_confusion_matrix(Y_labels:np.ndarray, Y_pred:np.ndarray):           
    """                             truths
    \\ tr tr tr                     x y z
    la                             x
    la                     labels  y
    la                             z
    
    """
    n_classes = get_shape_size(Y_labels)

    if n_classes != 1:
        result = np.zeros((n_classes, n_classes))
        Y_pred_copy = one_hot(Y_pred)
    else:
        result = np.zeros((2,2))
        Y_pred_copy = np.round(Y_pred)

    possibilities = compute_possibilities(n_classes)  

    for x_idx, x_axis_possibility in enumerate(possibilities):
        for y_idx, y_axis_possibility in enumerate(possibilities):
            result[y_idx][x_idx] = ((Y_labels == y_axis_possibility) & (Y_pred_copy == x_axis_possibility)).sum()

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
    Y_pred_copy = sigmoid(Y_pred_copy)

    N = Y_labels_copy.shape[0]
    binary_crossentropy = -1/N * np.sum(Y_labels_copy * np.log(Y_pred_copy + 10**-100) + (1 - Y_labels_copy) * np.log(1 - Y_pred_copy + 10**-100))

    return np.round(binary_crossentropy, ROUND_DIGITS)
    
def compute_categorical_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()

    Y_pred_copy = softmax(Y_pred_copy)
    categorical_crossentropy = -np.sum(Y_labels_copy * np.log(Y_pred_copy + 10**-100))

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