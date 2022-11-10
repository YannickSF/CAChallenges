
import sys


if __name__ == '__main__':
    chaine = ''
    start = False
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z']

    letter_from = sys.argv[1]
    for i in alp:

        if start:
            chaine += i
        else:
            if letter_from == i:
                chaine += letter_from
                start = True

    print(chaine)
