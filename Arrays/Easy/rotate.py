from typing import List
#Rotate an array left -> 1,2,3,4,5 : 2,3,4,5,1
#Rotate an array right -> 1,2,3,4,5 : 5,1,2,3,4

def rotateLeft(arr:List[int],n:int)->int:
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    
    for i in range(n):
        print(arr[i])


def rotateRight(arr:List[int],n:int)->None:
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = temp
    
    for i in range(n):
        print(arr[i])


    


arr = [1,2,3,4,5]
n = len(arr)
rotateRight(arr,n)   