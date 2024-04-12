#range(start, end , step)
# returns a iterator



#n=int(input("enter a number"))
#print(list(range(1,n,2)))
#for i in range(1,n,2): 
 #   print(i)


n=int(input("enter a number to see its table"))
for i in range(1,11,1):
    print(n,"X", i, "=" ,n*i)
print(list(range(n,n*10+1,n)))