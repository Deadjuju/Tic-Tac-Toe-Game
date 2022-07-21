from player import Player


TICTACTOE = """
      \/ |    |   
     _/\_|____|____
         | /\ |   
     ____|_\/_|____
      \/ |    | /\ 
      /\ |    | \/ 
"""


class MenuView:
    
    @classmethod
    def welcome(cls):
        print("--- WELCOME TO THE TIC-TAC-TOE GAME!--- ")
        print(TICTACTOE)

    @classmethod
    def begin_or_quit(cls) -> str:
        message = "To quit the game type - q - or - quit -\nElse type anything. -> "
        begin_or_quit = input(message)
        if begin_or_quit == "q" or begin_or_quit == "quit":
            return "quit"
        return "begin"

    @classmethod
    def display_of_the_starting_player(cls, player: Player):
        print(f"{player.username} starts the game")
