'''accept amount from user and find the minimum number notes required to get the amount amount =512  
Notes: 2000,500,100,50,10,5,2,1  

500-1 note  
10  - 1 note  
2-  1 coin  

amount=20550  
2000 – 10 note  
500 – 1 note  
50 -1 note'''


twothousand=0
fivehundred=0
hundred=fifty=ten=five=two=one=0

amt = int(input("Enter amount : "))
while(1):
    if(amt>=2000):
        twothousand =int(amt/2000)
        amt = int(amt%2000)
    elif(amt>=500):
        fivehundred = int(amt/500)
        amt= amt%500
    elif(amt>=100):
        hundred = int(amt/100)
        amt = amt%100
    elif(amt>=50):
        fifty= amt//50
        amt=amt%50
    elif(amt>=10):
        ten = int(amt/10)
        amt= amt%10
    elif(amt>=5):
        five = int(amt/5)
        amt = amt%5
    elif(amt>=2):
        two= amt//2
        amt=amt%2
    else:
        one = amt
        break

print(twothousand,fivehundred,hundred,fifty,ten,five,two,one,sep=",")
#print("2000 : ",twothousand,',500 : ',fivehundred,',100 : ',hundred,',50 : ',fifty,',10 : ',ten,',5 : ',five,',2 : ',two,",1 : ",one)