# reverse an array
# arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}

# Solution 1: Using an extra array.

# Approach: Declare an array,ans[] of the same size as the input array. Iterate from the back of the input array while storing the elements in ans[]  in opposite direction.

def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    printArray(ans, n)

def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    

# Solution 2: Space-optimized iterative method

# Approach: Unlike the previous method we use the same array to obtain the result. Follow the steps below.

# Keep a pointer p1  at the first index and another p2 at the last index of the array. 
# Swap the elements pointed by p1 and p2, Post swapping increment p1 and decrement p2.
# This process is repeated for only the first n/2 elements where n is the length of array.    

def reverseOptimized(arr,n):
    l = 0
    r = n-1
    while(l>=r):
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1
    printArray(arr,n)
    
    
# solution 3: Recursive method


# Create a function that takes an array, start index, and end index of the array as parameters.
# Swap the elements present  at the start and end index, 
# The portion of the array left to be reversed is arr[start+1,end-1]. Make a recursive call to reverse the rest of the array. While calling recursion pass start +1  and ends - 1 as parameters for the shrunk array. Repeat step 2.
# Continue recursion as long as the ‘start < end’ condition is satisfied. This is the base case for our recursion.

def reverseRecursive(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseRecursive(arr, start + 1, end - 1)
    printArray(arr,n)



arr = [5, 4, 3, 2, 1]
arr2 = [3,7,8,9,1]
n = len(arr)
reverseOptimized(arr, n)
reverseRecursive(arr2,0,n-1)
