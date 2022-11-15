

import sys


if __name__ == '__main__':

    def my_function(values):

        operator = args[0]
        values.remove(operator)
        values.append(operator)
        return values

    try:
        args = sys.argv
        args.remove(sys.argv[0])

        result = my_function(args)
        print(str.join(', ', result))

    except ValueError as ve:
        print('Error.')
