
import sys


def hash_file(name):
    hsh_file = {}

    with open(name, 'r') as file_map:
        ind = 0
        tbl_map = file_map.readlines()
        tmp = []
        for tmp_line in tbl_map:
            for i in tmp_line:
                if i != '\n':
                    tmp.append(i)
            hsh_file[ind] = tmp
            tmp = []
            ind += 1
        file_map.close()
    return hsh_file


def hash_block(hash_map):
    resolve_block = {k: [] for k in range(9)}

    for o in range(9):
        for p in range(9):

            if o < 3 and p < 3:
                resolve_block[0].append(hash_map[o][p])
            elif o < 3 and (3 <= p < 6):
                resolve_block[1].append(hash_map[o][p])
            elif o < 3 and (6 <= p < 9):
                resolve_block[2].append(hash_map[o][p])
            elif (3 <= o < 6) and p < 3:
                resolve_block[3].append(hash_map[o][p])
            elif (3 <= o < 6) and (3 <= p < 6):
                resolve_block[4].append(hash_map[o][p])
            elif (3 <= o < 6) and (6 <= p < 9):
                resolve_block[5].append(hash_map[o][p])
            elif (6 <= o < 9) and p < 3:
                resolve_block[6].append(hash_map[o][p])
            elif (6 <= o < 9) and (3 <= p < 6):
                resolve_block[7].append(hash_map[o][p])
            elif (6 <= o < 9) and (6 <= p < 9):
                resolve_block[8].append(hash_map[o][p])

    return resolve_block


def select_block(ligne, colonne):
    find_block = -1
    if ligne < 3 and colonne < 3:
        find_block = 0
    elif ligne < 3 and (3 <= colonne < 6):
        find_block = 1
    elif ligne < 3 and (6 <= colonne < 9):
        find_block = 2
    elif (3 <= ligne < 6) and colonne < 3:
        find_block = 3
    elif (3 <= ligne < 6) and (3 <= colonne < 6):
        find_block = 4
    elif (3 <= ligne < 6) and (6 <= colonne < 9):
        find_block = 5
    elif (6 <= ligne < 9) and colonne < 3:
        find_block = 6
    elif (6 <= ligne < 9) and (3 <= colonne < 6):
        find_block = 7
    elif (6 <= ligne < 9) and (6 <= colonne < 9):
        find_block = 8
    return find_block


def find_x():
    for i in range(1, 10):
        if str(i) not in current_block and str(i) not in current_line and str(i) not in current_column:
            return i


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    hsh_map = hash_file(args[0])
    blocks = hash_block(hsh_map)

    for line in hsh_map.keys():
        for c in range(len(hsh_map[line])):
            if hsh_map[line][c] == '.':

                current_block = blocks[select_block(line, c)]
                current_line = hsh_map[line]
                current_column = [hsh_map[k][c] for k in range(9)]

                hsh_map[line][c] = find_x()

    for line in hsh_map.keys():
        paper = ''
        for c in range(len(hsh_map[line])):
            paper += '{0}'.format(hsh_map[line][c])
        print(paper)
