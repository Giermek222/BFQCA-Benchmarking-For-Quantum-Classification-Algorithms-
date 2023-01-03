import time
import os
import numpy as np

from cowskit_utils.request import make_request, send_request
from cowskit_utils.argparser import parse_flags

def main():
    
    path = os.path.realpath(os.path.dirname(__file__)) + "/"
    args, dataset, encoding, algorithm = parse_flags(hook_path = path, override=False)

    start = time.time()
    X_train, X_test, y_train, y_test = dataset.load_iris(16,32)
    algorithm.fit(X_train, y_train)
    end = time.time()
    total_training_time = round((end-start)*1000, 2)

    # print(X_train.shape)
    # print(y_train.shape)

    latencies = []
    for _ in range(args.tries):
        start = time.time()
        algorithm.predict(X_train[0:1,:])
        end = time.time()
        total_time = round((end-start), 2) # Add *1000
        total_time = round(total_time, 2)
        latencies.append(total_time)


    body = make_request(
        args.dataset,
        args.algorithm,
        algorithm.score(X_train, y_train),
        algorithm.score(X_test, y_test),
        1.0,
        1.0,
        np.max(latencies),
        np.min(latencies),
        round(np.average(latencies), 2),
        round(np.percentile(latencies, args.latency_percentile), 2),
        total_training_time
    )
    send_request(body)

    return body

if __name__ == "__main__":
    main()