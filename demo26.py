Std = {
    101:'Scoot',102:'Miller',103:'Adamas',104:'James',105:'David'
}
print(Std.get(101))
print(Std.get(105))
print(Std.items())
Std.update({106:'vani'})
print(Std)
Std.pop(106,'vani')
print(Std)
Std.popitem()
print(Std)
Std.setdefault(107,'Null')
print(Std)
