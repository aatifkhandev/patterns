def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    return arr




arr = [5,4,3,2,1]
n = len(arr)
print(BubbleSort(arr))