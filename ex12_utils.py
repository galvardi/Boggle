###############################################################
# FILE : ex12_utils.py
# WRITER : Raz Zeevy , raz.zeevy ,207481664, Gal Vardi, galvardi, 208935031,
# EXERCISE : intro2cs2 ex12 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED:
###############################################################

from boggle_board_randomizer import randomize_board

def is_valid_path(board, path, words):
    for loc in range(0, len(path) - 1):
        for coor in [0, 1]:
            if path[loc][coor] - path[loc + 1][coor] not in [0, 1, -1]:
                return
    word = "".join([board[loc[0]][loc[1]] for loc in path])
    if word in words: return True


def pos_cords_gen(start_coor, path=None):
    """"""
    pos_coords = []
    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            pos_coor = (start_coor[0] + i, start_coor[1] + j)
            if (3 >= pos_coor[0] >= 0) and \
                    (3 >= pos_coor[1] >= 0):
                if not path or pos_coor not in path:
                    pos_coords.append(pos_coor)
    return pos_coords

def find_length_n_paths(n, board, words):
    """ """

    def find_length_n_paths_helper(coords, n, cur_word, board, path,
                                   pos_paths,
                                   words):
        """ """
        if len(path) == n:
            if cur_word in words:
                pos_paths.append(path[:])
                return pos_paths
            else:
                return pos_paths
        double_char = False
        pos_coords = pos_cords_gen((coords[0], coords[1]), path)
        for check_coords in pos_coords:
            if len(board[check_coords[0]][
                       check_coords[1]]) == 2: double_char = True
            cur_word += board[check_coords[0]][check_coords[1]]
            path.append(check_coords)
            find_length_n_paths_helper(check_coords, n, cur_word, board,
                                       path[:],
                                       pos_paths, words)
            path.pop()
            cur_word = cur_word[:-2] if double_char else cur_word[:-1]
        return pos_paths

    cur_word = ""
    path = []
    pos_paths = []
    double_char = False
    for row in range(len(board)):
        for col in range(len(board[0])):
            if not cur_word:
                cur_word += board[row][col]
                path.append((row, col))
            if len(board[row][col]) == 2: double_char = True
            pos_paths = find_length_n_paths_helper((row, col), n, cur_word,
                                                   board, path, pos_paths,
                                                   words)
            cur_word = cur_word[:-2] if double_char else cur_word[:-1]
            if path: path.pop()

    return pos_paths


def find_length_n_words(n, board, words):
    def find_possible_path(word):
        paths = []
        find_path_helper(word, None, [], paths)
        return paths

    def find_path_helper(word, start_coor, path, paths):
        if not word:
            return paths.append(path)
        if start_coor:
            pos_coors = pos_cords_gen(start_coor, path=path)
        else:
            pos_coors = [(i, j) for i in range(len(board)) for j in range(
                len(board[0]))]
        for coor in pos_coors:
            square = board[coor[0]][coor[1]]
            if square == word[0:len(square)]:
                find_path_helper(word[len(square):], coor, path + [coor],
                                 paths)

    paths = []
    for word in words:
        if len(word) != n:
            continue
        word_paths = find_possible_path(word)
        if word_paths: paths.append((word, word_paths))
    return paths


def max_score_paths(_board, _words):
    words_found = []
    score = 0
    board_paths = []
    for i in range(4 * 4 + 1):
        paths_to_word = find_length_n_words(i, _board, _words)
        for paths in paths_to_word:
            words_found.append(paths[0])
            score += max([len(path) for path in paths[1]]) ** 2
            longest_path = sorted(paths[1], key=lambda path: len(path),
                               reverse=True)[0]
            board_paths.append(longest_path)
    return board_paths

def get_words():
    with open('boggle_dict.txt', 'r') as f:
        words = [word.strip('\n') for word in f]
    return words

board = [['A', 'BAG', 'A', 'BAG'],
         ['Q', 'L', 'E', 'A'],
         ['Q', 'R', 'BAG', 'G'],
         ['RA', 'Z', 'Q', 'A']]
words = ['ALBERT', 'RAZ', 'BAG']

board = randomize_board()
words = get_words()
a = max_score_paths(board, words)
print(a)

# _board = randomize_board()

# print(_board)
# a = max_score_paths(_board, words)
# a = is_valid_path(_board, [(0, 0), (1, 0), (0, 2)], get_words())
