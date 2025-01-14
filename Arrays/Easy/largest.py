from typing import List
#Finding largest element in an array

def FindLargest(arr:List[int],n:int)->int:
    max = arr[0]
    for i in range(1,n):
        if max<arr[i]:
            max = arr[i]
    return max


def main():
    arr = [1, 2, 3, 4, 5]
    n = len(arr)  
    print("The largest element in the array is:", FindLargest(arr, n))

if __name__ == "__main__":
    main()
    
    
# #include<bits/stdc++.h>

# using namespace std;

# int largest (int arr[], int n){
     
#      int max = INT_MIN;

#      for(int i=0;i<n;i++){
#         if(arr[i]>max){
#             max=arr[i];
#         }
#      }
#      return max;

# }



# int main(){
# int n;
# cout<<"enter the number of elements";
# cin>>n;
# int arr[n];

# for(int i=0;i<n;i++){
# cin>>arr[i];
# }
# largest(arr,n);
# for(int i=0;i<n;i++){
#     cout<<arr[i]<<endl;
# }

# }