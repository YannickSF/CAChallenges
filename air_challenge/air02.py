import sys

if __name__ == '__main__':

    def my_function(tab_to_string, sep):
        string_to_create = ''
        for w in tab_to_string:
            string_to_create += w + sep

        return string_to_create


    try:
        args = sys.argv
        args.remove(sys.argv[0])

        sep = args[len(args) - 1]
        args.remove(sep)

        print(my_function(args, sep))

    except ValueError as ve:
        print('Error.')

