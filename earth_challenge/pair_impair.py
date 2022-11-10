
import sys

PAIR = [0, 2, 4, 6, 8]
IMPAIR = [1, 3, 5, 7, 9]


if __name__ == '__main__':

    user = sys.argv[1]
    try:
        value = int(user)

        if int(user[len(user) - 1]) in PAIR:
            print('pair')

        if int(user[len(user) - 1]) in IMPAIR:
            print('impair')

    except ValueError as ve:
        print('Tu ne me la mettras pas à l’envers.')

