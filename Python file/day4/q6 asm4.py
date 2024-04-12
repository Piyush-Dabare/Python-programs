'''6. Remove empty strings from the list of strings
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]
'''
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]

for i in list1:
    if len(i)==0:
        list1.remove(i)
print(list1)

ls = [e for e in list1 if len(e)>=1]
print(ls)