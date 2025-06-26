# arr = 1 1 1 2 3 
# count 1 -> 3

def count(number,arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i]==number:
            cnt+=1
    return cnt

arr = [1,1,1,2,3]
number = 1
print(count(number,arr))