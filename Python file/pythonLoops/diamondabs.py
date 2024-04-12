
n= int(input("Enter no of lines : "))
count = 1
a=(n//2)
spaces=a
#stars=(n-2*a)%n
while(count<=n):
    print("-"*spaces)
    a=a-1
    spaces=abs(a)
    count+=1