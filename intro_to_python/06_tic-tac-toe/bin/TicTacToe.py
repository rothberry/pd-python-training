from ast import Or
from doctest import FAIL_FAST


init_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# init_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# test_board = ["1", "2", "3", "X", "5", "6", "7", "8", "9"]
WIN_COMBOS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


class TicTacToe:
    def __init__(self):
        self.board = init_board
        self.counter = 0
        self.player_dict = {"X": [], "O": []}
        pass

    def test_hi(self):
        print("sup")

    def display_board(self):
        print(f"===TURN={self.counter + 1}===")
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])
        print("==========")

    def input_to_index(self, user_input):
        # converts user input to idx
        return int(user_input) - 1

    def move(self, player, location):
        # If the move is valid, make the move and display the board.
        if not self.position_taken(location):
            # self.move(player, self.input_to_index(spot))
            self.counter += 1
            self.player_dict[player].append(location)
            self.board.insert(location, player)
            self.board.pop(location + 1)
            self.display_board()
        else:
            # If the move is invalid, ask for a new move until a valid move is received.
            print("Try Again....")
            self.turn()

    def position_taken(self, location):
        # breakpoint()
        return self.board[location] == "X" or self.board[location] == "O"

    def turn(self):
        # Ask the user for their move by specifying a position between 1-9.
        # print("Pick a spot:")
        # Receive the user's input.
        spot = input("Pick a Spot!\n")
        print("You chose: " + spot)
        # Translate that input into an index value.
        location = self.input_to_index(spot)
        print("Which is index: " + str(location))
        self.move(self.current_player(), location)

    def current_player(self):
        if self.counter % 2 == 0:
            return "X"
        else:
            return "O"

    def turn_count(self):
        print(f"Currently: {self.counter}")            

    def print_player(self, player):
        print(self.player_dict[player])

    def did_win(self):
        pass

    def is_full(self):
        pass

    def is_draw(self):
        pass

    def is_over(self):
        pass

    def winner(self):
        pass
