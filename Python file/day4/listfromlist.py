l1=[11,25,66,99,201,121]
l2=[e for e in l1 if e%11==0]
print(l2)
l2=[e if e>30 else None for e in l1]
print(l2) 