
import sys


def hash_file(name):
    hsh_file = {}

    with open(name, 'r') as file_map:
        ind = 0
        tbl_map = file_map.readlines()
        tmp = []
        for line in tbl_map:
            for i in line:
                if i != '\n':
                    tmp.append(i)
            hsh_file[ind] = tmp
            tmp = []
            ind += 1
        file_map.close()
    return hsh_file


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    hsh_map = hash_file(args[0])
