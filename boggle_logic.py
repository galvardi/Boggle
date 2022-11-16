###############################################################
# FILE : boggle_logic.py
# WRITER : Raz Zeevy , raz.zeevy ,207481664, Gal Vardi, galvardi, 208935031,
# EXERCISE : intro2cs2 ex12 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED:
###############################################################
# Constants
MIN_LEN_WORD = 3
BOARD_ROWS = 4
BOARD_COLS = 4

def is_valid_path(path):
    for loc in range(0, len(path) - 1):
        for coor in [0, 1]:
            if path[loc][coor] - path[loc + 1][coor] not in [0, 1, -1]:
                return False
    return True

def pos_cords_gen(start_coor, path=None):
    """"""
    pos_coords = []
    for i in [-1, 1, 0]:
        for j in [-1, 1, 0]:
            pos_coor = (start_coor[0] + i, start_coor[1] + j)
            if (BOARD_ROWS-1 >= pos_coor[0] >= 0) and \
                    (BOARD_COLS-1 >= pos_coor[1] >= 0):
                if not path or pos_coor not in path:
                    pos_coords.append(pos_coor)
    return pos_coords

def find_length_n_words(n, board, words, get_max=False):
    def find_possible_path(word):
        paths = []
        find_path_helper(word, None, [], paths)
        return paths

    def find_path_helper(word, start_coor, path, paths):
        if paths: return
        if not word:
            return paths.append(path)
        if start_coor:
            pos_coors = pos_cords_gen(start_coor, path=path)
        else:
            pos_coors = [(i, j) for i in range(BOARD_ROWS) for j in range(
                BOARD_COLS)]
        for coor in pos_coors:
            square = board[coor[0]][coor[1]]
            if square == word[0:len(square)]:
                find_path_helper(word[len(square):], coor, path + [coor],
                                 paths)

    paths = []
    max_word_len = 0
    for word in words:
        len_word = len(word)
        if get_max: max_word_len = max(max_word_len, len_word)
        if len_word != n:
            continue
        word_paths = find_possible_path(word)
        if word_paths: paths.append((word, word_paths))
    if get_max: return paths, max_word_len
    return paths

def find_words_in_board(board, words):
    words_in_board = []
    i = MIN_LEN_WORD
    max_word_len = len(board)*len(board[0])
    while i < max_word_len+1:
        if i == MIN_LEN_WORD:
            paths_to_word, mx = find_length_n_words(i, board, words,
                                                                  True)
            max_word_len = min(max_word_len, mx)
        else:
            paths_to_word = find_length_n_words(i, board, words)
        for paths in paths_to_word:
            words_in_board.append(paths[0])
        i += 1
    return words_in_board

if __name__ == '__main__':
    board = [['A', 'BAG', 'A', 'BAG'],
             ['Q', 'L', 'E', 'A'],
             ['Q', 'R', 'BAG', 'G'],
             ['RA', 'Z', 'Q', 'A']]
    word_dict = {'BAG' : False, 'RAZ' : False, 'asdasd' : False}
    a = find_words_in_board(board,word_dict.keys())
    print(a)
