from enum import Enum


class Pointer(Enum):
    """ Pointer value possibilities """

    CROSS = "X"
    CIRCLE = "O"


class Player:
    def __init__(self, username: str, pointer_object: Pointer) -> None:
        self.username = username
        self.score = 0
        self.pointer_object = pointer_object
    
    @property
    def pointer(self) -> str:
        return self.pointer_object.value

    def __str__(self) -> str:
        return f"{self.username} | {self.score} points"
