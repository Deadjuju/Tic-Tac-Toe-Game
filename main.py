from controllers.tic_tac_toe_controller import TicTacToe
from models.grid import Grid
from models.player import Player
from views.menu_view import TicTacToeView



if __name__ == "__main__":

    grid = Grid()
    view = TicTacToeView()
    player_manager = Player

    tic_tac_toe = TicTacToe(grid, view, player_manager)

    tic_tac_toe.run()
