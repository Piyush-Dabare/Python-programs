'''n=int(input("enter no of lines "))
counter =1
num = n//2
while(counter <=n):
    print(" "*num ,'*'*(2*counter-1))
    num -= 1 
    counter+=1'''


n= int(input("Enter no of lines : "))
count =0
stars=1
spaces=n//2
while(count<(n//2+1)):
    print(" "*spaces,"*"*stars,sep="")
    spaces=spaces-1
    stars=stars + 2
    count+=1
count=0
stars=n-2
spaces=1
