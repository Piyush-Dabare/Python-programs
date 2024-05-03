rock = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def calrainwater(arr):
    total_rain = 0
    l = [0]*len(arr)
    r = [0]*len(arr)
    m = arr[0]
    for i in range(len(arr)):
        if m<arr[i]:
            m=arr[i]
        l[i] = m
    print(l)

    m = arr[-1]
    for i in range(-1,-len(arr)-1,-1):
        if m<arr[i]:
            m=arr[i]
        r[i] = m
    print(r)

    for i in range(1,len(arr)-1):
        total_rain = total_rain + min(l[i],r[i]) - arr[i]
        # print(total_rain)
    return total_rain

print(calrainwater(rock))