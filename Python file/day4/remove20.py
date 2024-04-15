'''10. Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
output:
[5, 15, 25, 50]'''

list1 = [5, 20, 15, 20, 25, 50, 20]

list2=[e for e in list1 if e!=20]


