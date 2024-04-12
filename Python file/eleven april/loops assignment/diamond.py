l= int(input("Enter no o lines : "))
s = (l+1)//2
count=1
n=l
while(count<=l):
    c=count%s
    odd=2*(c)-1
    print("-"*(n%s))
    #print("*"*(odd))
    count+=1
    n-=1