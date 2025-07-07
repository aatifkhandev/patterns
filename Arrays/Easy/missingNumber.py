def missingNumberOptimizedOne(arr):
    n = len(arr)
    expected_sum = (n*(n+1)//2)
    actual_sum = 0
    for i in range(n):
        actual_sum+=arr[i]
        
    return expected_sum-actual_sum
        




arr = [3,0,1]
print(missingNumber(arr))