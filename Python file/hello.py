'''print("HELLO ..")
print("another hello")
name = input ('Emter your name : ')
rollno = input ("Rnter your rollno : ")
print(name,rollno,sep=",",end=" ")
print("Name:",name,"Rollno:",rollno, end="$")

var1=10
print("Memory location : ",id(var1))
var2=var1
print("Memeory Location var2 : ", id(var2))
var1=12
print("Memory location : ",id(var1))
print("Memeory Location var2 : ", id(var2))

num = input("Enter a number : ")
num1=num+var1
print(num1)

tot_lect= int(input("Enter Total Lectures "))
att_Lect = int(input("Enter Attended Lectures "))

print(att_Lect,tot_lect)

per_att = att_Lect/tot_lect *100
if(per_att > 75):
    print("Alowed fro exam")
elif(per_att>50):
    print("Allowed with 40% reduction")
else:
    print("Not Allowed")'''
    
print(2**3**2)


