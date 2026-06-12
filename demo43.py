score=list(map(int,input('Enter the scores: ').split()))
result=sum(score)/len(score)
print(f"The average is: {result:.2f}")