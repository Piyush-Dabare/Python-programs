n = int(input())

lt = list(map(int,input().split(' ')))
lenght_lt = len(lt)
sum_of_list = 0
s =0
for i in range(lenght_lt):
    l=i
    r= i+1
    k=1
    for j in range(i,lenght_lt):
        print(" j = ", j)
        if r > lenght_lt:
            break
        sum_of_list += sum(lt[l:r])
        l = r
        print('l = ',l)
        r = r + 1 + k
        k+=1
        print("r = ",r)
    if sum_of_list > s:
        s = sum_of_list
        sum_of_list = 0
print(s)

l = [23,43,54,546,758,542,3]
print(*l)
