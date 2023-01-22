import numpy as np

def remove_padding_from_labels(Y_labels:np.ndarray, Y_pred:np.ndarray, n_padding: int = 0):
    n_classes = get_shape_size(Y_labels) - n_padding
    Y_labels = Y_labels[:, :n_classes]
    Y_pred = Y_pred[:, :n_classes]

    if n_classes != 1:
        Y_pred = softmax(Y_pred)
    else:
        Y_pred = np.round(Y_pred)

def compute_confusion_matrix(Y_labels:np.ndarray, Y_pred:np.ndarray):

    n_classes = get_shape_size(Y_labels)
    result = np.zeros((n_classes, n_classes))

    possibilities = np.eye(n_classes)
    for x_idx, x_axis_possibility in enumerate(possibilities):
        for y_idx, y_axis_possibility in enumerate(possibilities):
            result[y_idx][x_idx] = ((Y_labels == y_axis_possibility) & (Y_pred == x_axis_possibility)).sum()

    return result

def get_shape_size(data:np.ndarray) -> int:
    if len(data.shape) == 1:
        return 1
    features_shape = data.shape[1:]
    return np.prod(features_shape)

def softmax(x) -> np.ndarray:
    return(np.exp(x)/np.exp(x).sum(axis=1)) # was without axis

def one_hot(x) -> np.ndarray:
    return (x == x.max(axis=1)[:,None]).astype(int)

def compute_possibilities(n_classes: int, n_padding: int = 0) -> np.ndarray:
    possiblities = np.eye(n_classes - n_padding)
    possiblities = np.pad(possiblities, (0,n_padding), 'constant', constant_values=(0))
    return possiblities
    
def compute_accuracy(Y_labels:np.ndarray, Y_pred:np.ndarray, n_padding: int = 0) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()

    n_classes = get_shape_size(Y_labels_copy)
    if n_classes != 1:
        Y_pred_copy = softmax(Y_pred_copy)
        Y_pred_copy = one_hot(Y_pred_copy)
    else:
        Y_pred_copy = np.round(Y_pred_copy)

    N = Y_labels_copy.shape[0]
    possibilities = compute_possibilities(n_classes, n_padding)

    accuracy = 0
    for possibility in possibilities:
        TP = ((Y_pred_copy == possibility) & (Y_labels_copy == possibility)).sum()
        TN = ((Y_pred_copy != possibility) & (Y_labels_copy != possibility) & (Y_pred_copy == Y_labels_copy)).sum()
        accuracy += (TP + TN) / N
    accuracy /= n_classes
    
    return accuracy

def compute_precision(Y_labels:np.ndarray, Y_pred:np.ndarray, n_padding: int = 0) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()

    n_classes = get_shape_size(Y_labels_copy)
    if n_classes != 1:
        Y_pred_copy = softmax(Y_pred_copy)
        Y_pred_copy = one_hot(Y_pred_copy)
    else:
        Y_pred_copy = np.round(Y_pred_copy)

    possibilities = compute_possibilities(n_classes, n_padding)
    precision = 0
    for possibility in possibilities:
        TP = ((Y_pred_copy == possibility) & (Y_labels_copy == possibility)).sum()
        FP = ((Y_pred_copy == possibility) & (Y_labels_copy != possibility)).sum()
        if TP + FP == 0: FP = 1
        precision += TP / (TP + FP)
    precision /= n_classes
    return precision

def compute_recall(Y_labels:np.ndarray, Y_pred:np.ndarray, n_padding: int = 0) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()

    n_classes = get_shape_size(Y_labels_copy)
    if n_classes != 1:
        Y_pred_copy = softmax(Y_pred_copy)
        Y_pred_copy = one_hot(Y_pred_copy)
    else:
        Y_pred_copy = np.round(Y_pred_copy)

    possibilities = compute_possibilities(n_classes, n_padding)
    recall = 0
    for possibility in possibilities:
        TP = ((Y_pred_copy == possibility) & (Y_labels_copy == possibility)).sum()
        FN = ((Y_pred_copy != possibility) & (Y_labels_copy != possibility) & (Y_pred_copy != Y_labels_copy)).sum()
        if TP + FN == 0: FN = 1
        recall += TP / (TP + FN)
    recall /= n_classes
    return recall

def compute_f1_score(Y_labels:np.ndarray, Y_pred:np.ndarray, n_padding: int = 0) -> float:
    precision = compute_precision(Y_labels, Y_pred, n_padding)
    recall = compute_recall(Y_labels, Y_pred, n_padding)
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2*precision*recall/(precision+recall)

    return f1_score

def compute_binary_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()

    Y_labels_copy, Y_pred_copy = Y_labels_copy.flatten(), Y_pred_copy.flatten()

    N = Y_labels_copy.shape[0]
    binary_crossentropy = -1/N * np.sum(Y_labels_copy * np.log(Y_pred_copy + 10**-100) + (1 - Y_labels_copy) * np.log((1 - Y_pred_copy) + 10**-100))

    return binary_crossentropy
    
def compute_categorical_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray) -> float:
    Y_labels_copy, Y_pred_copy = Y_labels.copy(), Y_pred.copy()

    Y_pred_copy = softmax(Y_pred_copy)
    Y_labels_copy, Y_pred_copy = Y_labels_copy.flatten(), Y_pred_copy.flatten()
    categorical_crossentropy = -np.sum(Y_labels_copy * np.log(Y_pred_copy + 10**-100))
    
    return categorical_crossentropy

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