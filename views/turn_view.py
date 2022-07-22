from time import sleep

from models.player import Player


class TurnView:
    
    
    @classmethod
    def announce_the_player(cls, player: Player) -> None:
        print("_" * 20)
        print(f"{player.username} plays! ")
        print(f"Pointer: {player.pointer} ")
        print("-" * 20)
        input("- press enter -")

    @classmethod
    def prompt_to_choose_a_line(cls, game_grid) -> str:
        print("Choose a line.")
        print(f"1 -> {game_grid.linea['value']}")
        print(f"2 -> {game_grid.lineb['value']}")
        print(f"3 -> {game_grid.linec['value']}")
        line = input("Type: 1, 2, or 3: ")
        print(f"Line: {line}")
        return line

    @classmethod
    def prompt_to_choose_a_column(cls, line: dict) -> str:
        print("Choose a column.")
        print(line['value'])
        print("^ ^ ^")
        print("1 2 3")
        column = input("Type: 1, 2, or 3: ")
        return column

    @classmethod
    def prompt_confirmation(cls, box: str) -> bool:
        choice_confirmation = input(f"Your choice: {box}.\n Type - no - to choose an other box.\n-> ")
        if choice_confirmation == "no" or choice_confirmation == "NO":
            return False
        return True

    @classmethod
    def not_valide_choice_message(cls, wrong_choice):
        print(f"\n{'_' * 33}")
        print("############ WARNING ############")
        sleep(0.8)
        print(f"-- {wrong_choice} -- \nis not a valid choice")
        sleep(0.3)
        print(f"{'_' * 33}\n")


    @classmethod
    def warning_box_already_used(cls) -> None:
        print()
        print("!" * 15)
        print("/!\ WARNING /!\\")
        sleep(1)
        print("This box is already selected")
        sleep(1)
