import sys

if __name__ == '__main__':

    def cutter(string_to_cut, sep):
        return string_to_cut.split(sep)


    try:
        args = sys.argv
        args.remove(sys.argv[0])

        return_result = cutter(args[0], args[1])

        for m in return_result:
            print(m)
            
    except ValueError as ve:
        print('Error.')

