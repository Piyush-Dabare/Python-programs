'''4. Print two lists in the following order
list1 = [5, 6,7]
list2 = [0, 1]
output:
50,51,60,61,70,71'''

list1 = [5, 6,7]
list2 = [0, 1]

for i in list1:
    for j in list2:
        print(i,j,sep='',end=',')
print()

for i in list1:
    for j in list2:
        print(str(i)+str(j),',',end=" ")   