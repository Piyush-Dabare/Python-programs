st = input("")
z=0
o=0
for i in st:
    if i == "z":
        z+=1
    else:
        o+=1
if(2*z == o):
    print("Yes")
else:
    print("No")

