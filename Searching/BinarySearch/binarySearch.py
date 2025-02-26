# # Binary search

def binarySearch(arr,n,target):
    low = 0
    high = n-1
    while low<=high:
        mid = (low + high) // 2 
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        elif arr[mid]>target:
            high = mid-1
    return -1



arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 17
n = len(arr)
print(binarySearch(arr,n,target))