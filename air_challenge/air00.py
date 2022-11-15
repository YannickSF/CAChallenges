
import sys


if __name__ == '__main__':

    def cutter(string_to_cut, sep):
        resolve = []
        word = ''
        for i in string_to_cut:
            if i == sep:
                resolve.append(word)
                word = ''
            else:
                word += i

        if word != '':
            resolve.append(word)

        return resolve if len(resolve) > 0 else [word]


    try:
        args = sys.argv
        args.remove(sys.argv[0])

        space_result = cutter(args[0], ' ')

        tab_result = []
        for k in space_result:
            tab_result = tab_result + cutter(k, '\t')

        return_result = []
        for j in space_result:
            return_result = return_result + cutter(j, '\n')

        for m in return_result:
            print(m)
    except ValueError as ve:
        print('Error.')
        
