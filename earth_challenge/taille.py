import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('erreur .')
    else:
        try:
            val = int(sys.argv[1])
            print('erreur .')

        except ValueError as ve:
            print(len(sys.argv[1]))
