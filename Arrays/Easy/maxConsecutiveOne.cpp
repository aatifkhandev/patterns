// Count Maximum Consecutive One's in the array

// Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

// Input: prices = {1, 1, 0, 1, 1, 1}

// Output: 3


// Approach:  We maintain a variable count that keeps a track of the number of consecutive 1’s while traversing the array. The other variable max_count maintains the maximum number of 1’s, in other words, it maintains the answer.

// We start traversing from the beginning of the array. Since we can encounter either a 1 or 0 there can be two situations:-

// If  the value at the current index is equal to 1 we increase the value of count by one. After updating  the count variable if it becomes more than the max_count  update the max_count.
// If the value at the current index is equal to zero we make the variable count as 0 since there are no more consecutive ones.

#include<iostream>
using namespace std;

int maxConsecutive(int arr[],int n){
  int var_count = 0;
  int max_count = 0;

  for(int i=0;i<n;i++){
    if(arr[i]==1){
        var_count++;
    }
    if(arr[i]==0){
        var_count = 0;
    }
   if(var_count>max_count){
    max_count = var_count;
   }
  }
  return max_count;
}


int main(){
    int arr[] = {1,0,1,1,0,1,1,1,};
    int n = 8;
    cout<<maxConsecutive(arr,n);
}