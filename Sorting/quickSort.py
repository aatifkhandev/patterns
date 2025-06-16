def partition(arr,st,end):
    idx = st-1
    pivot = arr[end]
    for j in range(st,end):
        if arr[j]<=pivot:
            idx+=1
            arr[j],arr[idx] = arr[idx],arr[j]
        
        
    arr[end],arr[idx+1] = arr[idx+1],arr[end]
    return idx+1

def quickSort(arr,st,end):
    if st<end:
        pivIdx = partition(arr,st,end)
        quickSort(arr,st,pivIdx-1)
        quickSort(arr,pivIdx+1,end)
        

arr = [5,4,3,2,1]
n = len(arr)
st = 0
end = n-1
quickSort(arr,st,end)
print(arr)