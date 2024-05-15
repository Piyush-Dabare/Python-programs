# # 5
# # 1 0 5 5 3
# # 0 2 2 2 2
# # 0 8 7 1 1 4 3 7 0 2


# N = int(input())
# l = list(map(int,input().split(" ")))
# # print(l)10
# m = 0
# n = 0

# for i in l:
#     if m==i:
#         m = m + n + 1
#     if n+1 == i:
#         n = i
#     print(m,end=' ')
import math
from typing import List
def quadraticRoots( a : int, b : int , c:int ) -> List[int]:
        # code 
        d = b*b - 4*a*c
        print(d)
        if d < 0:
            return [-1]
        else:
            print((-b + math.sqrt(d))/(2*a))
            x = math.floor((-b + math.sqrt(d))/(2*a))
            y = math.floor((-b - math.sqrt(d))/(2*a))
            if x > y: 
                return [x,y]
            else:
                return [y,x]
print(quadraticRoots(752, 904 ,164))