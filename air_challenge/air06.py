

import sys


if __name__ == '__main__':

    def my_function(values, ins):
        for i in range(len(values)):
            if values[i] < ins < values[i+1]:
                values.insert(i + 1, ins)
                break
        return values

    try:
        args = sys.argv
        args.remove(sys.argv[0])
        operator = args[len(args) - 1]
        args.remove(operator)

        result = my_function(args, operator)
        print(result)

    except ValueError as ve:
        print('Error.')
