def moveZero(arr):
    n = len(arr)
    temp = [0]*n
    
    j = 0
    
    for i in range(n):
        if arr[i]!=0:
            temp[j] = arr[i]
            j+=1
            
    while j<n:
        temp[j] = 0
        j+=1
        
    for i in range(n):
        arr[i] = temp[i]
    
    return arr
     
    


# def moveZerosOptimized(arr:List[int],  n: int) -> int:
    j = -1
    # Place the pointer j
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return arr
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
moveZero(arr)
print(arr)
# n = 10
# ans = moveZerosOptimized(arr, n)
# for it in ans:
#     print(it, end=' ')
# print()




# arr = [1,0,2,0,3,0,4,5]
# n = len(arr)
# print(moveZero(arr,n))
