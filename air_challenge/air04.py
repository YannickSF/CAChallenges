

import sys


if __name__ == '__main__':

    def my_function(values, ope):
        for i in range(len(values)):
            values[i] = values[i] + ope

        return values

    try:
        args = sys.argv
        args.remove(sys.argv[0])
        operator = args[len(args) - 1]
        args.remove(operator)

        for a in range(len(args)):
            args[a] = int(args[a])

        result = my_function(args, int(operator))

        print(result)

    except ValueError as ve:
        print('Error.')
