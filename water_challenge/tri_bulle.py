
import sys

if __name__ == '__main__':

    args = sys.argv
    args.remove(sys.argv[0])

    def my_bubble_sort(tab):
        for i in range(len(tab), 0, -1):
            for j in range(0, i - 1):
                if tab[j+1] < tab[j]:
                    tmp = tab[j+1]
                    tab[j+1] = tab[j]
                    tab[j] = tmp

        return tab

    try:
        for h in range(len(args)):
            args[h] = int(args[h])

        print(my_bubble_sort(args))

    except ValueError as ve:
        print('error.')
