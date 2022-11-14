
import sys


def fibonacci(high):
    results = [0, 1]
    [results.append(results[v] + results[v + 1]) for v in range(high)]
    return results


if __name__ == '__main__':
    arg = sys.argv[1]
    try:
        index = int(arg)
        if index > 0:
            fibo = fibonacci(index)
            print(fibo[index])
        else:
            print(-1)

    except ValueError as ve:
        print(-1)

