'''
income = int(input("Enter your income : "))

if(income>=100000):
    print("PLatinum Card")
elif(income>50000):
    print("Gold Card")
elif(income>25000):
    print("Silver Card")
else:
    print("Bronze Card")
    
'''

'''
idx = 0
while idx < 5:
    print("*",end=" ")
    idx+=1
print("*" * 5)
'''
# while(1):    
#     print("""\na.thali 
# b.chapati 
# c.lassi 
# d.paratha """)
#     order=input("enter your order   :   ")
#     if(order == "a"):
#         print("thali order placed")
#     elif(order == "b"):
#         print("chapati order placed")
#     elif(order =="c"):
#         print("lassi ordered")
#     elif(order=="d"):
#         print("Paratha")
#     else:
#         print("quit")
#         break
# else:
#     print("Limit is reached")

# s = "Hello"
# formatted_string = "{:*>7}".format(s)
# print(formatted_string)

# # r=s.split('')
# print()



# l = [23,43,54,546,758,542,3]

# for i in range(len(l)):
#     print(f"value at {i} : ", l[i])

# import math

# print()
# point = math.sqrt((3-1)**2+(4-1)**2)
# print(point)


# print(int('0010',2))

# print()
# st = "Hi there learning python!"
# st = st.split()
# st = [i.capitalize() for i in st]
# st = " ".join(st)
# print(st)

# ind = int(input("Enter index at which string to be inserted : "))
# st = "Python 3.12"
# print(st)
# s=[]
# sub_str = input("Enter a substring to be inserted ")
# s.append(st[:ind])
# s.append(sub_str)
# s.append(st[ind:])
# s = ' '.join(s)
# # st[7:8]= sub_str
# print(s)

# st = ['qee','ta','ycv','ibh','pdkj']
# st = sorted(st, key= lambda x: x[1])
# print(st)

# print(s)
# s.remove(54)
# print(s)
# s.discard(2)
# print(s)

# from itertools  import combinations,permutations
# num='1234' #[1,2,3,4]
# combs=[]
# for num_len in range(1,len(num)+1):
#     combs += list(set(combinations(num,num_len)))
# print(combs)
# perm=[]
# for comb in combs:
#     perm += list(set(permutations(comb)))
# print(list(set(perm)))
# l=[12,34,53,45]

# st = 'BANANANA'
# d1 = dict()
# vowels = 'AEIOU'
# for i in range(len(st)):
#     for j in range(i+1,len(st)):
#         if st[i] in vowels:
#             d1[st[i:j]] = d1.get(st[i:j],0) + 1
#         else:
#             break

# print(d1)
# d2 = dict()
# for i in range(len(st)):
#     for j in range(i+1,len(st)):
#         if st[i] not in vowels:
#             d2[st[i:j]] = d2.get(st[i:j],0) + 1
#         else:
#             break
# m = max(d1.values())
# print(d2, m)

# 5. Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order. It should work for any two lists.
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# # output:
# # 10 400
# # 20 300
# # 30 200
# # 40 100
# # print(list2[-])
# j=-1
# for i in range(len(list1)):
#     print(list1[i],list2[j])
#     j-=1

# vowels = "AEIOUY"
# #DDXDDD-DD
# #012345678
# st = input()
# lt = list(st)
# p = 'valid'
# c = []
# a = int(lt[0])+ int(lt[1])
# c.append(a)
# a= int(lt[3]) + int(lt[4])
# c.append(a)
# a = int(lt[4]) + int(lt[5])
# c.append(a)
# a = int(lt[7]) + int(lt[8])
# c.append(a)
# for i in c:
#     if i%2==1:
#         p="invalid"
#         break
# if lt[2] in vowels:
#     p="invalid"
# print(p)


# l = [12,34,56,7,4,90,23,34,64,6] 
# # for i,j in enumerate(l):
# #     print("index =",i,"value =",j)
# # print(l)
# # # lt = [e if e>20 else 9009 for e in l]
# lt = l
# # print(lt)
# # lt.insert(0,89578)
# print(lt[::3])

# num = 3456
# c=0
# l=[]
# for i in range(len(str(num))):
#     l.append(num%10)
#     num//=10
# c = len(l)
# print(l)
# print(c)

# for i in l:
    

# l = [True for i in range(7)]
# print(l)
emp={45:"ankit",12:"suraj",56:"chardul",98:"vivek",23:"bsumati",1:"sumantra"}
# sort them by their id

print(sorted(emp.values()))
sorted_empid_dict = {}
for empid in sorted(emp.values()):
    for i in emp.keys():
        if emp[i]==empid:
            break  
    sorted_empid_dict[i] = empid
print(sorted_empid_dict)