import sys


if __name__ == '__main__':
    nb = sys.argv[1]
    ps = sys.argv[2]

    try:
        val = int(nb)
        pss = int(ps)
        print(pow(val, pss))

    except ValueError:
        print('argument error .')
