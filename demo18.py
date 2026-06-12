'''
shallow copy- original & new list both will be updated
deep copy- original & new list both will be different
'''
import copy
original=[1,2,3,4,5]
print(original)
new=copy.deepcopy(original)
print(new)
new[0]=100
print(original)
print(new)

import copy
original=[1,2,3,4,5]
print(original)
new=original
print(new)
new[0]=100
print(original)
print(new)
