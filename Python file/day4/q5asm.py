'''5. Given a two Python list. Iterate both lists simultaneously such that list1 should display 
item in original order and list2 in reverse order. It should work for any two lists.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
output:
10 400
20 300
30 200
40 100'''

list1 = [10, 20, 30, 40,50]
list2 = [100, 200, 300, 400,500]


for i in list1:
    for j in range(-1,-(len(list2)+1),-1):
        print(i,list2[j])
        j-=1
        break
''' 
list3 = list2[::-1]
for e1,e2 in zip(list1,list3):
    print(e1,e2)
'''


