import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])

    resolve = []
    try:
        args[0] = int(args[0])
        args[1] = int(args[1])

        resolve = [i for i in range(args[0], args[1])]
        print(resolve)
    except ValueError as ve:
        print(False)
