lt = [89,70,67,50,40,30]
lenght_lt = len(lt)
for i in range(lenght_lt):
    for j in range(i,0,-1):
        if lt[j] < lt[j-1]:
            lt[j],lt[j-1] = lt[j-1],lt[j]
print(lt)
