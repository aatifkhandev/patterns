# Binary search

def binarySearch(arr,n,target):
    low = 0
    high = n-1
    mid = (low+high)//2
    while(low<=high):
        
        if(arr[mid]==target):
            
            return target-1
        
        elif(arr[mid]<target):
            low = mid+1
        elif(arr[mid]>target):
    
    
            high = mid-1
    return mid
    
    







arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
n = len(arr)
print(binarySearch(arr,n,target))