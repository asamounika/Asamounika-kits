Score=list(map(str,input('Enter the scores: ').split()))
print(f"Ranked : {sorted(Score,reverse=True)}|Top Scorer : {max(Score)}")