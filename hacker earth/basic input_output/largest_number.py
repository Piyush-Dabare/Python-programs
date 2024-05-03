n , k = map(int,input().split())
k1 =  k
st = str(n)
lt = [0]*len(st)
lt1 = [0]*(len(st)-k)
n1=n
for a1 in range(len(st)):
    a = n1%10
    lt[(-a1-1)] = a
    n1//=10

# print(lt)

for i in range(len(st)):
    for j in range(i,len(st)):
        for l in range(j,len(st)):
            lts = lt
            lts.remove(lt[i])
            lts.remove(lt[j])
            lts.remove(lt[l])
            if lts > lt1:
                lt1 = lts

print(lt1)

