// Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
// Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0

#include<iostream>
#include<vector>
using namespace std;


void moveZeros(vector<int>& arr){
    vector<int>temp;
    
    for(int i=0;i<arr.size();i++){
        if(arr[i]!=0){
         temp.push_back(arr[i]);
        }
    }

    for(int i=0;i<temp.size();i++){
        arr[i] = temp[i];
    }

    for(int i = temp.size();i<arr.size();i++){
        arr[i] = 0;
    }


}

void moveZerosOptimized()



int main(){
   vector<int> arr = {1,0,2,0,3,0,4,0,5,0,6,0,7};
   moveZeros(arr);
   for(auto it : arr){
    cout<<it<<endl;
   }
}




//   int n = sizeof(arr) / sizeof(arr[0]);
      
    // cout<<moveZeros(arr);
//     for(int i=0;i<n;i++){
//     cout<<arr[i]<<endl;
//  }