#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/find-mex-62916c25/

N = int(input())
l=[]
m=[]
for i in range(N):
    a = int(input(''))
    l.append(a)
    if a <= min:
        min = a
        min_idx = i
    m.append(min_idx)
print(m)