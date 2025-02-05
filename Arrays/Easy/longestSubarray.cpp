
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

int longestSubarrayNew(int arr[] , int k, int n){ //BruteForce : Generating all subArray's
 
 int len = 0;

 for(int i=0;i<n;i++){
    int sum=0;
    for(int j = i ;j<n; j++){

       

        
            sum+=arr[j];
        
        if(sum==k){
            len = max(len , j-i+1);
        }
    }
 }
 return len;
  
}

int longestSubarrayBetter(vector<int>arr,long long k , int n){
    map<long long , int>preSum;
    long long sum = 0;
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        //calculate the prefix sum till index i:
        sum += arr[i];

        // if the sum = k, update the maxLen:
        if (sum == k) {
            maxLen = max(maxLen, i + 1);
        }
        // calculate the sum of remaining part i.e. x-k:
        long long rem = sum - k;
       
       if (preSum.find(rem) != preSum.end()) {
            int len = i - preSum[rem];
            maxLen = max(maxLen, len);
        }

        //Finally, update the map checking the conditions:
        if (preSum.find(sum) == preSum.end()) {
            preSum[sum] = i;
        }
}
return maxLen;
}

int longestSubarrayOptimal(vector<int>& arr, long long k) {
    int n = arr.size(); 

    int left = 0, right = 0; // 2 pointers
    long long sum = arr[0];
    int maxLen = 0;
    while (right < n) {
        // if sum > k, reduce the subarray from left
        // until sum becomes less or equal to k:
        while (left <= right && sum > k) {
            sum -= arr[left];
            left++;
        }

        // if sum = k, update the maxLen i.e. answer:
        if (sum == k) {
            maxLen = max(maxLen, right - left + 1);
        }

        // Move forward thw right pointer:
        right++;
        if (right < n) sum += arr[right];
    }

    return maxLen;
}


int main(){

vector<int>arr = {2,3,5,1,9};
int n = 5;
    long long  k = 10;
    int len = longestSubarrayOptimal(arr, k ) ;
    cout << "The length of the longest subarray is: " << len << "\n";
    return 0;

}