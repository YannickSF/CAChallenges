
import sys


if __name__ == '__main__':
    chaine = sys.argv[1]
    reverse = ''

    for i in range(len(chaine) - 1, -1, -1):
        reverse += chaine[i]

    print(reverse)
