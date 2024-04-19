no = int(input("Enter a number : "))

for i in range(2,int((no**0.5)+1)):
    if no % i == 0:
        print("Not a Prime number .")
        break