
from models.player import Player, Pointer


class Grid:

    def __init__(self) -> None:
        self.a1 = "_"
        self.a2 = "_"
        self.a3 = "_"

        self.b1 = "_"
        self.b2 = "_"
        self.b3 = "_"

        self.c1 = " "
        self.c2 = " "
        self.c3 = " "

    @property
    def linea(self) -> dict:
        line = {'name': "linea", 'value': f"{self.a1}|{self.a2}|{self.a3}"}
        return line

    @property
    def lineb(self) -> dict:
        line = {'name': "lineb", 'value': f"{self.b1}|{self.b2}|{self.b3}"}
        return line

    @property
    def linec(self) -> dict:
        line = {'name': "linec", 'value': f"{self.c1}|{self.c2}|{self.c3}"}
        return line

    @property
    def template(self) -> str:
        return f"{self.linea['value']}\n{self.lineb['value']}\n{self.linec['value']}"

    @classmethod
    def not_valide_choice_message(cls, wrong_choice):
        print(f"\n{'_' * 33}")
        print("############ WARNING ############")
        print(f"-- {wrong_choice} -- \nis not a valid choice")
        print(f"{'_' * 33}\n")

    def display_current_grid(self) -> None:
        print("-_ CURRENT GRID _-\n")
        print(f"{self.template}\n")

    def _choose_a_line(self):
        print("Choose a line.")
        print(f"1 -> {self.linea['value']}")
        print(f"2 -> {self.lineb['value']}")
        print(f"3 -> {self.linec['value']}")
        line = input("Type: 1, 2, or 3: ")
        print(f"Line: {line}")
        if line == "1":
            return self.linea
        if line == "2":
            return self.lineb
        if line == "3":
            return self.linec
        self.not_valide_choice_message(line)
        return self._choose_a_line()

    def _choose_a_column(self, line: dict):
        print("Choose a column.")
        print(line['value'])
        print("^ ^ ^")
        print("1 2 3")
        column = input("Type: 1, 2, or 3: ")
        if column == "1":
            return 1
        if column == "2":
            return 2
        if column == "3":
            return 3
        self.not_valide_choice_message(column)
        return self._choose_a_column(line)

    def get_the_box(self) -> str:
        line = self._choose_a_line()
        column = self._choose_a_column(line)
        index = column - 1
        if line['name'] == self.linea['name']:
            return ("a1", "a2", "a3")[index]
        if line['name'] == self.lineb['name']:
            return ("b1", "b2", "b3")[index]
        if line['name'] == self.linec['name']:
            return ("c1", "c2", "c3")[index]

    def check_box_avaibility(self, box: str) -> True:
        if box == "a1":
            if self.a1 == Pointer.CIRCLE.value or self.a1 == Pointer.CROSS.value:
                return False
        if box == "a2":
            if self.a2 == Pointer.CIRCLE.value or self.a2 == Pointer.CROSS.value:
                return False
        if box == "a3":
            if self.a3 == Pointer.CIRCLE.value or self.a3 == Pointer.CROSS.value:
                return False
        if box == "b1":
            if self.b1 == Pointer.CIRCLE.value or self.b1 == Pointer.CROSS.value:
                return False
        if box == "b2":
            if self.b2 == Pointer.CIRCLE.value or self.b2 == Pointer.CROSS.value:
                return False
        if box == "b3":
            if self.b3 == Pointer.CIRCLE.value or self.b3 == Pointer.CROSS.value:
                return False
        if box == "c1":
            if self.c1 == Pointer.CIRCLE.value or self.c1 == Pointer.CROSS.value:
                return False
        if box == "c2":
            if self.c2 == Pointer.CIRCLE.value or self.c2 == Pointer.CROSS.value:
                return False
        if box == "c3":
            if self.c3 == Pointer.CIRCLE.value or self.c3 == Pointer.CROSS.value:
                return False
        return True

    def update_template(self, box: str, pointer: str) -> None:
        if box == "a1":
            self.a1 = pointer
        if box == "a2":
            self.a2 = pointer
        if box == "a3":
            self.a3 = pointer
        if box == "b1":
            self.b1 = pointer
        if box == "b2":
            self.b2 = pointer
        if box == "b3":
            self.b3 = pointer
        if box == "c1":
            self.c1 = pointer
        if box == "c2":
            self.c2 = pointer
        if box == "c3":
            self.c3 = pointer

    def check_if_winner(self, pointer: str) -> bool:
        a_line = self.a1 == self.a2 == self.a3 == pointer
        b_line = self.b1 == self.b2 == self.b3 == pointer
        c_line = self.c1 == self.c2 == self.c3 == pointer
        column_1 = self.a1 == self.b1 == self.c1 == pointer
        column_2 = self.a2 == self.b2 == self.c2 == pointer
        column_3 = self.a3 == self.b3 == self.c3 == pointer
        diagonal_1 = self.a1 == self.b2 == self.c3 == pointer
        diagonal_2 = self.a3 == self.b2 == self.c1 == pointer

        if a_line or b_line or c_line:
            return True
        if column_1 or column_2 or column_3:
            return True
        if diagonal_1 or diagonal_2:
            return True
        return False
       

if __name__ == "__main__":

    grid = Grid()

    print("check")
    grid.check_if_winner("!")

    pointer = "/"
    box = grid.get_the_box()
    print(f"Box: {box}")
    grid.update_template(box, "O")

    print(grid.template)
    print(grid.a1)
