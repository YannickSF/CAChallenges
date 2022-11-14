
import sys


def check_if_first(value):
    find_dividend = False

    for i in range(2, value):
        if value % i == 0:
            find_dividend = True

    return not find_dividend


if __name__ == '__main__':
    arg = sys.argv[1]
    try:
        index = int(arg)
        if index > 0:
            find = False
            while not find:
                index += 1
                if check_if_first(index):
                    print(index)
                    find = True
        else:
            print(-1)

    except ValueError as ve:
        print(-1)

