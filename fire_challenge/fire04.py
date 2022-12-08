
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


def draw(map_of_lines):
    for line in map_of_lines.keys():
        paper = ''
        for c in range(len(map_of_lines[line])):
            paper += '{0}'.format(map_of_lines[line][c])
        print(paper)


def check_lines(params, lines):
    board_width = int(params[0])
    board_empty = params[1]
    board_obstacle = params[2]
    board_full = params[3]

    if len(lines.keys()) != board_width:
        return False

    line_length = -1
    for line in lines.keys():
        current_line_as_tab = [li for li in lines[line]]
        if line_length == -1:
            line_length = len(current_line_as_tab)

        if len(current_line_as_tab) != line_length:
            return False
        else:
            line_length = len(current_line_as_tab)

        for e in current_line_as_tab:
            if e == board_empty:
                pass
            elif e == board_obstacle:
                pass
            elif e == board_full:
                pass
            else:
                return False

    return True


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    hsh_map = hash_file(args[0])

    file_params = [a for a in hsh_map[0]]
    if len(file_params) > 4:
        raise Exception("Invalid parameters.")
    del hsh_map[0]

    if not check_lines(file_params, hsh_map):
        raise Exception("Board does not respect rules.")

    # todo : find biggest square

    draw(hsh_map)
