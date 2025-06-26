def merge(arr,start,mid,end):
    temp = []
    i = start
    j = mid+1
    while i<=mid and j<=end:
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
            
    while i<=mid:
        temp.append(arr[i])
        i+=1
        
    while(j<=end):
        temp.append(arr[j])
        j+=1
        
    for idx in range(len(temp)):
        arr[idx+start] = temp[idx]




def MergeSort(arr,start,end):
    if start<end:
        mid = start+(end-start)//2
        MergeSort(arr,start,mid)
        MergeSort(arr,mid+1,end)
        merge(arr,start,mid,end)
        
arr = [5,4,3,2,1]
n = len(arr)
MergeSort(arr,0,n)
# for i in range(len(arr)):
#     print(i)
#     print()