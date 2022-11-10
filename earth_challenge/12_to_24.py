import sys

if __name__ == '__main__':
    usr = sys.argv[1]

    hr12 = usr[0:2]
    valhr12 = int(hr12)
    state = usr[5:7]

    if state == 'AM':
        print('{0}:{1}'.format(valhr12, usr[3:5]))
    else:
        # PM
        valhr12 = 0 if valhr12 + 12 == 24 else valhr12 + 12
        print('{0:02d}:{1}'.format(valhr12, usr[3:5]))
