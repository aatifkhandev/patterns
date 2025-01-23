from typing import List
# Move Negative numbers to end of array
#arr = [1,-2,-3,4,5,-6,7]

# def moveNumbers(arr:List[int],n:int)->int:

def swapOne(a,b):
    temp=a
    a=b
    b=temp
    return a,b
    
def moveNeg(arr:List[int],n:int)->int:
    j=n-1
    for i in range(len(arr)):
        if arr[i]<0:
            swapOne(arr[i],arr[j])
            j+=1
            
    return arr


arr=[1,-2,-3,4,5]
n=5
print(moveNeg(arr,n))