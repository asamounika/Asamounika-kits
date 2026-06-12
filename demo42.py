Score=list(map(int,input('Enter the HTTP codes: ').split()))
Last_five=Score[-5:]
print(f"Last Five: {Last_five} | Critical Error Found: {True if 500 in Last_five else False}") 
