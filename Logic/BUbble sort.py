lt = [2,34,53,53,70,-9,89]
l=len(lt)
c=0
for i in range(l):
    k=l-i-1
    for j in range(k):
        if lt[j]>lt[j+1]:
            lt[j+1],lt[j] = lt[j],lt[j+1]
            c+=1
print(lt)
print(c)