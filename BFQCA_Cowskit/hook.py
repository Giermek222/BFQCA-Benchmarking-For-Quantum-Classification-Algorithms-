import time


from cowskit_utils.request import make_request, send_request
from cowskit_utils.argparser import parse_flags

def main():
    
    args, dataset, encoding, algorithm = parse_flags(override=True)

    start = time.time()
    print(start)
    X_train, X_test, y_train, y_test = dataset.load_iris(16,32)
    algorithm.fit(X_train, y_train)
    end = time.time()
    print(end)

    total_time = round(end-start, 2)
    print(total_time)

    body = make_request(
        args.problem_name,
        args.algorithm,
        algorithm.score(X_train, y_train),
        algorithm.score(X_test, y_test),
        1.0,
        1.0,
        total_time,
        total_time,
        total_time,
        total_time,
        total_time
    )
    send_request(body)

    return body

if __name__ == "__main__":
    main()