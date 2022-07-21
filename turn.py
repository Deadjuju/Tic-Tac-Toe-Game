
from grid import Grid
from player import Player, Pointer
from views.turn_view import TurnView


class Turn:

    def __init__(self, grid: Grid, player: Player) -> None:
        self.grid = grid
        self.player = player
        self.turn_view = TurnView()

    def choose_a_box(self):
        while True:
            box = self.grid.get_the_box()
            if self.turn_view.prompt_confirmation(box, self.grid):
                return box
            return self.choose_a_box()
    
    def run(self):
        self.turn_view.announce_the_player(self.player)
        self.grid.display_current_grid()
        
        box = self.choose_a_box()
        self.grid.update_template(box, self.player.pointer)
        self.grid.display_current_grid()


if __name__ == "__main__":

    grid = Grid()
    player = Player("Deadjuju", Pointer.CIRCLE)

    turn = Turn(grid, player)

    turn.run()
