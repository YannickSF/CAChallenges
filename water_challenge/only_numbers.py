import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])

    try:
        int(args[0])
        print(True)
    except ValueError as ve:
        print(False)
