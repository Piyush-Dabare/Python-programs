lt = [2,34,53,539,70,-9,89]
length_lt = len(lt) 
for i in range(length_lt):
    for j in range(i,length_lt):
        if lt[i] > lt[j]:
            lt[i],lt[j]=lt[j],lt[i]
print(lt)


