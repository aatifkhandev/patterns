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
            
            
            
            
arr = [1,2,3,4,5]
n = len(arr)
k = 5
print(longestSubArray(arr,n,k))