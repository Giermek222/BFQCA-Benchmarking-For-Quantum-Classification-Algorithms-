import sklearn.datasets as skdatasets
from sklearn.model_selection import train_test_split

def load_iris(
    train_size: int = None,
    test_size: int = None,
):
    X, Y= skdatasets.load_iris(return_X_y=True)
    # X, y = shuffle(X, y)

    return train_test_split(
        X, Y, test_size=test_size, train_size=train_size, random_state=42
    )