# 5
# 1 0 5 5 3
# 0 2 2 2 2


n = int(input())
l = list(map(int,input().split(" ")))
m = 0
p=[]
for i in range(len(l)):
    if m < i:
        m=i
    p= l[:i+1]
    print(p)
    for j in range(m+2):
        print(j in p,j)
        if j not in p:
            print(j,end=' ')
            break
