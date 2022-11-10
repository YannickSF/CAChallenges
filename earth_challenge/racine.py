import sys
from math import sqrt

if __name__ == '__main__':
    nb = sys.argv[1]

    try:
        val = int(nb)
        if val > 0:
            print(int(sqrt(val)))
        else:
            print('argument error .')

    except ValueError:
        print('argument error .')
