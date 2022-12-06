
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    def hr(column, fill_hr):
        line = 'o'
        if column > 2:
            line += 'o'.rjust(fill_hr + 1, '-')
        elif column == 2:
            line += 'o'

        return line

    def vr(fill_vr):
        return '|' + '|'.rjust(fill_vr + 1, ' ')

    long = 0
    haut = 0
    try:
        for i in range(len(args)):
            args[i] = int(args[i])

        long = args[0]
        haut = args[1]

        if long < 1 or haut < 1:
            print('Error.')
        else:
            resolve = []
            fill = long - 2
            if fill < 0:
                fill = 0

            for i in range(haut):
                if i == 0 or i == haut - 1:
                    resolve.append(hr(long, fill))
                else:
                    resolve.append(vr(fill))

            for r in resolve:
                print(r)

    except ValueError as ve:
        print('Error.')
