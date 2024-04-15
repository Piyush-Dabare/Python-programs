'''Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :  
     Unit                                             Price    
First 100 units                                       no charge  
Next 100 units                                        Rs 5 per unit  
After 200 units                                       Rs 10 per unit  
(For example if input unit is 350 than total bill amount is Rs2000)  '''

units = int(input("Enter number of units : "))

charge=0
if units >200:
    charge = charge + (units - 200) * 10
    units = 200

if units > 100:
    charge = charge + (units - 100) * 5
    units = 100

if units <= 100:
    charge = charge + units * 0

print(charge)
