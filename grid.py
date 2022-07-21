
class Grid:

    def __init__(self) -> None:
        # self.a1 = "_"
        self.a2 = "_"
        self.a3 = "_"

        self.b1 = "_"
        self.b2 = "_"
        self.b3 = "_"

        self.c1 = " "
        self.c2 = " "
        self.c3 = " "

    @property
    def a1(self, pointer='_') -> str:
        return pointer

    @property
    def linea(self) -> str:
        return f"{self.a1}|{self.a2}|{self.a3}"

    @property
    def lineb(self) -> str:
        return f"{self.b1}|{self.b2}|{self.b3}"

    @property
    def linec(self) -> str:
        return f"{self.c1}|{self.c2}|{self.c3}"

    @property
    def template(self):
        return f"{self.linea}\n{self.lineb}\n{self.linec}"

    @classmethod
    def not_valide_choice_message(cls, wrong_choice):
        print(f"\n{'_' * 33}")
        print("############ WARNING ############")
        print(f"-- {wrong_choice} -- \nis not a valid choice")
        print(f"{'_' * 33}\n")

    def _choose_a_line(self):
        print("Choose a line.")
        print(f"1 -> {self.linea}")
        print(f"2 -> {self.lineb}")
        print(f"3 -> {self.linec}")
        line = input("Type: 1, 2, or 3: ")
        if line == "1":
            return self.linea
        if line == "2":
            return self.lineb
        if line == "3":
            return self.linec
        self.not_valide_choice_message(line)
        return self._choose_a_line()

    def _choose_a_column(self, line):
        print("Choose a column.")
        print(line)
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

    def get_the_box(self):
        line = self._choose_a_line()
        column = self._choose_a_column(line)
        index = column - 1
        if line == self.linea:
            return ("a1", "a2", "a3")[index]
        if line == self.lineb:
            return ("b1", "b2", "b3")[index]
        if line == self.linec:
            return ("c1", "c2", "c3")[index]

    
    # @property
    # def replace_box(self, pointer):
    #     box = self._get_the_box()
    #     if box == "a1":
    #         self.a1 == pointer
    #     if box == "a2":
    #         self.a2 == pointer
    #     if box == "a3":
    #         self.a3 == pointer
    #     if box == "b1":
    #         self.b1 == pointer
    #     if box == "b2":
    #         self.b2 == pointer
    #     if box == "b3":
    #         self.b3 == pointer
    #     if box == "c1":
    #         self.c1 == pointer
    #     if box == "c2":
    #         self.c2 == pointer
    #     if box == "c3":
    #         self.c3 == pointer




if __name__ == "__main__":

    grid = Grid()
    print(grid.template)

    pointer = "/"
    grid.get_the_box()
    
    print(grid.template)
