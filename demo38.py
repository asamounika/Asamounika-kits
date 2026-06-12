'''
Create list of candidates
and candidates from last
remove one by one candidates from first
add a candidate in between at highest priority
'''
''''queue=['Mouni','vani','Mini','Chinnari']
queue.append('Anvika')
print(queue)
queue.remove('Mouni')
print(queue)
queue.insert(1,'Anvi')
print(queue)
'''
price=list(map(int,input('Enter the Price: ').split()))
new_list=[]
for i in price:
    if i>1000:
        new_list.append(i)
print(new_list)
#or
price=list(map(int,input('Enter the Price: ').split()))
print([i for i in price if i>1000])