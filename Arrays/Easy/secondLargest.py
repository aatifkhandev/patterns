from typing import List
# Finding Second Largest number in an array

#  [1,2,3,4,5]
#  Second Smallest : 2
# 	Second Largest : 4

def secondLargest(arr:List[int],n:int)->int:
    secL=0
    largest = arr[0]
    for i in range(n):
        if arr[i]>largest:
            largest=arr[i]
    
    arr.sort(reverse=False,key=None)    
    for i in range(n-2,-1,-1):
        if arr[i]!=largest:
            secL=arr[i]
            break
    return secL



def secondSmall(arr:List[int],n:int)->int:
    
    smallest = arr[0]
    for i in range(n):
        if arr[i]<smallest:
            smallest=arr[i]
    
    arr.sort()    
    for i in range(n):
        if arr[i]!=smallest:
            return arr[i]
            
    return -1

arr=[1,2,3,4,5]
n=5
print(secondSmall(arr,n))