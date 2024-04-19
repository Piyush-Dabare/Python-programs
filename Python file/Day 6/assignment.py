#1
# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red","Yellow","orange"]
# sampleSet.add(sampleList)

#2
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.intersection(set2))

#3
# set1 = {10, 20, 30, 40, 50,25}
# set2 = {30, 40, 50, 60, 70,100}

# u = set1.union(set2)
# common_element = set1.intersection(set2)
# print(u-common_element)

#4
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# u = set1.union(set2)
# i= set1.intersection(set2)
# print(u-i)

# tuple 1
# aTuple = (10, 20, 30, 40, 50,60)
# print(tuple(sorted(aTuple,reverse=True)))

# aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
# print(aTuple[1][1])

# aTuple = (10, 20, 30, 40)
# a,b,c,d = aTuple
# print(a,b,c,d)

# tuple1 = (11, 22)
# tuple2 = (99, 88)

# tuple1,tuple2 = tuple2,tuple1
# print(tuple1,tuple2)

# tuple1 = (11, [22, 33], 44, 55)
# tuple2 = tuple1[2:len(tuple1)]
# print(tuple2)

# tuple1 = (11, [22, 33], 44, 55)
# tuple1[1][0]=200
# print(tuple1)

# a= 10
# b= 20
# a,b = b,a
# print(a,b)