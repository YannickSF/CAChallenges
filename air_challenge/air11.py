
import sys

if __name__ == '__main__':

    args = sys.argv
    args.remove(sys.argv[0])

    try:

        for h in range(len(args)):
            args[h] = int(args[h])


        def my_sort_checker(tab):
            for c in range(len(tab) - 1):
                if tab[c] > tab[c + 1]:
                    return False
            return True


        def my_quicksort(tab, pivot):
            for i in range(len(tab)):
                if tab[i] > pivot:
                    tab.append(tab[i])
                    tab.remove(tab[i])

            return tab


        index_pivot = 0
        while not my_sort_checker(args):
            if index_pivot + 1 < len(args) - 1:
                index_pivot += 1
            else:
                index_pivot = 0

            args.append(args[index_pivot])
            args.remove(args[index_pivot])

            args = my_quicksort(args, args[len(args) - 1])

        print(args)

    except ValueError as ve:
        print('error.')
