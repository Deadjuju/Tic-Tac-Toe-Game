
from models.player import Pointer


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

    @property
    def display_current_grid(self) -> None:
        print(f"-_ CURRENT GRID _-\n{self.template}\n")

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
