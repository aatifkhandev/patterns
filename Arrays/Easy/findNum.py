from typing import List
#find the number that appear once and other number's twice
# Input:
#  arr[] = {4,1,2,1,2}
# Result:
#  4

def findNum(arr:List[int],n:int)->int:
    count=0
    for i in range(n):
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            
            return arr[i]
    
    return -1


arr = [4,1,2,1,2]
n = len(arr)
print(findNum(arr,n))
     
    