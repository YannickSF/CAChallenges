

import sys


if __name__ == '__main__':

    def my_function(values, ope):
        resolve = []
        for i in values:
            if ope in i or ope.upper() in i:
                resolve.append(i)

        return resolve

    try:
        args = sys.argv
        args.remove(sys.argv[0])
        operator = args[len(args) - 1]
        args.remove(operator)

        result = my_function(args, operator)
        print(result)

    except ValueError as ve:
        print('Error.')
