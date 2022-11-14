import sys

if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])

    if len(args) >= 2:
        resolve = []
        word = args[len(args) - 1]
        args.pop(len(args) - 1)
        index = -1

        for i in range(len(args)):
            if args[i] == word:
                index = i
                break

        print(index)
    else:
        print('Error.')
