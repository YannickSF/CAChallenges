
import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])

    try:
        int(args[0])
        print('Error.')

    except ValueError as ve:
        focus = True
        resolve = ''
        for i in range(len(args[0])):
            if focus:
                resolve += args[0][i].upper()
            else:
                resolve += args[0][i].lower()

            if args[0][i] == ' ':
                focus = True
            else:
                focus = False

        print(resolve)

