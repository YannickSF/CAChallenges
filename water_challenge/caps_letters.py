
import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])

    try:
        int(args[0])
        print('Error.')

    except ValueError as ve:
        step = True
        resolve = ''
        for i in range(len(args[0])):
            if step:
                resolve += args[0][i].upper()
            else:
                resolve += args[0][i].lower()

            step = not step

        print(resolve)

