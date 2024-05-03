l = [23,43,54,546,758,542,3]

def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr.pop()
    lower_arr = []
    upper_lt = []
    for i in arr:
        if i > pivot:
            upper_lt.append(i)
        else:
            lower_arr.append(i)

    return quickSort(lower_arr) + [pivot] + quickSort(upper_lt)




print(quickSort(l))
