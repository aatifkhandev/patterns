#find the number that appear once and other number's twice
# Input:
#  arr[] = {4,1,2,1,2}
# Result:
#  4

def findNum(arr):
    count=0
    for i in range(n):
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            
            return arr[i]
    
    return -1

def findNumOptimized(arr):
   
    n = len(arr)

    
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    for num, count in hashmap.items():
        if count == 1:
            return num

    return -1
    
       


arr = [4,1,2,1,2,4,7]
n = len(arr)
print(findNumOptimized(arr))
     
    