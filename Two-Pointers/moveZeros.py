def moveZeros(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]==0:
            arr[i] = arr[j]
            i+=1
    return arr





arr = [1,0,2,0,3,0,4,0,5]
moveZeros(arr)
print(arr)