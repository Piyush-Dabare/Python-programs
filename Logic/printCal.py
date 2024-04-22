startDate = int(input("Enter number of days : "))
startDay = input("Enter start day : ")

d = ['m','tu','w','th','fr','sat','sun']
h = d.index(startDay)

print(" "*h,end="  ")

for i in range(1,startDate+1):
    if (h+i)%7==0:
        print()
    print(i,d[(h+i-1)%7],end=' ',sep=":")





