import sys

if __name__ == '__main__':

    def my_function(string_to):
        string_to_create = ''
        last_letter = ''

        for letter in string_to:
            if last_letter != letter:
                string_to_create += letter
                last_letter = letter
        return string_to_create


    try:
        args = sys.argv
        args.remove(sys.argv[0])

        print(my_function(args[0]))

    except ValueError as ve:
        print('Error.')

