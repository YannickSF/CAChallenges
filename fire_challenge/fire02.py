
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


def compare_pattern(current_map_x, current_map_y, pattern_to_find):
    length_sh_y = len(pattern_to_find.keys())

    def check_line(current_pattern_line):
        length_sh_x = len(pattern_to_find[current_pattern_line])

        for c in range(length_sh_x):
            if current_map_x + c < len(hsh_map[current_map_y + current_pattern_line]):
                if not pattern_to_find[current_pattern_line][c] == ' ':
                    if not pattern_to_find[current_pattern_line][c] == \
                           hsh_map[current_map_y + current_pattern_line][current_map_x + c]:
                        return False
            else:
                return False
        return True

    for q in range(length_sh_y):
        if not check_line(q):
            return False
    return True


def draw(len_x, len_y, x, y, pattern_to_draw):
    paint = {}
    for w in pattern_to_draw.keys():
        for v in range(len(pattern_to_draw[w])):
            paint[x + v, y + w] = pattern_to_draw[w][v]

    for b in range(len_y):
        line = ''
        for d in range(len_x):
            if (d, b) in paint.keys():
                line += '{0}'.format(paint[d, b])
            else:
                line += '-'
        print(line)


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    hsh_map = hash_file(args[0])
    hsh_search = hash_file(args[1])

    found_pattern_x = -1
    found_pattern_y = -1

    for k in hsh_map.keys():
        for e in range(len(hsh_map[k])):
            if hsh_map[k][e] == hsh_search[0][0]:
                if compare_pattern(e, k, hsh_search):
                    found_pattern_x = e
                    found_pattern_y = k
                    print('Trouvé ! \n Coordonnées : {0}, {1}'.format(e, k))
                    draw(len(hsh_map[0]), len(hsh_map.keys()), e, k, hsh_search)

    if found_pattern_x == found_pattern_y == -1:
        print('Introuvable !')
