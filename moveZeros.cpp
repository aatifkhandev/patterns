#include<bits/stdc++.h>
#include<vector>
using namespace std;

//naive approach -> O(N)

void pushZeros(vector<int>arr){
    int n = arr.size();
    vector<int>nonZeros(n);
    int j = 0;
    for(int i =0;i<n;i++){
        if(arr[i]!=0){
            nonZeros[j++] = arr[i];
        }
    }

}

int main(){
    int arr[]={1,2,0,4,3,0,5,0};
    int n = 8;
    moveZeros(arr,n);
}