from random import choice

from controllers.turn import Turn
from models.grid import Grid
from models.player import Player, Pointer
from views.menu_view import TicTacToeView

DRAW_POINTS: int = 1
VICTORY_POINTS: int = 2


class TicTacToe:

    def __init__(self, grid: Grid, view: TicTacToeView, player_manager: Player) -> None:
        self.grid = grid
        self.view = view
        self.player_manager = player_manager

    def _begin_or_quit_the_game(self) -> str:
        return self.view.begin_or_quit()

    def _choose_who_starts(self, player1: Player, player2: Player) -> Player:
        starter = choice((player1, player2))
        self.view.display_of_the_starting_player(starter)
        return starter

    def _check_if_username_is_free(self, username1, pointer2) -> str:
        username2 = self._info_choose_your_username(player_number=2, pointer_obj=pointer2)
        if username1 == username2:
            print("This username is not free")
            return self._check_if_username_is_free(username1, pointer2)
        return username2

    @classmethod
    def _change_player(cls, current_player: Player, player1: Player, player2: Player) -> Player: 
        if current_player == player1:
            return player2
        return player1

    def _info_choose_your_username(self, player_number: int, pointer_obj: Pointer) -> str:
        pointer = pointer_obj.value
        username = self.view.prompt_for_username(player_number, pointer)
        if username == "":
            self.view.not_empty_username()
            return self._info_choose_your_username(player_number, pointer_obj)
        return username        

    def run(self):
        # Welcome part
        self.view.welcome()

        begin = self._begin_or_quit_the_game()

        if begin == "quit":
            is_game_runing = False
        else:
            is_game_runing = True

        # choose player 1
        pointer1 = Pointer.CIRCLE
        username1 = self._info_choose_your_username(player_number=1, pointer_obj=pointer1)
        player1 = Player(username1, pointer1)

        # choose player 2
        pointer2 = Pointer.CROSS
        username2 = self._check_if_username_is_free(username1, pointer2)
        player2 = Player(username2, pointer2)

        while is_game_runing:

            grid = Grid()
            turn_counter = 0

            next_player = self._choose_who_starts(player1, player2)
            is_game_over = False

            # Show score
            self.view.show_score(player1, player2)

            # The part begin
            while not is_game_over:

                current_player = next_player

                turn = Turn(grid, current_player)
                turn.run()
                grid = turn.grid
                grid.display_current_grid()
                
                is_player_winner = grid.check_if_winner(current_player.pointer)

                turn_counter += 1

                if is_player_winner:
                    # we have a winner
                    current_player.score += VICTORY_POINTS
                    print(f"{current_player.username} WIN !!!")
                    input()

                    # Play an other part?
                    self.view.show_score(player1, player2)
                    is_game_over = True
                    is_game_runing = self.view.prompt_to_stop_the_game()

                elif turn_counter == 9:
                    #  draw situation
                    player1.score += DRAW_POINTS
                    player2.score += DRAW_POINTS
                    print("It's a draw!!!")

                    self.view.show_score(player1, player2)
                    is_game_over = True
                    is_game_runing = self.view.prompt_to_stop_the_game()

                next_player = self._change_player(current_player, player1, player2)
            
            
        self.view.say_goodbye()
