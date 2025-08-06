# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the largest element in the array. 


def largest(arr):
    ans = max(arr)
    return ans
    # n = len(arr)
    # max = arr[0]
    # for i in range(n):
    #     if arr[i]>max:
    #         max = arr[i]
    # return max

def secondLargest(arr):
    max = arr[0]
    secondL = -1
    for i in range(len(arr)):
        if arr[i]>max:
            secondL = max
            max = arr[i]
        elif arr[i]>secondL and arr[i]!=max:
            secondL = arr[i]
            
    return secondL

def secondSmallest(arr):
    min_value  = arr[0]
    secondS = float('inf')
    for i in range(len(arr)):
        if arr[i]<min_value:
            secondS = min_value
            min_value = arr[i]
        elif arr[i]<secondS and arr[i]!=min_value:
            secondS = arr[i]
    return secondS

def sorted_arr(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
        
    return True

def removeDup(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1     
            arr[i] = arr[j]
    return i+1
    
# move zeros
# def moveZeros(arr):
#      i = 0
#      for j in range(len(arr)):
#          if(arr[j]!=0):
#              arr[i]=arr[j]
#             i+=1

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
    
arr = [1,2,3,4,5]
target = int(input("Enter the target : "))
print(linearSearch(arr,target))

