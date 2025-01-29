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



arr = [1,0,2,0,3,0,4,5]
n = len(arr)
print(moveZero(arr,n))
