from typing import List

#  Input : N = 3, k = 5, array[] = {2,3,5}
#  Result: 2
#  The longest subArray with sum 5 is {2, 3}. And its length is 2.

def longestSubArray(arr:List[int], n:int,k:int)->int:
    len = 0
    
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for K in range(i,j+1):
                sum+=arr[K]
                
            if(sum==k):
                 len = max(len,j-i+1)
    return len


def longestSubArrayNew(arr:List[int], n:int,k:int)->int:
    len = 0
    
    for i in range(n):
        sum=0
        for j in range(i,n):
            
            sum+=arr[j]
                
            if(sum==k):
                 len = max(len,j-i+1)
    return len


def longestSubArrayBetter(arr: [int], k: int) -> int:
    n = len(arr) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += arr[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return maxLen
            
            
            
            
            
arr = [2,3,5,1,9]
n = len(arr)
k = 10
print(longestSubArrayBetter(arr,k))