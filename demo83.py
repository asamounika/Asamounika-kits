class TournamentReceipt:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def Receipt(self):
        final=sum(self.score)
        print("="*50)
        print("TOURNAMENT RECEIPT")
        print("="*50)
        print(f"Player Name: {self.name}")
        print(f"Final Score: {final}")
        print("QUALIFIED")
        print("="*50)
name=input("Player: ")
score=[int(input())for _ in range(3)]
TournamentReceipt(name,score).Receipt()