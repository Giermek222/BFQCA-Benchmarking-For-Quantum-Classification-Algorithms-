import numpy as np
import struct

def get_shape_size(data:np.ndarray) -> int:
    if len(data.shape) == 1:
        return 1
    features_shape = data.shape[1:]
    return np.prod(features_shape)

def softmax(x):
    return(np.exp(x)/np.exp(x).sum())

def one_hot(x):
    if len(x.shape) == 1: return x
    return (x == x.max(axis=1)[:,None]).astype(int)
    
def compute_accuracy(Y_labels:np.ndarray, Y_pred:np.ndarray):
    samples_count = Y_labels.shape[0]
    n_classes = get_shape_size(Y_labels)
    Y_pred = softmax(Y_pred)
    Y_pred = one_hot(Y_pred)
    
    Y_labels, Y_pred = Y_labels.flatten(), Y_pred.flatten()
    
    return (Y_labels == Y_pred).sum() / n_classes / samples_count

def compute_precision(Y_labels:np.ndarray, Y_pred:np.ndarray):
    n_classes = get_shape_size(Y_labels)
    Y_pred = softmax(Y_pred)
    Y_pred = one_hot(Y_pred)
    
    possibilities = np.eye(n_classes)
    precision = 0
    for possibility in possibilities:
        TP = ((Y_pred == possibility) & (Y_labels == possibility)).sum()
        FP = ((Y_pred == possibility) & (Y_labels != possibility)).sum()
        if TP + FP == 0: FP = 1
        precision += TP / (TP + FP)
    precision /= n_classes
    return precision

def compute_recall(Y_labels:np.ndarray, Y_pred:np.ndarray):
    n_classes = get_shape_size(Y_labels)
    Y_pred = softmax(Y_pred)
    Y_pred = one_hot(Y_pred)
    
    possibilities = np.eye(n_classes)
    recall = 0
    for possibility in possibilities:
        TP = ((Y_pred == possibility) & (Y_labels == possibility)).sum()
        FN = ((Y_pred != possibility) & (Y_labels == possibility)).sum()
        if TP + FN == 0: FN = 1
        recall += TP / (TP + FN)
    recall /= n_classes
    return recall

def compute_f1_score(Y_labels:np.ndarray, Y_pred:np.ndarray):
    precision = compute_precision(Y_labels, Y_pred)
    recall = compute_recall(Y_labels, Y_pred)
    if precision + recall == 0:
        f1_score = 0
    else:
        f1_score = 2*precision*recall/(precision+recall)

    return f1_score

def compute_categorical_crossentropy_loss(Y_labels:np.ndarray, Y_pred:np.ndarray):
    Y_pred = softmax(Y_pred)

    Y_labels, Y_pred = Y_labels.flatten(), Y_pred.flatten()
    categorical_crossentropy = - np.sum(Y_labels * np.log(Y_pred + 10**-100))
    
    return categorical_crossentropy

def float_to_bin(number:np.float32):
    return np.binary_repr(number.view(np.int32), width=32)

def bin_to_float(binary:str):
    return np.float32(struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0])

def float_to_binV2(number:np.float32):
    i = np.float32(2)

    if number < 0:
        representation = "1"
        number = -number
    else:
        representation = "0"
    while(i>(1/(2**30) - 10**-100)):
        if number - i > 0:
            number -= i
            representation += "1"
        else:
            representation += "0"
        i /= 2

    return representation

def bin_to_floatV2(binary:str):
    number = np.float32(0)
    
    i = np.float32(2)
    for idx in range(1, len(binary)):
        if binary[idx] == "1":
            number += i
        i /= 2
    if binary[0] == "1":
        number = -number
    return number