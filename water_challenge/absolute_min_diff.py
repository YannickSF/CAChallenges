import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])

    try:
        args = [int(a) for a in args]

    except ValueError as ve:
        print('Error.')

    if len(args) >= 2:
        table = []

        for i in range(len(args)):
            if i < len(args) - 1:
                for j in range(i + 1, len(args)):
                    diff = args[i] - args[j]
                    if diff < 0:
                        diff = diff * -1

                    table.append(diff)

        table.sort()
        print(table[0])
    else:
        print('Error.')
