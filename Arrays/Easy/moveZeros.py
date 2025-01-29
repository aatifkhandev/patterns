from typing import List
# i/p : [1,0,2,0,3,0,4,0]
#o/p : [1,2,3,4,5,0,0,0,0,0]


def moveZero(arr:List[int],n:int)->int:
    temp = []
    
    for i in range(n):
        if arr[i]!=0:
            temp.append(arr[i])
            
    nz = len(temp)
    
    
    for i in range(nz):
        arr[i] = temp[i]
        
    
    for i in range(nz ,n):
        arr[i] = 0
        
    
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


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZerosOptimized(arr, n)
for it in ans:
    print(it, end=' ')
print()




arr = [1,0,2,0,3,0,4,5]
n = len(arr)
print(moveZero(arr,n))
