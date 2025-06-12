def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if arr[j]<arr[minIndex]:
                minIndex = j
        arr[j],arr[minIndex] = arr[minIndex],arr[j]
                
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    return arr



arr = [9,0,5,19,1000,454565]
BubbleSort(arr)
print("Hi")
print(arr)