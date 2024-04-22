lt = [2,34,53,5334,70,-9,89]

def mergelist(arr1,arr2):
    l=[]
    i=0
    j=0
    while (i<len(arr1)) and (j<len(arr2)):
        if arr1[i]<arr2[j]:
            l.append(arr1[i])
            i+=1
        else:
            l.append(arr2[j])
            j+=1
    while i<len(arr1):
        l.append(arr1[i])
        i+=1
    while j<len(arr2):
        l.append(arr2[j])
        j+=1
    return l

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    arr1 = mergeSort(arr[:mid])
    arr2 = mergeSort(arr[mid:])
    lt = mergelist(arr1,arr2)
    return lt



print(mergeSort(lt))
