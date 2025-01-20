from typing import List
# Move Negative numbers to end of array
#arr = [1,-2,-3,4,5,-6,7]

# def moveNumbers(arr:List[int],n:int)->int:

def swapOne(a,b):
    temp=a
    a=b
    b=temp
    return a,b
    
swapOne(4,1)
print(f'a = {a}, b = {b}')