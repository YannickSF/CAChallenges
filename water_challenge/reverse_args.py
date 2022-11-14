
import sys

if __name__ == '__main__':

    args = sys.argv
    args.remove(sys.argv[0])

    resolve = []
    for a in args:
        tmp_tab = a.split(' ')
        if len(tmp_tab) > 0:
            for d in tmp_tab:
                resolve.append(d)
        else:
            resolve.append(tmp_tab[0])
    reverse = [resolve[b] for b in range(len(resolve) - 1, -1, -1)]

    for c in reverse:
        print(c)
