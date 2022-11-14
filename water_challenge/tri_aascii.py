
import sys

if __name__ == '__main__':

    args = sys.argv
    args.remove(sys.argv[0])

    def ascii_sort(tab):
        for i in range(len(tab), 0, -1):
            for j in range(0, i - 1):
                if tab[j+1][0] < tab[j][0]:
                    tmp = tab[j+1]
                    tab[j+1] = tab[j]
                    tab[j] = tmp

        return tab

    try:
        for h in range(len(args)):
            args[h] = str(args[h])

        print(ascii_sort(args))

    except ValueError as ve:
        print('error.')
