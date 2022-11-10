import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    hr24 = usr[0:2]
    valhr24 = int(hr24)
    valhr12 = valhr24 - 12

    if valhr12 == 0:
        print('{0}:{1}PM'.format(valhr24, usr[3:5]))
    elif valhr12 > 0:
        # PM
        print('{0}:{1}PM'.format(valhr12, usr[3:5]))
    else:
        # AM
        print('{0}:{1}AM'.format(valhr24, usr[3:5]))
