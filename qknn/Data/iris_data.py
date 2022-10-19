import sklearn.datasets as skdatasets
from typing import Optional, Union, Tuple
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import Bunch
from sklearn.decomposition import PCA


def pca_reduce(
    X_train: np.ndarray, X_test: np.ndarray, n_components: int = 2
) -> Tuple[np.ndarray, np.ndarray]:
    pca = PCA(n_components=n_components)
    X_train = pca.fit_transform(X_train)
    X_test = pca.fit_transform(X_test)

    return (X_train, X_test)


def features_labels_from_data(
    X: Union[np.ndarray, list],
    y: Union[np.ndarray, list],
    train_size: Optional[Union[float, int]] = None,
    test_size: Optional[Union[float, int]] = None,
    n_features: Optional[int] = None,
    *,
    use_pca: Optional[bool] = False,
    return_bunch: Optional[bool] = False
):
    """
    This script splits a dataset according to the required train size, test size and
    number of features

    Args:
        X:
            raw data from dataset
        y:
            labels from dataset

        test_size :
            float or int, default=None
            If float, should be between 0.0 and 1.0 and represent the proportion
            of the dataset to include in the test split. If int, represents the
            absolute number of test samples. If None, the value is set to the
            complement of the train size. If ``train_size`` is also None, it will
            be set to 0.25.

        train_size : float or int, default=None
            If float, should be between 0.0 and 1.0 and represent the
            proportion of the dataset to include in the train split. If
            int, represents the absolute number of train samples. If None,
            the value is automatically set to the complement of the test size.

        n_features:
            number of desired features

        use_pca:
            whether to use PCA for dimensionality reduction or not
            default False

        return_bunch:
            whether to return a :class:`sklearn.Bunch`
            (similar to a dictionary) or not

        Returns:
            Preprocessed dataset as available in sklearn
    """

    # decomposing dataset according to the required train and test size
    # exceptions are already handled in train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, train_size=train_size, random_state=42
    )

    if n_features is not None:
        if use_pca:
            X_train, X_test = pca_reduce(X_train, X_test, n_components=n_features)
        else:
            X_train = X_train[:, 0:n_features]
            X_test = X_test[:, 0:n_features]

    if return_bunch:
        # a Bunch is similar to a
        # dictionary (actually inherits from it)
        return Bunch(
            training_data=X_train,
            test_data=X_test,
            training_labels=y_train,
            test_labels=y_test,
        )

    return (X_train, X_test, y_train, y_test)


def load_iris(
    train_size: Optional[Union[float, int]] = None,
    test_size: Optional[Union[float, int]] = None,
    n_features: Optional[int] = None,
    *,
    use_pca: Optional[bool] = False,
    return_bunch: Optional[bool] = False
):
    """
    This script loads iris dataset from sklearn and splits it according to
    the required train size, test size and number of features

    Args:
        test_size :
            float or int, default=None
            If float, should be between 0.0 and 1.0 and represent the proportion
            of the dataset to include in the test split. If int, represents the
            absolute number of test samples. If None, the value is set to the
            complement of the train size. If ``train_size`` is also None, it will
            be set to 0.25.

        train_size : float or int, default=None
            If float, should be between 0.0 and 1.0 and represent the
            proportion of the dataset to include in the train split. If
            int, represents the absolute number of train samples. If None,
            the value is automatically set to the complement of the test size.

        n_features:
            number of desired features

        use_pca:
            whether to use PCA for dimensionality reduction or not
            default False

        return_bunch:
            whether to return a :class:`~sklearn.utils.Bunch`
            (similar to a dictionary) or not

        Returns:
            Iris dataset as available in sklearn
    """
    # X: data
    # y: labels
    X, y = skdatasets.load_iris(return_X_y=True)

    return features_labels_from_data(
        X,
        y,
        train_size,
        test_size,
        n_features,
        use_pca=use_pca,
        return_bunch=return_bunch,
    )
