
import sys


if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    try:
        if a > b:
            print('résultat: {0}'.format(a // b))
            print('reste: {0}'.format(a % b))
        else:
            print('erreur .')

    except ZeroDivisionError:
        print('erreur .')
