t = int(input())
for k in range(t):
    n = int(input())
    s = 0
    a = list(map(int,input().split()))
    print(a)
    for i in a:
        s+=i
    print(s)
    s1 = (n*(n+1))
    print(s1)
    if s1 == 2*s:
        print("YES")
    else:
        print("NO")
    s=0