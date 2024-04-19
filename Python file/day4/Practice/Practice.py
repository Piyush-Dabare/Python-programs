#5
# ls = ['abc', 'xyz', 'aba', '1221','3cdf3']
# count=0
# for i in ls:
#     if len(i)>=2 and i[0]==i[-1]:
#         count+=1
# print(count)

#6
# ls = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# l = [e[1] for e in ls ]
# l.sort()
# m = []
# idx =0
# for i in range(len(l)):
#     for j in range(len(ls)):
#         if l[i] == ls[j][1]:
#             m.append(ls[j])
#             break
# print(m)

#7
# ls = [1,2,3,5,4,8,5,2,3,4,1]
# l = []
# for i in ls:
#     if i not in l:
#         l.append(i)

# print(l)

#9
# ls = [1,2,3,[4,5,6]]
# l=[]
# for i in ls:
#     l.append(i)
# print(l)
# ls[1] = 500
# print(ls)
# print(l) 

#12
# ls = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# ls.remove(ls[3])
# print(ls)

#13
ls = [[['*']*6]*4]*3
print(ls)

