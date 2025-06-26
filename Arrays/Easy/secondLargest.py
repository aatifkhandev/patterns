from typing import List
import sys
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


def secondLargestOptimized(arr:list[int],n:int)->int:
    largest=arr[0]
    secondLar = -1
    for i in range(n):
        if arr[i]>largest:
            secondLar=largest
            largest=arr[i]
        elif arr[i]>secondLar and arr[i]<largest:
            secondLar=arr[i]
    return secondLar

def secondSmallOptimized(arr:List[int],n:int)->int:
    smallest1 = arr[0]
    secondSmall1 = (sys.maxsize)
    for i in range(n):
        if arr[i]<smallest1:
            secondSmall1=smallest1
            smallest1=arr[i]
        elif arr[i]<secondSmall1 and arr[i]!=smallest1:
            secondSmall1=arr[i]
    return secondSmall1

arr=[1,2,3,4,5,6,7,8,9,10]
n=len(arr)
print(secondSmallOptimized(arr,n))