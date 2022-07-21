from time import sleep
from player import Player


TICTACTOE = """
      \/ |    |   
     _/\_|____|____
         | /\ |   
     ____|_\/_|____
      \/ |    | /\ 
      /\ |    | \/ 
"""


class TicTacToeView:
    
    @classmethod
    def welcome(cls) -> None:
        print("--- WELCOME TO THE TIC-TAC-TOE GAME!--- ")
        print(TICTACTOE)
        sleep(1)
        print()

    @classmethod
    def begin_or_quit(cls) -> str:
        message = "To quit the game type - q - or - quit -\nElse type anything. -> "
        begin_or_quit = input(message)
        if begin_or_quit == "q" or begin_or_quit == "quit":
            return "quit"
        print("Let the game begin")
        sleep(1)
        return "begin"

    @classmethod
    def display_of_the_starting_player(cls, player: Player) -> None:
        print(f"{player.username} starts the game")
        sleep(0.75)
        print("-" * 20)
        sleep(1)

    @classmethod
    def show_score(cls, player1: Player, player2: Player) -> None:
        print(f"{player1.username}|score: {player1.score} - VS - {player2.username}|score: {player2.score}")
        sleep(2)

    @classmethod
    def prompt_to_stop_the_game(cls) -> bool:
        print("To stop the game type stop:")
        response = input("|-> ")
        if response.lower() == "stop":
            return False
        return True

    @classmethod
    def say_goodbye(cls) -> None:
        print("SEE YOU SOON!!!")
        sleep(1)
        print(TICTACTOE)
        sleep(1)
