# t = int(input(''))
# for i in range(t):
#     l = list(map(int,input().split(' ')))
#     n=l[0]
#     m=l[1]
#     lt = [[0]*m]*n
#     ch = [[False]*m]*n
#     # print(ch)
#     for i in range(n):
#         in_lt = list(input())
#         j=0
#         for a in in_lt:
#             lt[i][j]=a
#             j+=1
# print(lt)

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a += [input()]
print(a)                

print(a + ["-".join(k) for k in zip(a)])