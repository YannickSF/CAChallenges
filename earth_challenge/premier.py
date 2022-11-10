import sys
from math import sqrt


def check_if_first(value):
    find_dividend = False

    for i in range(2, value):
        if value % i == 0:
            find_dividend = True

    return not find_dividend


if __name__ == '__main__':
    nb = sys.argv[1]

    try:
        val = int(nb)
        if val == 0 or val == 1:
            print('Non, {0} n’est pas un nombre premier.'.format(val))
        else:
            if check_if_first(val):
                print('Oui, {0} est un nombre premier.'.format(val))
            else:
                print('Non, {0} n’est pas un nombre premier.'.format(val))

    except ValueError:
        print('argument error .')
