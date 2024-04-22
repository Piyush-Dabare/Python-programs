l = [23,43,54,546,758,542,3]

def quickSort(arr):
    if len(arr)<2:
        return arr
    max_index = 0
    pivot = arr[-1]
    for i in range(len(arr)):
        if arr[i] > pivot:
            max_index = i
        if arr[i] < pivot:
            arr[max_index],arr[i]= arr[i],arr[max_index]
    left = quickSort(arr[:i])
    right = quickSort(arr[i:])
    l = left + right
    return l




print(quickSort(l))
