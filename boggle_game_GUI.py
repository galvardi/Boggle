###############################################################
# FILE : boggle_game_GUI.py
# WRITER : Raz Zeevy , raz.zeevy ,207481664, Gal Vardi, galvardi , 208935031,
# EXERCISE : intro2cs2 ex12 2021
# DESCRIPTION:
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED:
###############################################################
import tkinter as tk
from boggle_board_randomizer import randomize_board
import time
import pygame

# CONSTANTS
# FONTS
BUTTON_FONT = ('Berlin Sans FB', 15)
SMALL_FONT = ('Berlin Sans FB', 15)
LABEL_FONT = ('Berlin Sans FB', 20)
PLAYER_LABEL_FONT = ('Berlin Sans FB', 20)
MAIN_FONT = ('Berlin Sans FB', 25, 'underline')
PLAYER_ENTRY_FONT = ('Berlin Sans FB', 25)
NAME_SCREEN_FONT = ('Berlin Sans FB', 35,)
MENU_BTN_FONT = ('Berlin Sans FB', 20)
# WORD_BANK_FONT = ('Berlin Sans FB', )
# COLORS
BG_CLOCK = '#a1a1f7'
FG_CLOCK = 'white'
FG_BUTTON_FONT = 'white'
BG_BUTTON_ACTIVE = '#AFEEEE'
BG_BUTTON = 'lightblue'
BG_CLEAR_BUTTON = 'grey'
BG_CLEAR_BUTTON_ACTIVE = 'darkgrey'
BG_APPROVE_BUTTON = '#BA55D3'
BG_APPROVE_BUTTON_ACTIVE = '#EE82EE'
BG_COLOR = '#394d59'
BG_ENTER_BTN = "#fbbceb"
BG_WORD_BOX = "#929aed"
BG_PLAYER_ENTER_BTN = "#3e56b8"
FG_HIGH = "yellow"
# LAYOUT
TEXT = 'text'
TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
X = 'x'
Y = 'y'
BOTH = 'both'
NW = 'nw'
NSEW = "nsew"
#
# BOGGLE GAME
# PATH's
P_FILES_DIR = 'static/'
P_HIGHSCORE_TITLE = "scoretitle.png"
P_BG_IMG = 'newbg2.png'
P_TITLE_IMG = "title.png"
P_SOUNDTRACK = 'soundtrack.mp3'
P_GAME_BG_MUSIC = 'game_bg_music.mp3'
P_S_WORD_FOUND = 'word_found.ogg'
P_S_TIMES_UP = 'win.ogg'
P_S_WIN = 'win.ogg'
P_S_LETTER_CLICK = 'click.ogg'
P_S_BTN_CLICK = 'button_click.ogg'
# SOUNDS
S_CHANNEL = 0
S_VOLUME = 0.5
S_DURATION = 600
S_BTN_CLICK = 'button_click'
S_WIN = 'win'
S_TIMES_UP = 'time_up'
S_WORD_FOUND = 'word_found'
S_LETTER_CLICK = 'click'
# COORD's
# BOGGLE GAME
ZERO_COORD = 0
SCREEN_WIDTH = 500

Y_GAME_INFO_LABEL = 200
Y_GAME_INFO = 220
Y_GAME_BUTTONS = 250
Y_BOARD = 200
Y_GAME_BOARD = 300
X_BOARD = 100
X_SCORE = 750
Y_SCORE_LABEL = 210
Y_SCORE = 240
X_CLOCK = 720
X_CLOCK_OFFSET = 0
Y_CLOCK_OFFSET = 70
X_L_CLOCK_OFFSET = 28
Y_CLOCK_LABEL = 140
Y_PLAYER_LABEL = 180
Y_PLAYER_OFFSET = 30
Y_WORD_BANK_TEXT = 575
X_WORD_BANK_TEXT = 410
Y_WORD_BANK_BOX = 500
X_WORD_BANK_BOX = 90
Y_WORD_BANK_L = 480
X_WORD_BANK_L = 430
X_NAME_CORDS = 430
Y_NAME_CORDS_FIR = 250
Y_NAME_CORDS_SEC = 350
Y_NAME_CORDS_THIRD = 420
X_CUR_WORD = 430
X_APP_BTN = 600
X_CLEAR_BTN = 100
X_PLAYER_LABEL = 150
X_BOG_BACK_BTN = 785
Y_INIT_IMG_SEC = 100
Y_INIT_IMG_FIR = 150
X_COMP_BACK_BTN = 790
Y_COMP_BACK_BTN = 475
# SIZES
H_WORD_BANK = 3
# POPUPS
X_POP_PROMPT = 220
X_POP_OFFSET = 30
Y_POP_PROMPT = 70
X_POP_SEC_PROMPT = 215
Y_POP_SEC_PROMPT = 80
Y_POP_SEC_PROMPT_OFFSET = 30
X_POP_BTN = 230
Y_POP_BTN = 250
X_POP_BTN_OFFSET = 65
# HIGHSCORE
Y_HIGH_SCORE_T = 250
X_HIGH_SCORE_T = 240
X_HIGH_IMAGE = 200
Y_HIGH_IMAGE = 130
Y_BACK_BTN = 550
X_BACK_BTN = 760
BACK_BTN_SIZE = 10
HIGH_BACK_BTN_SIZE_BIG = 20
HIGH_BACK_BTN_SIZE_HEIGHT = 6
HIGH_BORDER_SIZE = 3
L_TABLE_PLAYER = "Player"
L_TABLE_SCORE = "Score"
L_TABLE_TIME = "Time Played"
HIGH_DIC_PLAYER = "name"
HIGH_DIC_SCORE = "score"
HIGH_DIC_TIME = "time"
EMPTY_ST = ""
COLUMN_FIR = 1
COLUMN_SEC = 2
COLUMN_THIRD = 3
# LABELS
L_APPROVE_BUTTON = 'Check'
L_CLEAR_TEXT = 'Clear'
L_SCORE = 'SCORE'
L_START_SCORE = '0'
L_WORD_BANK = 'WORDS BANK'
L_CLOCK = 'TIME'
L_NAME_SCREEN_TITLE = "Please Enter Player Name"
L_ENTER_BTN = "Let's Boggle"
L_PLAYER = "PLAYER"
L_BACK_BTN = "Back"
# POPUP
POP_ENTER_PROMPT = "Please enter a valid name"
POP_NAME_BTN = "No Problem"
POP_NAME_TITLE = "Invalid Name"
POP_VIC_TITLE = "You Won"
POP_VIC_PROMPT = "Congratz! You found all the words"
POP_SCORE = "Your Score: "
POP_END_BTN = "Main Menu"
POP_TIME_OVER = "Times Up. Your score is: "
POP_TIME_TITLE = "Time Over"
POP_TYPE_TIMEOUT = 'timeout'
POP_QUIT_TITLE = 'End Game?'
POP_QUIT_FIRST = "Are you sure you want"
POP_QUIT_SEC = "to end the current game?"
POP_YES = "Yes"
POP_NO = "No"
POP_EXIT_FIRST = "Are you sure you want"
POP_EXIT_SEC = "to exit?"
POP_EXIT_TITLE = "Exit?"
POP_EXIT_YES = "Yes"
POP_EXIT_NO = "No"
# POP TYPES
POP_TYPE_EXIT = 'exit'
POP_TYPE_WIN = 'win'
POP_TYPE_QUIT = 'quit'
POP_TYPE_NAME = 'name'
# TK BUTTONS ATTRIBUTES
STATE = 'state'
SUNKEN = 'sunken'
DISABLED = 'disabled'
GROOVE = 'groove'
RAISED = "raised"
NORMAL = 'normal'
RIDGE = 'ridge'
# CLOCK
MILL_SECS = 1000
SECONDS_FORMAT = "%S"
TEXT_COMMAND = "text"
NEW_MIN_SECONDS = "59"
END_MIN_SECONDS = "00"
ZERO_SEC = '0'
COLON = ":"
ZERO = 0
TEN = 10
ONE = 1
# MAIN MENU
MAIN_ICON_SIZE = 20
MAIN_PADX = 15
X_PLAY_BTM = 300
Y_MAIN_BTN_OFFSET_PLAY = 50
Y_MAIN_BTN_OFFSET_SCORE = 150
Y_MAIN_BTN_OFFSET_QUIT = 250
# GAME COMPONENTS
COMP_BTN_WIDTH = 10
BACK_BTN_W = 5
WORD_BANK_WIDTH = 50
WORD_BANK_WRAP = 500
L_APP_BTN = 'approve'
BTN_HEIGHT = 1
PADY = 80
# Buttons
HS = 'high_score'
PLAY = 'play'
QUIT = 'quit'
CLEAR = 'clear'
L_PLAY_BUTTON = 'Play'
L_HS_BUTTON = 'High Score'
L_QUIT_BUTTON = 'Quit'
# PATH's
P_PLAY_ICON = 'play.png'
P_HS_ICON = 'high_score.png'
P_QUIT_ICON = 'shutdown.png'
P_MSG_IMG = "msg2.png"
# COORDS's
X_POP_OFFSET = 530
Y_POP_OFFSET = 230
# SIZES
W_MENU_BUTTON = 200
H_MENU_BUTTON = 50
BUTTON_WIDTH = 15
SMALLER_BTN_SIZE = 5
SMALL_BTN_SIZE = 7


class HoverButton(tk.Button):
    """this class is used to model all the buttons in the game"""

    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        """when courser is in the button area"""
        self['background'] = self['activebackground']

    def on_leave(self, e):
        """when courser leaves the button area"""
        self['background'] = self.defaultBackground

    def on_click(self):
        """when the button is clicked"""
        self.config(relief=SUNKEN)
        self[STATE] = DISABLED


class PopUp():
    """this class is responsible for modeling all of the pop up windows"""

    def __init__(self, parent):
        self.parent = parent

    def build(self):
        """initializing the canvis and imiges for every window called"""
        self.pop = tk.Toplevel(self.parent)
        w, h = self.parent.winfo_screenwidth(), \
               self.parent.winfo_screenheight()
        self._width = min(SCREEN_WIDTH,int(w / 3))
        self._height = int(h / 3)
        self.Y_BTN = self._height - self._height // 5
        self.pop.geometry(
            "{}x{}+{}+{}"
                .format(self._width,self._height,X_POP_OFFSET,Y_POP_OFFSET))
        self.pop.overrideredirect(1)
        self.canvas = tk.Canvas(self.pop, width=self._width,
                                height=self._height, bg=BG_COLOR)
        self.bg_img = tk.PhotoImage(file=P_FILES_DIR + "msg2.png",
                                    master=self.canvas)
        self.canvas.create_image(ZERO_COORD, ZERO_COORD, image=self.bg_img,
                                 anchor=NW)
        self.canvas.pack()

    def invalid_name(self):
        """the popup window for when the player dosent enter a name"""
        self.build()
        self.pop.title(POP_NAME_TITLE)
        self.canvas.create_text(X_POP_PROMPT, Y_POP_PROMPT,
                                text=POP_ENTER_PROMPT,
                                font=LABEL_FONT)
        self.btn = HoverButton(self.canvas, text=POP_NAME_BTN,
                               font=BUTTON_FONT,
                               relief=GROOVE,
                               activebackground=BG_APPROVE_BUTTON_ACTIVE,
                               bg=BG_PLAYER_ENTER_BTN,
                               fg=FG_BUTTON_FONT, width=BUTTON_WIDTH)
        self.btn_win = self.canvas.create_window(X_POP_BTN, self.Y_BTN
                                                 , window=self.btn)

    def win(self, score):
        """the popup window for when the player wins the game"""
        self.build()
        self.pop.title(POP_VIC_TITLE)
        self.canvas.create_text(X_POP_SEC_PROMPT, Y_POP_SEC_PROMPT,
                                text=POP_VIC_PROMPT,
                                font=LABEL_FONT)
        self.canvas.create_text(X_POP_SEC_PROMPT, Y_POP_SEC_PROMPT +
                                Y_POP_SEC_PROMPT_OFFSET,
                                text=POP_SCORE + str(score),
                                font=LABEL_FONT)
        self.btn = HoverButton(self.canvas, text=POP_END_BTN,
                               font=BUTTON_FONT,
                               relief=GROOVE,
                               activebackground=BG_APPROVE_BUTTON_ACTIVE,
                               bg=BG_PLAYER_ENTER_BTN,
                               fg=FG_BUTTON_FONT, width=BUTTON_WIDTH)
        self.btn_win = self.canvas.create_window(X_POP_BTN, self.Y_BTN,
                                                 window=self.btn)

    def timeout(self, score):
        """the popup window for when the player runs out of time"""
        self.build()
        self.pop.title(POP_TIME_TITLE)
        self.canvas.create_text(X_POP_PROMPT, Y_POP_PROMPT,
                                text=POP_TIME_OVER + score,
                                font=LABEL_FONT)
        self.btn = HoverButton(self.canvas, text=POP_END_BTN,
                               font=BUTTON_FONT,
                               relief=GROOVE,
                               activebackground=BG_APPROVE_BUTTON_ACTIVE,
                               bg=BG_PLAYER_ENTER_BTN,
                               fg=FG_BUTTON_FONT, width=BUTTON_WIDTH)
        self.btn_win = self.canvas.create_window \
            (X_POP_BTN, self.Y_BTN, window=self.btn)

    def quit(self):
        """the popup window for when the player presses the exit button"""
        self.build()
        self.pop.title(POP_QUIT_TITLE)
        self.canvas.create_text(X_POP_PROMPT, Y_POP_PROMPT,
                                text=POP_QUIT_FIRST,
                                font=LABEL_FONT)
        self.canvas.create_text(X_POP_PROMPT, Y_POP_PROMPT + Y_PLAYER_OFFSET,
                                text=POP_QUIT_SEC,
                                font=LABEL_FONT)
        self.btn_yes = HoverButton(self.canvas, text=POP_YES,
                                   font=BUTTON_FONT,
                                   relief=GROOVE,
                                   activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                   bg=BG_PLAYER_ENTER_BTN,
                                   fg=FG_BUTTON_FONT, width=SMALLER_BTN_SIZE)
        self.btn_yes_win = self.canvas.create_window(X_POP_BTN +
                                                     X_POP_BTN_OFFSET,
                                                     self.Y_BTN,
                                                     window=self.btn_yes)
        self.btn_no = HoverButton(self.canvas, text=POP_NO,
                                  font=BUTTON_FONT,
                                  relief=GROOVE,
                                  activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                  bg=BG_PLAYER_ENTER_BTN,
                                  fg=FG_BUTTON_FONT, width=SMALLER_BTN_SIZE)
        self.btn_no_win = self.canvas.create_window(X_POP_BTN -
                                                    X_POP_BTN_OFFSET,
                                                    self.Y_BTN,
                                                    window=self.btn_no)

    def exit(self):
        """the popup window for when the player wishes to exit the game"""
        self.build()
        self.pop.title(POP_EXIT_TITLE)
        self.canvas.create_text(X_POP_PROMPT, Y_POP_PROMPT,
                                text=POP_EXIT_FIRST,
                                font=LABEL_FONT)
        self.canvas.create_text(X_POP_PROMPT, Y_POP_PROMPT + Y_PLAYER_OFFSET,
                                text=POP_EXIT_SEC,
                                font=LABEL_FONT)
        self.btn_yes = HoverButton(self.canvas, text=POP_EXIT_YES,
                                   font=BUTTON_FONT,
                                   relief=GROOVE,
                                   activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                   bg=BG_PLAYER_ENTER_BTN,
                                   fg=FG_BUTTON_FONT, width=SMALLER_BTN_SIZE)
        self.btn_yes_win = self.canvas.create_window(X_POP_BTN +
                                                     X_POP_BTN_OFFSET,
                                                     self.Y_BTN,
                                                     window=self.btn_yes)
        self.btn_no = HoverButton(self.canvas, text=POP_EXIT_NO,
                                  font=BUTTON_FONT,
                                  relief=GROOVE,
                                  activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                  bg=BG_PLAYER_ENTER_BTN,
                                  fg=FG_BUTTON_FONT, width=SMALL_BTN_SIZE)
        self.btn_no_win = self.canvas.create_window(X_POP_BTN -
                                                    X_POP_BTN_OFFSET,
                                                    self.Y_BTN,
                                                    window=self.btn_no)


class TimerClock(tk.Frame):
    def __init__(self, master, timer_time, **kw):
        tk.Frame.__init__(self, master=master, **kw)
        self._main_canvas = master
        self.time_ended = False
        self.clock_frame = tk.Frame(self._main_canvas)
        self.clock_label = tk.Label(self.clock_frame, text=timer_time,
                                    font=LABEL_FONT,
                                    bg=BG_CLOCK,
                                    fg=FG_CLOCK)
        self.clock_label.pack()
        self.clock_frame.pack()
        self.clock_Win = self._main_canvas.create_window(X_CLOCK +
                                                         X_CLOCK_OFFSET,
                                                         Y_GAME_INFO - Y_CLOCK_OFFSET,
                                                         anchor=NW,
                                                         window=self.clock_frame)
        clock_title = self._main_canvas.create_text(X_CLOCK + X_L_CLOCK_OFFSET,
                                                    Y_CLOCK_LABEL,
                                                    text=L_CLOCK,
                                                    font=LABEL_FONT)
        self.time_seconds = time.strftime(SECONDS_FORMAT)
        self.show_time()

    def show_time(self):
        if self.time_ended: return
        if int(time.strftime(SECONDS_FORMAT)) - int(self.time_seconds) >= 1 or \
                time.strftime(SECONDS_FORMAT) == END_MIN_SECONDS:
            self.clock_label.after(MILL_SECS, self.show_time)
            self.time_seconds = time.strftime(SECONDS_FORMAT)
            minute = int(self.clock_label.cget(TEXT)[:1])
            seconds = int(self.clock_label.cget(TEXT)[2:])
            if seconds == ZERO:
                if minute == ZERO:
                    self.time_ended = True
                    return self.timeout()
                else:
                    minute -= ONE
                    seconds = NEW_MIN_SECONDS
            elif seconds <= TEN:
                seconds = seconds - ONE
                seconds = ZERO_SEC + str(seconds)
            else:
                seconds -= ONE
            if type(seconds) is int: seconds = str(seconds)
            self.clock_label.configure(text=str(minute) + COLON + seconds)
        else:
            self.clock_label.after(MILL_SECS, self.show_time)
            return

    @staticmethod
    def timeout():
        pass


class HighScore():
    """this class models the highscore screen"""

    def __init__(self, parent, parent_canvas, high_score_data):
        self.parent = parent
        self.main_canvas = parent_canvas
        self.high_score_data = high_score_data
        self.score_img = tk.PhotoImage(file=P_FILES_DIR + P_HIGHSCORE_TITLE,
                                       master=self.main_canvas)
        self.main_canvas.create_image(X_HIGH_IMAGE, Y_HIGH_IMAGE,
                                      image=self.score_img,
                                      anchor=NW)
        self.back_btn = HoverButton(self.main_canvas, text=L_BACK_BTN,
                                    font=BUTTON_FONT,
                                    relief=GROOVE,
                                    activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                    bg=BG_PLAYER_ENTER_BTN,
                                    fg=FG_BUTTON_FONT,
                                    width=BACK_BTN_SIZE)
        self.back_btn.pack()
        self.btn_win = self.main_canvas.create_window(X_BACK_BTN, Y_BACK_BTN,
                                                      window=self.back_btn)
        self.score_board_label = tk.Label(self.main_canvas,
                                          text=EMPTY_ST, width=
                                          HIGH_BACK_BTN_SIZE_BIG, height=
                                          HIGH_BACK_BTN_SIZE_HEIGHT,
                                          font=NAME_SCREEN_FONT,
                                          fg=FG_HIGH, bg=BG_CLOCK,
                                          borderwidth=HIGH_BORDER_SIZE,
                                          relief=SUNKEN)
        self.score_board_label.pack()
        self._draw_row(L_TABLE_PLAYER, L_TABLE_SCORE, L_TABLE_TIME, 1,
                       LABEL_FONT)
        self._draw_table()

    def _draw_row(self, player, score, time, row, font):
        """this function add a new row to the highscore board"""
        self.score_board_label_player = tk.Label(self.score_board_label,
                                                 text=player,
                                                 font=font,
                                                 fg=FG_HIGH, bg=BG_CLOCK,
                                                 borderwidth=HIGH_BORDER_SIZE,
                                                 relief=SUNKEN)
        self.score_board_label_player.grid(row=row, column=COLUMN_FIR,
                                           sticky=NSEW)

        self.score_board_label_score = tk.Label(self.score_board_label,
                                                text=score,
                                                font=font,
                                                fg=FG_HIGH, bg=BG_CLOCK,
                                                borderwidth=HIGH_BORDER_SIZE,
                                                relief=SUNKEN)
        self.score_board_label_score.grid(row=row, column=COLUMN_SEC,
                                          sticky=NSEW)
        self.score_board_label_time = tk.Label(self.score_board_label,
                                               text=time,
                                               font=font,
                                               fg=FG_HIGH, bg=BG_CLOCK,
                                               borderwidth=HIGH_BORDER_SIZE,
                                               relief=SUNKEN)
        self.score_board_label_time.grid(row=row, column=COLUMN_THIRD,
                                         sticky=NSEW)
        self.main_canvas.create_window(X_HIGH_SCORE_T, Y_HIGH_SCORE_T,
                                       window=self.score_board_label,
                                       anchor=NW)

    def _draw_table(self):
        """this function generates the entire highscore table from the data"""
        for i, data in enumerate(self.high_score_data):
            self._draw_row(data[HIGH_DIC_PLAYER], data[HIGH_DIC_SCORE],
                           data[HIGH_DIC_TIME],
                           [i + 2],
                           SMALL_FONT)


class NameScreen():
    """this class models the screen for the player to enter their name"""

    def __init__(self, parent, parent_canvas):
        self.parent = parent
        self.main_canvas = parent_canvas
        self.title_label = tk.Label(self.main_canvas,
                                    text=L_NAME_SCREEN_TITLE,
                                    font=NAME_SCREEN_FONT,
                                    fg=FG_HIGH, bg=BG_CLOCK,
                                    borderwidth=HIGH_BORDER_SIZE,
                                    relief=RAISED)
        self.title_label.pack()
        self.main_canvas.create_window(X_NAME_CORDS, Y_NAME_CORDS_FIR,
                                       window=self.title_label)
        self.entry_box = tk.Entry(self.main_canvas, width=BACK_BTN_SIZE,
                                  font=PLAYER_ENTRY_FONT)
        self.entry_box.pack()
        self.box_win = self.main_canvas.create_window(X_NAME_CORDS,
                                                      Y_NAME_CORDS_SEC,
                                                      window=self.entry_box)
        self.entry_btn = HoverButton(self.main_canvas, text=L_ENTER_BTN,
                                     font=BUTTON_FONT,
                                     relief=GROOVE,
                                     activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                     bg=BG_PLAYER_ENTER_BTN,
                                     fg=FG_BUTTON_FONT, width=BACK_BTN_SIZE)
        self.entry_btn.pack()
        self.btn_win = self.main_canvas.create_window(X_NAME_CORDS,
                                                      Y_NAME_CORDS_THIRD,
                                                      window=self.entry_btn)
        self.back_btn = HoverButton(self.main_canvas, text=L_BACK_BTN,
                                    font=BUTTON_FONT,
                                    relief=GROOVE,
                                    activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                    bg=BG_PLAYER_ENTER_BTN,
                                    fg=FG_BUTTON_FONT, width=BACK_BTN_SIZE)
        self.back_btn.pack()
        self.btn_win = self.main_canvas.create_window(X_BACK_BTN, Y_BACK_BTN,
                                                      window=self.back_btn)

    def get_name(self):
        """this function returns the name entered by the player"""
        return self.entry_box.get()


class MainMenu():
    """this class models the main menu of the game"""

    def __init__(self, parent, parent_canvas):
        self.parent = parent
        self.buttons = {}
        self.main_canvas = parent_canvas
        self._init_buttons()

    def _init_buttons(self):
        """this function initializes and places all the buttons"""
        self.play_icon = tk.PhotoImage(file=P_FILES_DIR + P_PLAY_ICON)
        self.play_icon = self.play_icon.subsample(MAIN_ICON_SIZE,
                                                  MAIN_ICON_SIZE)
        play_btn = HoverButton(
            self.main_canvas, text=L_PLAY_BUTTON, font=MENU_BTN_FONT,
            relief=GROOVE, activebackground=BG_BUTTON_ACTIVE,
            bg=BG_BUTTON, padx=MAIN_PADX, image=self.play_icon, compound=LEFT,
            fg=FG_BUTTON_FONT, width=W_MENU_BUTTON, height=H_MENU_BUTTON)
        play_btn.pack(fill=X, expand=True)
        self.buttons[PLAY] = play_btn
        self.high_score_icon = tk.PhotoImage(file=P_FILES_DIR + P_HS_ICON)
        self.high_score_icon = \
            self.high_score_icon.subsample(MAIN_ICON_SIZE, MAIN_ICON_SIZE)
        high_score_btn = HoverButton(
            self.main_canvas, text=L_HS_BUTTON, font=MENU_BTN_FONT,
            relief=GROOVE, activebackground=BG_BUTTON_ACTIVE,
            bg=BG_BUTTON, padx=MAIN_PADX, image=self.high_score_icon,
            compound=LEFT,
            fg=FG_BUTTON_FONT, width=W_MENU_BUTTON, height=H_MENU_BUTTON)
        high_score_btn.pack(fill=X, expand=True)
        self.buttons[HS] = high_score_btn
        self.quit_icon = tk.PhotoImage(file=P_FILES_DIR + P_QUIT_ICON)
        self.quit_icon = self.quit_icon.subsample(MAIN_ICON_SIZE,
                                                  MAIN_ICON_SIZE)
        quit_btn = HoverButton(self.main_canvas, text=L_QUIT_BUTTON,
                               font=MENU_BTN_FONT, relief=GROOVE,
                               activebackground=BG_BUTTON_ACTIVE,
                               bg=BG_BUTTON, padx=MAIN_PADX,
                               image=self.quit_icon, compound=LEFT,
                               height=H_MENU_BUTTON, fg=FG_BUTTON_FONT,
                               width=W_MENU_BUTTON)
        quit_btn.pack(fill=X, expand=True)
        self.buttons[QUIT] = quit_btn
        play_win = self.main_canvas.create_window(
            X_PLAY_BTM, Y_BOARD + Y_MAIN_BTN_OFFSET_PLAY, anchor=NW,
            window=play_btn)
        high_score_win = self.main_canvas.create_window(
            X_PLAY_BTM, Y_BOARD + Y_MAIN_BTN_OFFSET_SCORE, anchor=NW,
            window=high_score_btn)
        quit_win = self.main_canvas.create_window(
            X_PLAY_BTM, Y_BOARD + Y_MAIN_BTN_OFFSET_QUIT, anchor=NW,
            window=quit_btn)


class GameComponents:
    """this class models the main screen of the game, where you play the
    game"""
    CUR_WORD_DEF = '____________'

    def __init__(self, parent, board, game_time, player_name,
                 parent_canvas, screen_width):
        self._parent = parent
        self.buttons = {}
        self._board = board
        self.game_time = game_time
        self._main_canvas = parent_canvas
        self.player_name = player_name
        self.X_BOARD = screen_width // 5
        self.X_WORD_BANK = screen_width // 6
        self._init_components()

    def _init_components(self):
        """this function initializes and places all of the different
        components which are on the screen"""
        # score
        self._score_frame = tk.Frame(self._parent)
        self.score_txt_num = self._main_canvas.create_text(X_SCORE,
                                                           Y_SCORE,
                                                           text=L_START_SCORE,
                                                           font=LABEL_FONT,
                                                           fill=FG_CLOCK)
        score_title_txt = self._main_canvas.create_text(X_SCORE,
                                                        Y_SCORE_LABEL,
                                                        text=L_SCORE,
                                                        font=LABEL_FONT)
        # board
        self._board_frame = tk.Frame(self._parent)
        self._init_board(self._board_frame)
        self._board_frame.pack(fill=BOTH, expand=True)
        self._board_frame_win = self._main_canvas.create_window(self.X_BOARD,
                                                                Y_GAME_BOARD,
                                                                anchor=NW,
                                                                window=self._board_frame)
        # cur word
        self._cur_word_txt = self._main_canvas.create_text(X_CUR_WORD,
                                                           Y_GAME_INFO_LABEL,
                                                           text=self.CUR_WORD_DEF,
                                                           font=MAIN_FONT)
        # approve button
        self._approve_btn_frame = tk.Frame(self._parent)
        self._init_approve_button(self._approve_btn_frame)
        self._main_canvas.create_window(X_APP_BTN, Y_GAME_BUTTONS, anchor=NW,
                                        window=self._approve_btn_frame)
        # clear button
        self._clear_button_frame = tk.Frame(self._parent)
        self._init_clear_button(self._clear_button_frame)
        self._main_canvas.create_window(X_CLEAR_BTN, Y_GAME_BUTTONS,
                                        anchor=NW,
                                        window=self._clear_button_frame)
        # words bank
        self._init_word_bank()
        # clock
        self.clock = TimerClock(self._main_canvas, self.game_time)

        # player
        self._main_canvas.create_text(X_PLAYER_LABEL, Y_PLAYER_LABEL,
                                      text=L_PLAYER, font=PLAYER_LABEL_FONT)
        self._main_canvas.create_text(X_PLAYER_LABEL, Y_PLAYER_LABEL +
                                      Y_PLAYER_OFFSET,
                                      text=self.player_name,
                                      font=LABEL_FONT, fill=FG_CLOCK)
        # back button
        self.back_btn = HoverButton(self._main_canvas, text=L_BACK_BTN,
                                    font=BUTTON_FONT,
                                    relief=GROOVE,
                                    activebackground=BG_APPROVE_BUTTON_ACTIVE,
                                    bg=BG_PLAYER_ENTER_BTN,
                                    fg=FG_BUTTON_FONT, width=BACK_BTN_W)
        self.back_btn.pack()
        self.btn_win = self._main_canvas.create_window(X_COMP_BACK_BTN,
                                                       Y_COMP_BACK_BTN,
                                                       window=self.back_btn)
        self.buttons['back'] = self.back_btn

    def _init_word_bank(self):
        """initializes and placed the word bank on the screen"""
        self._word_bank_frame = tk.Frame(self._main_canvas)
        self._words_bank_label = tk.Label(self._word_bank_frame,
                                          width=WORD_BANK_WIDTH,
                                          height=H_WORD_BANK, text=EMPTY_ST,
                                          font=SMALL_FONT, bg=BG_WORD_BOX,
                                          fg=FG_BUTTON_FONT, \
                                          borderwidth=HIGH_BORDER_SIZE,
                                          justify=LEFT,
                                          relief=RIDGE,
                                          wraplength=WORD_BANK_WRAP)
        self._words_bank_label.pack()
        self.word_bank_box_win = self._main_canvas.create_window(
            self.X_WORD_BANK,
            Y_WORD_BANK_BOX,
            anchor=NW,
            window=self._word_bank_frame)
        self._main_canvas.create_text(X_WORD_BANK_L, Y_WORD_BANK_L,
                                      text=L_WORD_BANK,
                                      font=LABEL_FONT)
        self.word_bank = self._main_canvas.create_text(X_WORD_BANK_TEXT,
                                                       Y_WORD_BANK_TEXT,
                                                       text=EMPTY_ST,
                                                       font=SMALL_FONT)

    def _init_board(self, frame):
        """initializes and placed the game board on the screen"""
        self._board_frame = frame
        self._board_frame.pack(pady=(PADY, ZERO_COORD))
        self._init_board_buttons()

    def _init_approve_button(self, frame):
        """initializes and placed the approve button on the screen"""
        approve_button = HoverButton(
            frame, text=L_APPROVE_BUTTON, font=BUTTON_FONT, relief=GROOVE,
            activebackground=BG_APPROVE_BUTTON_ACTIVE, bg=BG_APPROVE_BUTTON,
            fg=FG_BUTTON_FONT, width=COMP_BTN_WIDTH)
        self.buttons[L_APP_BTN] = approve_button
        approve_button.pack()

    def _init_clear_button(self, frame):
        """initializes and placed the clear button on the screen"""
        clear_button = HoverButton(
            frame, text=L_CLEAR_TEXT, font=BUTTON_FONT, relief=GROOVE,
            activebackground=BG_CLEAR_BUTTON_ACTIVE, bg=BG_CLEAR_BUTTON,
            fg=FG_BUTTON_FONT, width=COMP_BTN_WIDTH)
        self.buttons[CLEAR] = clear_button
        clear_button.pack()

    def _init_board_buttons(self):
        """initializes and placed the board buttons on the screen"""
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                button = HoverButton(self._board_frame, text=self._board[
                    i][j],
                                     font=BUTTON_FONT,
                                     relief=GROOVE,
                                     activebackground=BG_BUTTON_ACTIVE,
                                     bg=BG_BUTTON,
                                     fg=FG_BUTTON_FONT,
                                     width=COMP_BTN_WIDTH, height=BTN_HEIGHT)
                self.buttons[(i, j)] = button
                button.grid(row=i, column=j)

    def reset_buttons(self):
        """this function resets the button's states"""
        self.update_current_word(GameComponents.CUR_WORD_DEF)
        for button in self.buttons.values():
            button.config(relief=GROOVE)
            button[STATE] = NORMAL

    def update_word_bank(self, word_bank_txt):
        """this function updates the word bank with new words"""
        self._words_bank_label[TEXT] = word_bank_txt

    def update_current_word(self, word):
        """this function updates the current word"""
        self._main_canvas.itemconfig(self._cur_word_txt, text=word)

    def update_score(self, score):
        """this function updates the players score"""
        self._main_canvas.itemconfig(self.score_txt_num, text=score)


class BoggleGUI:
    """this class is the at the highest level and it is in charge of all
    the UI components"""

    def __init__(self):
        self.root = tk.Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self._width = min(int(w / 1.5),853)
        self._height = min(int(h / 1.2),600)
        self.root.geometry(
            "{}x{}+{}+{}".format(self._width,self._height,
                                 int(w / 5),int(h / 12)))
        self.root.resizable(False,False)
        self._main_canvas = None
        self.pop = PopUp(self.root)
        self.change_tune = True
        pygame.init()

    def play_soundtrack(self, tune_path):
        """this function is responsible to play the game's bg music"""
        pygame.mixer.music.load(P_FILES_DIR + tune_path)
        pygame.mixer.music.play()

    def play_sound(self, sound_type):
        """this function is responsible to play the game's sounds"""
        duration = S_DURATION
        volume = S_VOLUME
        s_chan = S_CHANNEL
        if sound_type == S_LETTER_CLICK:
            path = P_FILES_DIR + P_S_LETTER_CLICK
        elif sound_type == S_WORD_FOUND:
            path = P_FILES_DIR + P_S_WORD_FOUND
        elif sound_type == S_BTN_CLICK:
            path = P_FILES_DIR + P_S_BTN_CLICK
        elif sound_type == S_TIMES_UP:
            duration = 2000
            path = P_FILES_DIR + P_S_TIMES_UP
        elif sound_type == S_WIN:
            duration = 2000
            path = P_FILES_DIR + P_S_WIN
        pygame.mixer.Channel(s_chan).set_volume(volume)
        pygame.mixer.Channel(s_chan).play(pygame.mixer.Sound(path),
                                     maxtime=duration)

    def pop_msg(self, msg_type=None):
        """this function is responsible for calling creating the various
        popup windows"""
        self.pop_up = PopUp(self._main_canvas)
        if msg_type == POP_TYPE_NAME:
            self.pop_up.invalid_name()
        elif msg_type == POP_TYPE_WIN:
            self.pop_up.win(self.game_comp._main_canvas.itemcget(
                self.game_comp.score_txt_num, TEXT_COMMAND))
        elif msg_type == POP_TYPE_QUIT:
            self.pop_up.quit()
        elif msg_type == POP_TYPE_TIMEOUT:
            self.pop_up.timeout(self.game_comp._main_canvas.itemcget(
                self.game_comp.score_txt_num, TEXT_COMMAND))
        elif msg_type == POP_TYPE_EXIT:
            self.pop_up.exit()

    def pop_msg_remove(self):
        """this function closes the pop up window
        according to the players input"""
        self.play_sound(S_BTN_CLICK)
        self.pop_up.canvas.destroy()
        self.pop_up.pop.destroy()
        self.pop_up = None

    def remove(self):
        """this function destroys the classes canvas"""
        self._main_canvas.destroy()
        self._main_canvas = None

    def start_game(self, board, game_time, player_name):
        """this function is called when the player begins playing the game"""
        self.play_soundtrack(P_GAME_BG_MUSIC)
        self.change_tune = True
        self._main_canvas = tk.Canvas(self.root, width=self._width,
                                      height=self._height, bg=BG_COLOR)
        self._init_canvas_imgs()
        self._main_canvas.pack()
        self.game_comp = GameComponents(self._main_canvas, board, game_time,
                                        player_name, self._main_canvas, self._width)

    def player_name_screen(self):
        """this function is called to init the player name screen once the
        player presses play"""
        self._main_canvas = tk.Canvas(self.root, width=self._width,
                                      height=self._height, bg=BG_COLOR)
        self._init_canvas_imgs()
        self._main_canvas.pack()
        self.name_screen = NameScreen(self.root, self._main_canvas)

    def go_main_menu(self):
        """this function is called to init the games main menu"""
        if self.change_tune: self.play_soundtrack(P_SOUNDTRACK)
        self.change_tune = False
        self._main_canvas = tk.Canvas(self.root, width=self._width,
                                      height=self._height, bg=BG_COLOR)
        self._init_canvas_imgs_main_menu()
        self._main_canvas.pack(expand=True,fill=BOTH)
        self.main_menu = MainMenu(self.root, self._main_canvas)

    def go_high_score(self, high_score_data):
        """this function is called to init the highscore screen once the
                player presses highscore"""
        self._main_canvas = tk.Canvas(self.root, width=self._width,
                                      height=self._height, bg=BG_COLOR)
        self.init_canvas_imgs_high_score()
        self.init_canvas_imgs_high_score()
        self._main_canvas.pack()
        self.high_score = HighScore(self.root, self._main_canvas,
                                    high_score_data)

    def init_canvas_imgs_high_score(self):
        """this function is called to init the images which are in the
        highscore screen"""
        self.bg_img = tk.PhotoImage(file=P_FILES_DIR + P_BG_IMG,
                                    master=self._main_canvas)
        self._main_canvas.create_image(ZERO_COORD, ZERO_COORD,
                                       image=self.bg_img, \
                                       anchor=NW)

    def _init_canvas_imgs_main_menu(self):
        """this function is called to init the images which are in the
                main menu screen"""
        self.bg_img = tk.PhotoImage(file=P_FILES_DIR + P_BG_IMG,
                                    master=self._main_canvas)
        self.title_img = tk.PhotoImage(file=P_FILES_DIR + P_TITLE_IMG,
                                       master=self._main_canvas)
        self._main_canvas.create_image(ZERO_COORD, ZERO_COORD,
                                       image=self.bg_img, anchor=NW)
        self._main_canvas.create_image(self._width / 2, Y_INIT_IMG_FIR,
                                       image=self.title_img)

    def _init_canvas_imgs(self):
        """this function is called to init the images which are in the
                background most of the game"""
        self.bg_img = tk.PhotoImage(file=P_FILES_DIR + P_BG_IMG,
                                    master=self._main_canvas)
        self.title_img = tk.PhotoImage(file=P_FILES_DIR + P_TITLE_IMG,
                                       master=self._main_canvas)
        self._main_canvas.create_image(ZERO_COORD, ZERO_COORD,
                                       image=self.bg_img, anchor=NW)
        self._main_canvas.create_image(self._width / 2, Y_INIT_IMG_SEC,
                                       image=self.title_img)

    def run(self):
        """this function is called to start dunning the game"""
        self.root.mainloop()


if __name__ == '__main__':
    game_board = randomize_board()
    boggle_game = BoggleGUI(game_board)
    boggle_game.run()
