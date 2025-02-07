//i/p : arr = {1,1,1,2,2,2,3,3,3}
//o/p : arr = {1,2,3}

#include<bits/stdc++.h>
using namespace std;


int removeDup(int arr[],int n){
    set<int>set;
    for(int i=0;i<n;i++){
        set.insert(arr[i]);
    }
    int k = set.size();
    int j = 0;
    for(int x :set){
        arr[j++] =x;

    }
    return k;
}



int main(){
    int arr[] = {1,1,1,2,2,2,3,3,3};
   int n = sizeof(arr)/sizeof(arr[0]);
    int ans = removeDup(arr,n);

    for(int i=0;i<ans;i++){
        cout<<arr[i]<<endl;
    }
}