import numpy as np
def _kneighbors(self,
                y_train: np.ndarray,
                fidelities: np.ndarray,
                *,
                return_indices=False):
    """
    Retrieves the training labels associated to the :math:`k`
    nearest neighbors and (optionally) their indices

    Args:
        y_train:
            the training labels

        fidelities:
            the fidelities array

        return_indices:
            (bool) weather to return the indices or not

    Returns:
        neigh_labels: ndarray of shape (n_queries, n_neighbors)
            Array representing the labels of the :math:`k` nearest points

        neigh_indices: ndarray of shape (n_queries, n_neighbors)
            Array representing the indices of the :math:`k` nearest points,
            only present if return_indices=True.
    """
    if np.any(fidelities < -0.2) or np.any(fidelities > 1.2):
        raise ValueError("Detected fidelities values not in range 0<=F<=1:"
                         f"{fidelities[fidelities < -0.2]}"
                         f"{fidelities[fidelities > 1.2]}")

    # first sort neighbors
    neigh_indices = np.argsort(fidelities)

    # extract indices according to number of neighbors
    # and dimension
    n_queries, _ = fidelities.shape
    if n_queries == 1:
        neigh_indices = neigh_indices[-self.n_neighbors:]
    else:
        neigh_indices = neigh_indices[:, -self.n_neighbors:]

    neigh_labels = y_train[neigh_indices]

    if return_indices:
        return neigh_labels, neigh_indices
    else:
        return neigh_labels