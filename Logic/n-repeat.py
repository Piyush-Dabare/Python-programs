# WAP to find number in a list which is repeated
# exactly 'n' times

l = [23,4 ,64,89,5,5,45,23,5,45,45,9,782]
d=dict()
n=3
for i in l:
    d[i] = d.get(i,0)+1
for i in d.keys():
    if d[i]==n:
        print(i) 
print(d)


