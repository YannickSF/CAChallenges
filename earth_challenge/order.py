
import sys

if __name__ == '__main__':
    usr = sys.argv
    del usr[0]

    try:
        for j in range(len(usr)):
            usr[j] = int(usr[j])

        order = True
        for k in range(len(usr) - 1):
            if usr[k] > usr[k+1]:
                order = False
                break

        if order:
            print('Triée !')
        else:
            print('Pas triée !')

    except ValueError as ve:
        print('erreur.')
