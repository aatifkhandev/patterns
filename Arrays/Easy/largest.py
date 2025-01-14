#Finding largest element in an array

def FindLargest(arr,n):
    max=0
    for i in range(0,n):
        if max<arr[i]:
            max=arr[i]
    return max


arr=[1,2,3,4,5]
n=5
print(FindLargest(arr,n))