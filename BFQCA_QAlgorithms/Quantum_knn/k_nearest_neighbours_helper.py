import numpy as np


def _kneighbors(y_train: np.ndarray,
                fidelities: np.ndarray,
                n_neighbours,
                *,
                return_indices=False):

    if np.any(fidelities < -0.2) or np.any(fidelities > 1.2):
        raise ValueError("Detected fidelities values not in range 0<=F<=1:"
                         f"{fidelities[fidelities < -0.2]}"
                         f"{fidelities[fidelities > 1.2]}")

    # first sort neighbors
    indices_of_sorted_fidelities = np.argsort(fidelities)

    # extract indices according to number of neighbors
    # and dimension
    n_queries, _ = fidelities.shape
    if n_queries == 1:
        indices_of_sorted_fidelities = indices_of_sorted_fidelities[n_neighbours:]
    else:
        indices_of_sorted_fidelities = indices_of_sorted_fidelities[:, -n_neighbours:]

    sorted_labels = y_train[indices_of_sorted_fidelities]

    if return_indices:
        return sorted_labels, indices_of_sorted_fidelities
    else:
        return sorted_labels
