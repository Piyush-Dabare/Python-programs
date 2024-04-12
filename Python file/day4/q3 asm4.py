'''
3. Given a Python list of numbers. Turn every item of a list into its square root
aList = [1, 4, 9, 16, 25, 36, 49] 
output:
[1, 2, 3, 4, 5, 6, 7]'''

aList = [1, 4, 9, 16, 25, 36, 49] 
import math
l2=[]
for i in aList:
    l2.append(math.sqrt(i))
print(l2)
l3 = [e**0.5 for e in aList ]
print(l3)