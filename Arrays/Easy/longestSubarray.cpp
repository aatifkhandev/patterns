
// Input : N = 3, k = 5, array[] = {2,3,5}
// Result: 2
// The longest subarray with sum 5 is {2, 3}. And its length is 2.

// Input : N = 5, k = 10, array[] = {2,3,5,1,9}
// Result: 3
//  The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
#include<bits/stdc++.h>
using namespace std;


int longestSubarray(int arr[] , int k, int n){ //BruteForce : Generating all subArray's
 
 int len = 0;

 for(int i=0;i<n;i++){
    for(int j = i ;j<n; j++){

        int s = 0;

        for(int k=i;k<=j;k++){
            s+=arr[k];
        }
        if(s==k){
            len = max(len , j-i+1);
        }
    }
 }
 return len;
  
}



int main(){

int arr[] = {1, 2, 3, 4, 5};
int n = 5;
    int k = 5;
    int len = longestSubarray(arr, k , n) ;
    cout << "The length of the longest subarray is: " << len << "\n";
    return 0;

}