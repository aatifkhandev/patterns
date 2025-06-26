#include<bits/stdc++.h>
using namespace std;


 vector<int> findUnion(vector<int> &a, vector<int> &b) {
     
        vector<int>temp;
        // Your code here
        set<int>s;
        
        
        for(int i=0;i<a.size();i++){
            s.insert(a[i]);
        }
        
        
         for(int i=0;i<b.size();i++){
            s.insert(b[i]);
        }
        
        for(auto it : s){
            temp.push_back(it);
        }
        return temp;
    }

    int main(){
        vector<int>a = {1,1,2,2,2,4};
        vector<int>b = {2,2,4,4};
         vector < int > Union = findUnion(a,b);
  cout << "Union of arr1 and arr2 is  " << endl;
  for (auto & val: Union)
    cout << val << " ";
  return 0;
        
    }