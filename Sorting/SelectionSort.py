def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr




arr = [5,7,8,2,1]
print(SelectionSort(arr))