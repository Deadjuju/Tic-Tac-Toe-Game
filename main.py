from random import choice

from grid import Grid
from menu_view import MenuView
from player import Player, Pointer


class TicTacToe:

    def __init__(self, grid, menu_view, player_manager) -> None:
        self.grid = grid
        self.menu_view = menu_view
        self.player_manager = player_manager

    def _begin_or_quit_the_game(self) -> str:
        return self.menu_view.begin_or_quit()

    def _choose_who_starts(self, player1: Player, player2: Player):
        starter = choice((player1, player2))
        self.menu_view.display_of_the_starting_player(starter)
        return starter


    def run(self):
        # Welcome part
        self.menu_view.welcome()

        begin = self._begin_or_quit_the_game()
        print(begin)

        if begin == "quit":
            is_game_runing = False
        else:
            is_game_runing = True

        while is_game_runing:

            # choose player 1
            pointer1 = Pointer.CIRCLE
            username1 = player_manager.info_choose_your_username(player_number=1, pointer_obj=pointer1)
            player1 = Player(username1, pointer1)

            # choose player 2
            pointer2 = Pointer.CROSS
            username2 = player_manager.info_choose_your_username(player_number=2, pointer_obj=pointer2)
            player2 = Player(username2, pointer2)

            print(player1.__dict__)
            print(player2.__dict__)

            next_player = self._choose_who_starts(player1, player2)

            # turn = Turn(player=next_player, grid)

        

            input()



if __name__ == "__main__":

    grid = Grid()
    menu_view = MenuView()
    player_manager = Player

    tic_tac_toe = TicTacToe(grid, menu_view, player_manager)

    tic_tac_toe.run()
