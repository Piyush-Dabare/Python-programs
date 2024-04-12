'''8. Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like 
the following list

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]
output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n'] 

solution
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]
list1[2][1][2].extend(subList)
print(list1)'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
ls = ["h", "i", "j"]
for i in ls:
    list1[2][1][2].append(i)
print(list1)