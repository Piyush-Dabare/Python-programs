t = int(input())
n,x,y = map(int,input().split(' '))
lt = list(map(int,input().split(" ")))
s= 0
for j in  range(t):
    for i in lt:
        if x*i <= y:
            s += x*i
        else:
            s+=y
    print(s)
    s=0
  