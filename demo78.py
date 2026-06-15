class PlayerPerformance:
    def __init__(self,name,runs):
        self.name=name
        self.runs=runs
    def Receipt(self):
        total=sum(self.runs)
        matchs=len(self.runs)
        avg=total/matchs
        print("="*50)
        print("PLAYED PERFORMANCE")
        print("="*50)
        print(f"Player Name: {self.name}")
        print(f"Total Runs: {total}")
        print(f"Matches Played: {matchs}")
        print(f"Average Runs: {avg}")
        print("="*50)
name=input("Player: ")
runs=[int(input()) for _ in range(3)]
PlayerPerformance(name,runs).Receipt()