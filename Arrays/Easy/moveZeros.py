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
     
    


def moveZerosOptimized(arr:List[int],  n: int) -> int:
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

   
def moveZeroBetter(arr):
    count = 0
        
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[count] = arr[i]
            count+=1
        
    while count<len(arr):
            arr[count] = 0
            count+=1
    

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
moveZeroBetter(arr)
print(arr)