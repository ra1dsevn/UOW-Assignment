import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import random
import os
import threading
import time
import pyttsx3
from queue import Queue, Empty
from PIL import ImageTk, Image
import tkinter as tk
from queue import Queue
import threading

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.top_score_file = "TopScore.txt"
        self.speech_queue = Queue()
        self.speech_thread = threading.Thread(target=self.process_speech_queue)
        self.speech_thread.daemon = True
        self.speech_thread.start()

        # Load the background image
        background_image = Image.open("pic.jpg")
        background_photo = ImageTk.PhotoImage(background_image)

        # Create the Label component of the background image
        background_label = tk.Label(root, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_photo

        # Read top score
        self.top_scorer, self.top_score = self.read_top_score()

        # Top score label
        self.top_score_label = tk.Label(root, text=f"Top Score: {self.top_score} by {self.top_scorer}", font='normal 12 bold')
        self.top_score_label.grid(row=0, column=0, columnspan=3)

        # Game board buttons
        self.board_buttons = [tk.Button(root, text='', font='normal 20 bold', height=2, width=4,
                                        command=lambda i=i: self.on_button_click(i)) for i in range(9)]
        for i, button in enumerate(self.board_buttons):
            row, col = divmod(i, 3)
            button.grid(row=row + 1, column=col)

        # Info label
        self.info_label = tk.Label(root, text="Game 1", font='normal 15 bold')
        self.info_label.grid(row=4, column=0, columnspan=3)

        # Score label
        self.score_label = tk.Label(root, text="USER: 0  COMPUTER: 0", font='normal 15 bold')
        self.score_label.grid(row=5, column=0, columnspan=3)

        # Start button
        self.start_button = tk.Button(root, text='Start Game', command=self.start_game)
        self.start_button.grid(row=6, column=0, columnspan=3)

        # Game state
        self.user_score = 0
        self.computer_score = 0
        self.game_count = 1
        self.game_started = False

        self.first_move = random.choice(['USER', 'COMPUTER'])
        self.reset_game()

    def reset_game(self):
        self.board = [''] * 9
        self.game_over = False
        for button in self.board_buttons:
            button.config(text='', state=tk.NORMAL)

        self.current_turn = self.first_move

        if self.current_turn == 'COMPUTER':
            self.computer_move()
        self.game_started = False
        prompt_thread = threading.Thread(target=self.repeat_prompt)
        prompt_thread.start()


    def start_game(self):
        self.game_started = True

        # If it is not the first game, choose a different first hand at random
        if self.game_count > 1:
            available_choices = ['USER', 'COMPUTER']
            available_choices.remove(self.first_move)
            self.first_move = random.choice(available_choices)

        if self.game_count > 5 or (self.user_score >= 3 or self.computer_score >= 3):
            self.check_high_score()
            self.user_score = 0
            self.computer_score = 0
            self.game_count = 1
        self.reset_game()
        self.update_info_label()
        self.update_score_label()

    def on_button_click(self, i):
        if self.game_over or self.board[i]:
            return
        self.board[i] = '*'
        self.board_buttons[i].config(text='*', foreground='red', font='100px')
        if self.check_winner():
            self.end_game('USER')
        else:
            self.current_turn = 'COMPUTER'
            self.computer_move()
            threading.Thread(target=lambda: self.play_sound("Your Move")).start()
            time.sleep(3)

    def computer_move(self):
        empty_cells = [i for i, x in enumerate(self.board) if x == '']
        if not empty_cells:
            self.end_game('DRAW')
            return
        choice = random.choice(empty_cells)
        self.board[choice] = '#'
        self.board_buttons[choice].config(text='#', foreground='blue', font='100px')
        if self.check_winner():
            self.end_game('COMPUTER')
        else:
            self.current_turn = 'USER'
            threading.Thread(target=lambda: self.play_sound("My Move")).start()
            time.sleep(3)

    def check_winner(self):
        for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != '':
                return True
        return False

    def highlight_winner(self, a, b, c):
        for index in [a, b, c]:
            self.board_buttons[index].config(bg='green', fg='white')

    def end_game(self, winner):
        message = "Game over"
        if winner == 'USER':
            message += ", You win"
        elif winner == 'COMPUTER':
            message += ", I win"
        else:
            message += ", Draw"
            message += ", Tie, please start the next game!"
        self.play_sound(message)
        self.game_over = True
        self.game_count += 1
        self.update_info_label()
        self.update_score_label()
        self.current_turn = 'USER' if self.current_turn == 'COMPUTER' else 'COMPUTER'  # Exchange first hand
        self.play_sound("Thanks for playing")

    def update_info_label(self):
        self.info_label.config(text=f"Game {self.game_count}")

    def update_score_label(self):
        self.score_label.config(text=f"USER: {self.user_score}  COMPUTER: {self.computer_score}")

    def read_top_score(self):
        if os.path.exists(self.top_score_file):
            with open(self.top_score_file, 'r') as file:
                data = file.readline().split(',')
                if len(data) == 2:
                    return data[0], int(data[1])
        return 'None', 0

    def check_high_score(self):
        if self.user_score > self.top_score:
            self.play_sound("Congratulations, you beat the top score")
            name = tk.simpledialog.askstring("New High Score!", "Enter your name:")
            if name:
                with open(self.top_file, 'w') as file:
                    file.write(f"{name},{self.user_score}")
                self.top_score = self.user
                self.top_scorer = name
                self.update_top_score_label

    def update_top_score_label(self):
        self.top_score_label.config(text=f"Top Score: {self.top_score} by {self.top_scorer}")

    def play_sound(self, text):
        self.speech_queue.put(text)

    def process_speech_queue(self):
        engine = pyttsx3.init()
        while True:
            try:
                text = self.speech_queue.get(block=True)
                engine.say(text)
                engine.runAndWait()
            except Empty:
                pass

    def reset_game(self):
        self.board = [''] * 9
        self.game_over = False
        for button in self.board_buttons:
            button.config(text='', state=tk.NORMAL)
        self.current_turn = self.first_move
        if self.current_turn == 'COMPUTER':
            self.computer_move()
        self.game_started = False
        if not self.game_started:
            self.repeat_prompt()

    def repeat_prompt(self):
        self.play_sound("Press start to commence a new game")

root = tk.Tk()
game = TicTacToeGame(root)
root.mainloop()

