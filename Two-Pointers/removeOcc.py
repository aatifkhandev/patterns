def removeOccurrence(arr,val):
    i = 0
    for j in range(len(arr)):
        if arr[j]!=val:
            arr[i] = arr[j]
            i+=1
    return i


arr = [3,2,2,3]
val = 3
print(removeOccurrence(arr,val))
print(arr)
        
        