from typing import List
def isSorted(arr:List[int],n:int)->int:
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
        
    return True

arr=[1,2,4]
n=len(arr)
print(isSorted(arr,n))