line= int(input("Enter a numbers of lines : "))

pattern = '10'
one = '1'
n=line - 1
for i in range(1,line+1,1):
    print(" "*(i-1),pattern*n,'1',sep='')
    n-=1