###############################################################
# FILE : boggle_controller.py
# WRITER : Raz Zeevy , raz.zeevy ,207481664, Gal Vardi, galvardi, 208935031
# EXERCISE : intro2cs2 ex12 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED:
###############################################################ASDS

from boggle_game_GUI import BoggleGUI
from boggle_logic import is_valid_path, find_words_in_board
# from sandbox import BoggleGUI
from boggle_board_randomizer import randomize_board
import time
from datetime import datetime

# CONSTANTS
# GAME
GAME_TIME = '3:00'
TIMEOUT = 'timeout'
WIN = 'win'
EXIT = 'exit'
# PATH's
P_BOGGLE_DICT = 'boggle_dict.txt'
# TK GAME ATTRIBUTES
COMMAND = 'command'
TEXT = 'text'
# Buttons
APPROVE = 'approve'
CLEAR = 'clear'
BACK = 'back'
# KEYS
ESCAPE = '<Escape>'
ENTER = '<Return>'
# ROUTING
MENU = 'main_menu'
HS = 'high_score'
PLAY = 'play'
NAME_CHOOSE = 'name'
QUIT = 'quit'
# POP_UPS
POP_TYPE_TIMEOUT = 'timeout'
POP_TYPE_WIN = 'win'
POP_TYPE_QUIT = 'quit'
POP_TYPE_NAME = 'name'
POP_TYPE_EXIT = 'exit'
# HIGH_SCORE
HIGH_SCORE_NUM = 8
# SOUNDS
S_WIN = 'win'
S_TIMES_UP = 'time_up'
S_WORD_FOUND = 'word_found'
S_LETTER_CLICK = 'click'
S_BTN_CLICK = 'button_click'

class BoggleGame:
    """the class of the boggle game itself and all the data"""
    def __init__(self, gui, board, player_name, word_dict=None):
        self.gui = gui
        self.board = board
        self.cur_word = ''
        self.word_dict = word_dict
        self.player_name = player_name
        self.cur_path = []
        self.score = 0
        self.word_bank = []

    def start(self):
        """starts the boggle game"""
        start_time = time.time()
        self.gui.start_game(self.board, GAME_TIME, self.player_name)
        self.word_dict = self.word_dict if self.word_dict is not None else \
            self._get_words()
        for coor, button in self.gui.game_comp.buttons.items():
            button[COMMAND] = self._create_button_action(coor, button)
        self.gui.game_comp.clock.timeout = self.timeout
        self.all_words = len(self.word_dict)
        self.found_words = len(self.word_bank)

    def _create_button_action(self, name, button):
        """creating all the buttons actions for the GUI"""
        def letter_action():
            coor = name
            self.cur_path.append(coor)
            if not is_valid_path(self.cur_path):
                self._reset_word_selection()
                self.cur_path.append(coor)
            cur_word = self.cur_word + button[TEXT]
            self._update_current_word(cur_word)
            button.on_click()

        def approve_action():
            if self.cur_word in self.word_dict and \
                    not self.word_dict[self.cur_word]:
                self._update_word_bank()
                self._update_score()
                self._reset_word_selection()
                self._check_win()

        if name == APPROVE:
            return approve_action
        if name == CLEAR:
            return self._reset_word_selection
        if name == BACK:
            return self.back
        return letter_action

    def _reset_word_selection(self):
        """commanding the gui to reset the word selection"""
        self.cur_word = ''
        self.gui.game_comp.reset_buttons()
        self.cur_path = []

    def _update_current_word(self, word):
        """updates the word according to user selection"""
        self.gui.play_sound(S_LETTER_CLICK)
        self.cur_word = word
        self.gui.game_comp.update_current_word(word)

    def _update_score(self):
        """updates the score"""
        self.score += len(self.cur_word) ** 2
        self.gui.game_comp.update_score(self.score)

    def _update_word_bank(self):
        """updates the word bank after the user found a new word"""
        self.gui.play_sound(S_WORD_FOUND)
        self.word_bank.append(self.cur_word)
        self.found_words += 1
        self.word_dict[self.cur_word] = True
        word_bank_text = ', '.join(self.word_bank)
        self.gui.game_comp.update_word_bank(word_bank_text)

    def _get_words(self):
        """get all the possible words that are in the board"""
        with open(P_BOGGLE_DICT, 'r') as f:
            words = [word.strip('\n') for word in f]
        in_board_words = words
        # in_board_words = find_words_in_board(self.board, words)
        return {word: False for word in in_board_words}

    def _check_win(self):
        """Checks if all the words are found"""
        if self.found_words == self.all_words:
            self.win_game()

    @staticmethod
    def win_game(self):
        """this function is called when the game is won"""
        pass

    @staticmethod
    def back():
        """this function is called when the user clicks back \ escape """
        pass

    @staticmethod
    def timeout():
        """this function is called when the game's time is up"""
        pass


class HighScore():
    """The class of the high score page and its methods"""
    def __init__(self):
        self.data = []
        self.add_score('Tiger', 15)
        self.add_score('WorDinosaur', 10)
        self.add_score('TheSchlez', 5)

    def add_score(self, name, score):
        """adds a new score to the board"""
        time_sig = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.data.append(dict(
            name=name,
            score=score,
            time=time_sig
        ))

    def get_top_score(self):
        """get best n scores to show in the highscore page"""
        return sorted(self.data, key=lambda a: a['score'],
                      reverse=True)[:HIGH_SCORE_NUM]


class BoggleController:
    """Thats the main class that governs the entire app, routing and
    features"""
    def __init__(self):
        self._gui = BoggleGUI()
        self.high_score_data = HighScore()
        self._main_menu()
        # self._high_score()
        # self._gui.player_name_screen()
        # self._start_new_game('raz')
        # self._gui.root.bind(ESCAPE, quit)

    def _main_menu(self):
        """calls the main menu page"""
        self._gui.go_main_menu()
        self._gui.root.bind(ESCAPE, lambda e: self._quit())
        for key, button in self._gui.main_menu.buttons.items():
            if key == PLAY:
                button[COMMAND] = lambda: self._routing(NAME_CHOOSE)
            if key == HS:
                button[COMMAND] = lambda: self._routing(HS)
            if key == QUIT:
                button[COMMAND] = lambda: self._quit()

    def _routing(self, target, *args):
        """this function governs all the routing"""
        self._gui.play_sound(S_BTN_CLICK)
        self._gui.root.unbind(ENTER)
        self._gui.root.unbind(ESCAPE)
        if target == HS:
            self._gui.remove()
            self._high_score()
        if target == NAME_CHOOSE:
            self._gui.remove()
            self._name_choose()
        if target == PLAY:
            self._gui.remove()
            self._start_new_game(*args)
        if target == MENU:
            self._gui.remove()
            self._main_menu()

    def _high_score(self):
        """calls the high score page"""
        self._gui.root.bind(ESCAPE, lambda e: self._routing(MENU))
        self._gui.go_high_score(self.high_score_data.get_top_score())
        self._gui.high_score.back_btn[COMMAND] = lambda: self._routing(MENU)

    def _pop_up_msg(self, msg_type):
        """calls all the pop_up messages"""
        def quit_game():
            """quits the game"""
            self.high_score_data.add_score(self.game.player_name,
                                           self.game.score)
            self._gui.pop_msg_remove()
            self._routing(MENU)

        self._gui.pop_msg(msg_type)
        if msg_type == NAME_CHOOSE:
            self._gui.pop_up.btn[COMMAND] = self._gui.pop_msg_remove
        if msg_type == QUIT:
            self._gui.pop_up.btn_yes[COMMAND] = quit_game
            self._gui.pop_up.btn_no[COMMAND] = self._gui.pop_msg_remove
        if msg_type == TIMEOUT:
            self._gui.pop_up.btn[COMMAND] = quit_game
        if msg_type == WIN:
            self._gui.pop_up.btn[COMMAND] = quit_game
        if msg_type == EXIT:
            self._gui.pop_up.btn_yes[COMMAND] = lambda: exit()
            self._gui.pop_up.btn_no[COMMAND] = self._gui.pop_msg_remove

    def _name_choose(self):
        """calls the name choose screen"""
        def verify_name(name):
            """check is the name is not empty"""
            return name != ''

        def enter_name():
            """gets the name entry to start the game"""
            name = self._gui.name_screen.get_name()
            self._gui.play_sound(S_BTN_CLICK)
            if verify_name(name):
                self._routing(PLAY, name)
            else:
                self._pop_up_msg(POP_TYPE_NAME)

        self._gui.player_name_screen()
        self._gui.root.bind(ESCAPE, lambda e: self._routing(MENU))
        self._gui.root.bind(ENTER, lambda e: enter_name())
        self._gui.name_screen.entry_btn[COMMAND] = enter_name
        self._gui.name_screen.back_btn[COMMAND] = lambda: self._routing(MENU)

    def _start_new_game(self, name):
        """calls the boggle game page and starts it"""
        board = randomize_board()
        self.game = BoggleGame(self._gui, board, name)
        self.game.win_game = self._static_game_methods(WIN)
        self.game.back = self._static_game_methods(QUIT)
        self.game.timeout = self._static_game_methods(TIMEOUT)
        self._gui.root.bind(ESCAPE,
                            lambda e: self._static_game_methods(QUIT)())
        self.game.start()

    def _static_game_methods(self, func_name):
        """this function modify (and create) the static game functions that
        are ouside of the game's class scope"""
        def win():
            """what happend when the game is won"""
            self._gui.play_sound(S_WIN)
            self._pop_up_msg(POP_TYPE_WIN)

        def quit():
            """what happens when the quit option is selected by the user"""
            self._pop_up_msg(POP_TYPE_QUIT)

        def timeout():
            """what happend when there is a timeout"""
            self._gui.play_sound(S_TIMES_UP)
            self._pop_up_msg(POP_TYPE_TIMEOUT)

        if func_name == QUIT:
            return quit
        if func_name == WIN:
            return win
        if func_name == TIMEOUT:
            return timeout

    def run(self):
        """runs the app"""
        self._gui.run()

    def _quit(self):
        """quits the app"""
        self._pop_up_msg(POP_TYPE_EXIT)


if __name__ == '__main__':
    boggle = BoggleController()
    boggle.run()
