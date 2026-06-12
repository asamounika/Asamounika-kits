List=[5,10,2,4,15,6,8,12,20,3]
print("List is: ",List)
print("Length of the list is:",len(List))
print("Maximam value in the list is: ",max(List))
print("Minimum value in the list is: ",min(List))
print("Sum of the list is: ",sum(List))
print("Average of the list is : ",sum(List)/len(List))
print("Sorted list is :",sorted(List))


#List slicing
my_list=[1,2,3,4,5,6,7,8,9,10]
print(my_list[:])
print(my_list[0:5])
print(my_list[::2])
print(my_list[5:8])
print(my_list[-6:-2])
print(my_list[::-1])

List=["Python","Java","C++","JavaScript"]
print("The original list is: ",List)
List.append("Ruby")
print("The list after appending is: ",List)
List.append("SQL")
print("The list after appending is: ",List)

List=["python","java","c++","javascript"]
print("The original list is: ",List)
List.insert(0,"SQL")
print(List)
List.remove("c++")
print(List)

List=["python","jsva","c++","javascript"]
print("The original list is: ",List)
List.reverse()
print("The reversed list is : ",List)

front_end=['Html','Css','Javascript','Bootcamp','Reacts']
lang=['python','Django','Flask','NodeJS','ExpressJs']
print("Front-end technologiesa:",front_end)
print("Back-end technologies: ",lang)

List=[2,3,4,5,2,2]
print(List.count(2))

List=[2,3,4,5,2,2]
List.sort()
print(List)
List.reverse()
print(List)
List.clear()
print(List)

a=[10,20,30]
b=[1,2,3]
result=a+b
print(result)

b=[1,2,3]
result=b*3
print(result)

