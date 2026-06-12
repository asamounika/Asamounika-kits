#area
area = lambda r:3.14*r**2
print(area(5))

#square root
square=lambda n:n**2
print(square(4))

#sum of variable arguments total numbers
def total(*num):
    print(sum(num))
total(1,2,3,4,5)

#Index
Cartoons=['Tom and Jerry','Doremon','Shinchan','Chhoto Bheem','Motu patlu']
print(Cartoons)
print("Accessing the list using positive indexing: ")
print(Cartoons[0])
print(Cartoons[1])
print(Cartoons[2])
print(Cartoons[3])
print(Cartoons[4])
print("Accessing the list using negative indexing: ")
print(Cartoons[-1])
print(Cartoons[-2])
print(Cartoons[-3])
print(Cartoons[-4])
print(Cartoons[-5])

#with index
Cartoons=['Tom and Jerry','Doremon','Shinchan','Chhoto Bheem','Motu patlu']
for i in range(len(Cartoons)):
    print(f"Index {i}: {Cartoons[i]}")
print("----------------------")
#without index
for i in Cartoons:
    print(i)

#using while loop
Cartoons=['Tom and Jerry','Doremon','Shinchan','Chhoto Bheem','Motu patlu']
i=0
while i<len(Cartoons):
    print(Cartoons[i])
    i+=1

#delete
Cartoons=['Tom and Jerry','Doremon','Shinchan','Chhoto Bheem','Motu patlu']
print(Cartoons)
del Cartoons[0]
print(Cartoons)
del Cartoons[3]
print(Cartoons)