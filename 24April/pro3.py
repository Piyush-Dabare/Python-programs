t = int(input())
for i in range(t):
    n , k = map(int,input().split())
    lt = list(map(int,input().split()))
    lt = sorted(lt)
    s = 0
    for j in range(k):
        if (7-lt[j])>lt[j]:
            lt[j] = 7- lt[j]
            s+=lt[j]
        s += sum(lt[k:])
    print(s)