def linearSearch(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return arr[i]
    
    return -1
        
        
arr = [1,2,3,4,5]
n=len(arr)
target = int(input("Enter a number"))
print(linearSearch(arr,n,target))