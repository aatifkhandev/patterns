from typing import List
def removeDup(arr:List[int],n:int)->int:
    i=0
    for j in range(1,len(arr)):
        if(arr[i]!=arr[j]):
            i+=1
            arr[i]=arr[j]
            
    return i+1
        
        
        



arr = [1,1,2,2,2,3,3,3]
n = len(arr)
ans=removeDup(arr,n)
for i in range(ans):
    print(arr[i],end="")
    