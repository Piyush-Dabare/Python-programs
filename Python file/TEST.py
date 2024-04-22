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

st = ['qee','ta','ycv','ibh','pdkj']
st = sorted(st, key= lambda x: x[1])
print(st)

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

