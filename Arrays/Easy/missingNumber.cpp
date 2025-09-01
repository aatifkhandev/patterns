// Find the missing number in an array

// Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.


// Example 1:
// Input Format: N = 5, array[] = {1,2,4,5}
// Result: 3
// Explanation: In the given array, number 3 is missing. So, 3 is the answer.

// Example 2:
// Input Format: N = 3, array[] = {1,3}
// Result: 2
// Explanation: In the given array, number 2 is missing. So, 2 is the answer.

//BruteForce

#include<bits/stdc++.h>
using namespace std;

int missingNumberBruteForce(int arr[], int n) {

    // Outer loop that runs from 1 to N:
    for (int i = 1; i <= n; i++) {

        // flag variable to check
        //if an element exists
        int flag = 0;

        //Search the element using linear search:
        for (int j = 0; j < n - 1; j++) {
            if (arr[j] == i) {

                // i is present in the array:
                flag = 1;
                break;
            }
        }

        // check if the element is missing
        //i.e flag == 0:

        if (flag == 0) return i;
    }

    // The following line will never execute.
    // It is just to avoid warnings.
    return -1;
}



int missingNumberHashing(int arr[], int n) {

    int hash[n + 1] = {0}; //hash array

    // storing the frequencies:
    for (int i = 0; i < n - 1; i++)
        hash[arr[i]]++;

    //checking the freqencies for numbers 1 to N:
    for (int i = 1; i <= n; i++) {
        if (hash[i] == 0) {
            return i;
        }
    }

    // The following line will never execute.
    // It is just to avoid warnings.
    return -1;
}


int missingNumberSum(int arr[], int n) {

    //Summation of first N numbers:
    int sum = (n * (n + 1)) / 2;

    //Summation of all array elements:
    int s2 = 0;
    for (int i = 0; i < n - 1; i++) {
        s2 += arr[i];
    }

    int missingNum = sum - s2;
    return missingNum;
}

int missingNumberXor(int arr[], int n) {

    int xor1 = 0, xor2 = 0;

    for (int i = 0; i < n - 1; i++) {
        xor2 = xor2 ^ arr[i]; // XOR of array elements
        xor1 = xor1 ^ (i + 1); //XOR up to [1...N-1]
    }
    xor1 = xor1 ^ n; //XOR up to [1...N]

    return (xor1 ^ xor2); // the missing number
}

int main(){
    int arr[] = {1,2,4,5};
    int n = 4;
    cout<<missingNumberSum(arr,n);
}