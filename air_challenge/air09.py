

import sys


if __name__ == '__main__':

    try:
        args = sys.argv
        args.remove(sys.argv[0])
        with open(args[0], 'r') as file:
            print(file.read())

        file.close()

    except FileNotFoundError as ve:
        print('Error.')
