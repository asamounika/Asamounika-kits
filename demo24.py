Std = {
    101:'Scoot',102:'Miller',103:'Adamas',104:'James',105:'David'
}
print(Std)
Std[106]='Xyz'
print(Std)
del Std[101]
del Std[106]
print(Std)
#check 101,104,105
print(101 in Std)
print(105 in Std)
print(106 in Std)
print(Std.values())
print(Std.keys())