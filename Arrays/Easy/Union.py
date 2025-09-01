# // Input:
# // n = 5,m = 5.
# // arr1[] = {1,2,3,4,5}  
# // arr2[] = {2,3,4,4,5}
# // Output:
# //  {1,2,3,4,5}

# // Explanation: 
# // Common Elements in arr1 and arr2  are:  2,3,4,5
# // Distnict Elements in arr1 are : 1
# // Distnict Elemennts in arr2 are : No distinct elements.
# // Union of arr1 and arr2 is {1,2,3,4,5} 

def findUnion(arr1,arr2):
    s = set()
    temp = []
    for num in arr1:
        s.add(num)
        
    for num in arr2:
        s.add(num)
        
    for num in s:
        temp.append(num)
        
    return temp

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = findUnion(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)
   