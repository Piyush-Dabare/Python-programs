rock = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def left(arr, n):
    m = arr[n]
    for i in range(n):
        if arr[i]>m:
            m= arr[i]
    return m

def right(arr, n):
    m = arr[n]
    for i in range(n+1,len(arr)):
        if arr[i]>m:
            m= arr[i]
    return m

def calrainwater(arr):
    total_rain = 0
    for i in range(1,len(arr)-1):
        l = left(arr,i)
        r = right(arr,i)
        total_rain = total_rain + min(l,r) - arr[i]
        # print(total_rain)
    return total_rain

print(calrainwater(rock))