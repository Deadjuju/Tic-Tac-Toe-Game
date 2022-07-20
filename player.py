class Player:
    def __init__(self, username: str, score: int=0) -> None:
        self.username = username
        self.score = score
    
    def __str__(self) -> str:
        return f"{self.username} | {self.score} points"


if __name__ == "__main__":

    player1 = Player("Deadjuju")
    print(player1)
    print(player1.__dict__)
