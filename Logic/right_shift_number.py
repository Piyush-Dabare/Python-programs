# WAP to do right shift on given integer.
#     Ex. val = 1234 after right shift
#         right_shifted_val = 4123

val = int(input("Enter a number : "))
n = int(input("Enter number for right shift : "))
l = str(val)
l = len(l)
r = val % (10**(l-n))
r= r*(10**n)
l = val // (10**(l-n))
r = r+l
print(r)
