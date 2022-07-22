from time import sleep
from models.player import Player


TICTACTOE = """
      \/ |    |   
     _/\_|____|____
         | /\ |   
     ____|_\/_|____
      \/ |    | /\ 
      /\ |    | \/ 
"""
POURCENT_1 = "▒▒▒▒▒▒▒▒▒▒ 0%"
POURCENT_2 = "█▒▒▒▒▒▒▒▒▒ 10%"
POURCENT_3 = "██▒▒▒▒▒▒▒▒ 20%"
POURCENT_4 = "███▒▒▒▒▒▒▒ 30%"
POURCENT_5 = "████▒▒▒▒▒▒ 40%"
POURCENT_6 = "█████▒▒▒▒▒ 50%"
POURCENT_7 = "██████▒▒▒▒ 60%"
POURCENT_8 = "███████▒▒▒ 70%"
POURCENT_9 = "████████▒▒ 80%"
POURCENT_10 = "█████████▒ 90%"
POURCENT_11 = "██████████ 100%"
FIREWORK = """
         .* *.               `o`o`
         *. .*              o`o`o`o      ^,^,^
           * \               `o`o`     ^,^,^,^,^
              \     ***        |       ^,^,^,^,^
               \   *****       |        /^,^,^
                \   ***        |       /
    ~@~*~@~      \   \         |      /
  ~*~@~*~@~*~     \   \        |     /
  ~*~@smd@~*~      \   \       |    /     #$#$#        .`'.;.
  ~*~@~*~@~*~       \   \      |   /     #$#$#$#   00  .`,.',
    ~@~*~@~ \        \   \     |  /      /#$#$#   /|||  `.,'
_____________\________\___\____|_/______/_________|\/\___||______
"""

class TicTacToeView:

    @classmethod
    def _print_loader(cls, time_transition: float) -> None:
        print(POURCENT_1)
        sleep(time_transition)
        print(POURCENT_2)
        sleep(time_transition)
        print(POURCENT_3)
        sleep(time_transition)
        print(POURCENT_4)
        sleep(time_transition)
        print(POURCENT_5)
        sleep(time_transition)
        print(POURCENT_6)
        sleep(time_transition)
        print(POURCENT_7)
        sleep(time_transition)
        print(POURCENT_8)
        sleep(time_transition)
        print(POURCENT_9)
        sleep(time_transition)
        print(POURCENT_10)
        sleep(time_transition)
        print(POURCENT_11)
        sleep(time_transition)

    
    @classmethod
    def welcome_message(cls) -> None:
        print("--- WELCOME TO THE TIC-TAC-TOE GAME!--- ")
        print(TICTACTOE)
        sleep(1)
        print()

    @classmethod
    def begin_or_quit(cls) -> str:
        message = "To quit the game type - q - or - quit -\nElse type anything. -> "
        begin_or_quit = input(message)
        return begin_or_quit

    @classmethod
    def game_begin_message(cls) -> None:
        print("/" * 25)
        sleep(0.8)
        print("Let the game begin\n")
        sleep(1)

    @classmethod
    def waiting_for_starter_player(cls) -> None:
        """ Display a waiting message with a false loader """
        print("Please wait, We draw lots the player who will start")
        sleep(1)
        TicTacToeView._print_loader(0.06)


    @classmethod
    def display_of_the_starting_player(cls, player: Player) -> None:
        print(f"{player.username} starts the game")
        sleep(0.75)
        print(f'{"-" * 20}\n')
        sleep(1)

    @classmethod
    def show_score(cls, player1: Player, player2: Player) -> None:
        print("\n -----__________ SCORE: __________-----")
        sleep(0.1)
        print(f"{player1.username}|score: {player1.score} - VS - {player2.username}|score: {player2.score}")
        sleep(2)

    @classmethod
    def prompt_for_username(cls, player_number, pointer) -> str:
        print("_" * 15)
        sleep(0.5)
        print(f"Player {player_number}:")
        print(f"You are --  {pointer}  -- ")
        username = input("please type your username: -> ")
        return username

    @classmethod
    def not_empty_username(cls) -> None:
        print()
        print("!" * 15)
        print("/!\ WARNING /!\\")
        sleep(1)
        print("This field can not be empty.")
        sleep(1)

    @classmethod
    def username_already_used(cls) -> None:
        print("\n---------- INFORMATION ----------")
        print("-" * 33)
        sleep(1)
        print("This username is already in use")
        sleep(0.5)
        print("Please choose an other one\n")
        sleep(1)
        
    @classmethod
    def congrat_the_winner(cls, winner: str) -> None:
        print("\nWe've got a winner!!!")
        sleep(0.8)
        print(f"{winner} WIN !!!")
        sleep(1.5)
        print(FIREWORK)
        sleep(0.1)
        print()
        sleep(1.5)

    @classmethod
    def announce_equality(cls) -> None:
        print("\n ----- RESULT -----")
        print("It's a draw!!! \n")
        sleep(1)

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
