from enum import Enum


class Pointer(Enum):
    CROSS = "X"
    CIRCLE = "O"


class Player:
    def __init__(self, username: str, pointer_object: Pointer) -> None:
        self.username = username
        self.score = 0
        self.pointer_object = pointer_object
    
    @property
    def pointer(self):
        return self.pointer_object.value

    def __str__(self) -> str:
        return f"{self.username} | {self.score} points"

    @classmethod
    def info_choose_your_username(cls, player_number: int, pointer_obj: Pointer):
        pointer = pointer_obj.value
        print(f"Player {player_number}:")
        print(f"You are --  {pointer}  -- ")
        username = input("please type your username: -> ")
        return username


if __name__ == "__main__":

    player1 = Player("Deadjuju", Pointer.CIRCLE)
    print(player1.pointer)
    print(player1)
    print(player1.__dict__)
