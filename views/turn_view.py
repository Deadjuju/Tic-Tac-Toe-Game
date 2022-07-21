from time import sleep


class TurnView:
    
    
    @classmethod
    def announce_the_player(cls, player) -> None:
        print("_" * 20)
        print(f"{player.username} plays! ")
        print(f"Pointer: {player.pointer} ")
        print("-" * 20)
        input("- press enter -")

    @classmethod
    def prompt_confirmation(cls, box, grid) -> bool:
        grid.display_current_grid()
        choice_confirmation = input(f"Your choice: {box}.\n Type - no - to choose an other box.\n-> ")
        if choice_confirmation == "no" or choice_confirmation == "NO":
            return False
        return True

    @classmethod
    def warning_box_already_used(cls) -> None:
        print("!" * 15)
        print("/!\ WARNING /!\\")
        sleep(1)
        print("This box is already selected")
        sleep(1)
    