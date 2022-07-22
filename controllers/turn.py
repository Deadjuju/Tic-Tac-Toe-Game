
from models.grid import Grid
from models.player import Player, Pointer
from views.turn_view import TurnView


class Turn:
    """
    class grouping all the parts composing a turn    
    """

    def __init__(self, grid: Grid, player: Player) -> None:
        self.grid = grid
        self.player = player
        self.turn_view = TurnView()

    def _choose_a_line(self) -> dict:
        """ choice and control of the line

        Returns:
            dict: choosen line
        """

        game_grid = self.grid
        line = self.turn_view.prompt_to_choose_a_line(game_grid)
        if line == "1":
            return self.grid.linea
        if line == "2":
            return self.grid.lineb
        if line == "3":
            return self.grid.linec
        self.turn_view.not_valide_choice_message(line)
        return self._choose_a_line()

    def _choose_a_column(self, line: dict) -> int:
        """ choice and control of the

        Args:
            line (dict):

        Returns:
            int: choosen column
        """

        column = self.turn_view.prompt_to_choose_a_column(line)
        if column == "1":
            return 1
        if column == "2":
            return 2
        if column == "3":
            return 3
        self.turn_view.not_valide_choice_message(column)
        return self._choose_a_column(line)

    def _get_the_box(self) -> str:
        """ find the choosen box with a line and a column

        Returns:
            str: choosen box
        """

        line = self._choose_a_line()
        column = self._choose_a_column(line)
        index = column - 1
        if line['name'] == self.grid.linea['name']:
            return ("a1", "a2", "a3")[index]
        if line['name'] == self.grid.lineb['name']:
            return ("b1", "b2", "b3")[index]
        if line['name'] == self.grid.linec['name']:
            return ("c1", "c2", "c3")[index]


    def _choose_a_box(self) -> str:
        """Choice and controls of the box chosen by the player

        Returns:
            str: name of choosen box
        """
        
        while True:
            box = self._get_the_box()
            is_free_box = self.grid.check_box_avaibility(box)
            if not is_free_box:
                self.turn_view.warning_box_already_used()
                return self._choose_a_box()
            if self.turn_view.prompt_confirmation(box):
                return box
            return self._choose_a_box()
    
    def run(self):
        """ Course of a turn """

        self.turn_view.announce_the_player(self.player)
        self.grid.display_current_grid
        
        box = self._choose_a_box()
        self.grid.update_template(box, self.player.pointer)


if __name__ == "__main__":

    pass
