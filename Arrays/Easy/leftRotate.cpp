#include<iostream>
using namespace std;


void reverse_arr(int arr[],int st,int end){
   while(st<=end){
      int temp = arr[st];
      arr[st] = arr[end];
      arr[end] = temp;
      st++;
      end--;
   }
}

void leftRotateUsingReverse(int arr[],int n,int d){
   reverse_arr(arr,0,d-1);

   reverse_arr(arr,d,n-1);

   reverse_arr(arr,0,n-1);
}

// void leftRotate(int arr[],int n,int d){
 
//    d = d % n;
  
//    int temp[d];

//    for(int i=0;i<d;i++){
//       temp[i] = arr[i];
//    }

//    for(int i = d;i<n;i++){
//       arr[i-d] = arr[i];
//    }

//    for(int i = n-d;i<n;i++){
//       arr[i] = temp[i-(n-d)];
//    }


 
 
// }


int main(){
    int arr[] = {1,2,3,4,5,6,7};
    int n = 7;
    leftRotateUsingReverse(arr,n,3);
    for(int i=0;i<n;i++){
    cout<<arr[i]<<endl;
 }
}