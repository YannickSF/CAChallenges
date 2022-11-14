
import sys

if __name__ == '__main__':

    args = sys.argv
    args.remove(sys.argv[0])

    def my_select_sort(tab):
        for i in range(len(tab) - 2):
            mini = i
            for j in range(i + 1, len(tab)):
                if tab[j] < tab[mini]:
                    mini = j

            if mini != i:
                tmp = tab[i]
                tab[i] = tab[mini]
                tab[mini] = tmp

        return tab

    try:
        for h in range(len(args)):
            args[h] = int(args[h])

        print(my_select_sort(args))

    except ValueError as ve:
        print('error.')
