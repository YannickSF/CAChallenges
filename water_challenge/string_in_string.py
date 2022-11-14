
import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])
    if len(args) < 2:
        print('Error.')
    else:
        try:
            args[0] = str(args[0])
            args[1] = str(args[1])
        except ValueError as ve:
            print('Error.')

        print(True) if args[1] in args[0] else print(False)

