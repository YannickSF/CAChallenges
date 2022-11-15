

import sys


if __name__ == '__main__':

    def create_list(values):
        l1 = []
        l2 = []
        fusion = False
        for v in range(len(values)):
            if values[v] == 'fusion':
                fusion = not fusion
            else:
                if fusion:
                    l2.append(values[v])
                else:
                    l1.append(values[v])

        return l1, l2


    def my_function(lone, ltwo):
        def my_bubble_sort(tab):
            for i in range(len(tab), 0, -1):
                for j in range(0, i - 1):
                    if tab[j + 1] < tab[j]:
                        tmp = tab[j + 1]
                        tab[j + 1] = tab[j]
                        tab[j] = tmp

            return tab

        resolve = lone + ltwo
        return my_bubble_sort(resolve)

    try:
        args = sys.argv
        args.remove(sys.argv[0])
        list1, list2 = create_list(args)

        result = my_function(list1, list2)
        print(result)

    except ValueError as ve:
        print('Error.')
