
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


def draw(map_of_lines, ori_x=-1, ori_y=-1, length=-1):
    full_coord = []
    if ori_x != -1 and ori_y != -1:
        for x in range(length):
            for w in range(length):
                full_coord.append((ori_x + w, ori_y + x))

    for line in map_of_lines.keys():
        paper = ''
        for c in range(len(map_of_lines[line])):
            if (line, c) in full_coord:
                paper += '{0}'.format(board_full)
            else:
                paper += '{0}'.format(map_of_lines[line][c])
        print(paper)


def check_lines(lines):

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


def test_squares(board_to_test, org_x, org_y):

    def square_valid(x_sqr, y_sqr, s_len):
        for a in range(y_sqr, y_sqr + s_len):
            for b in range(x_sqr, x_sqr + s_len):
                if board_to_test[a][b] is board_obstacle:
                    return False
        return True

    resolved_squares = []
    for j in range(1, int(board_width)):
        if org_y + j in board_to_test.keys() and org_x + j < len(board_to_test[org_y + j]):
            if square_valid(org_x, org_y, j):
                return resolved_squares
            else:
                resolved_squares.append(j)

    return resolved_squares


def find_squares(board):
    resolve_squares = {}
    for origin_y in board.keys():
        for origin_x in range(len(board[origin_y])):
            test = test_squares(board, origin_x, origin_y)
            if len(test) > 0:
                resolve_squares[origin_y, origin_x] = test

    return resolve_squares


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        args.remove(args[0])

    hsh_map = hash_file(args[0])

    file_params = [a for a in hsh_map[0]]
    if len(file_params) > 4:
        raise Exception("Invalid parameters.")

    board_width = int(file_params[0])
    board_empty = file_params[1]
    board_obstacle = file_params[2]
    board_full = file_params[3]

    del hsh_map[0]
    tmp_map = {}
    it = 0
    for i in hsh_map.keys():
        tmp_map[it] = hsh_map[i]
        it += 1
    hsh_map = tmp_map

    if not check_lines(hsh_map):
        raise Exception("Board does not respect rules.")

    defined_squares = find_squares(hsh_map)
    maximum_length = {
        v: defined_squares[v][len(defined_squares[v]) - 1]
        if len(defined_squares[v]) > 0 else -1
        for v in defined_squares.keys()
    }

    bigger_key = (-1, -1)
    bigger_length = -1
    for key in maximum_length.keys():
        if maximum_length[key] > bigger_length:
            bigger_key = key
            bigger_length = maximum_length[key]
        elif maximum_length[key] == bigger_length:
            if bigger_key > key:
                bigger_key = key
                bigger_length = maximum_length[key]

    draw(hsh_map, bigger_key[0], bigger_key[1], bigger_length)
