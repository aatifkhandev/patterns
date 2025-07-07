
def missingNumberBrute(arr):
    for i in range(len(arr)):
        found = False
        for j in range(len(arr)):
            if arr[j]==i:
                found = True
                break
        if found==False:
            return i

def missingNumberBetter(arr):
    n = len(arr)
    hash = [0] * (n + 2)  # size n+2 avoids IndexError
    for i in range(n):
        hash[arr[i]] += 1

    for i in range(n + 2):
        if hash[i] == 0:
            return i




        

def missingNumberOptimizedOne(arr):
    n = len(arr)
    expected_sum = (n*(n+1)//2)
    actual_sum = 0
    for i in range(n):
        actual_sum+=arr[i]
        
    return expected_sum-actual_sum
        




arr = [1,2,4]
print(missingNumberBetter(arr))