'''2. take a list 'l1' of even nos between 150 to 250. Print its length.
Then create another list 'l2' using 'l1', containing only nos divisible by 4 from 'l1'.
'''
l1=list(range(150,251,2))
print(l1)
print(len(l1))
l2=[e for e in l1 if e%4==0]
print(l2)
