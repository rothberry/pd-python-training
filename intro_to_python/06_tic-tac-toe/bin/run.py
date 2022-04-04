from os import system
system('cls||clear')

from TicTacToe import TicTacToe


game = TicTacToe()
# game.position_taken(2)
# game.position_taken(4)
game.display_board()
game.turn()
game.turn()
game.turn()
game.print_player("X")
game.print_player("O")
# breakpoint()

