// Import statements (if needed)
import java.util.*; // Example: for Scanner or other utility classes

// Class definition
public class Main {
     
     static int secondLargest(int arr[],int n){
        int largest = arr[0];
        int secondL=-1;
        for(int i=0;i<n;i++){
            if(arr[i]>largest){
                largest=arr[i];
            }
        }
        Arrays.sort(arr);

        for(int i=n-2;i>=0;i--){
            if(arr[i]!=largest){
                secondL=arr[i];
                break;
            }
        }
        return secondL;
    }

    public static void main(String[] args) {
        int arr[]={1,2,3,4,5};
        int n=5;
        System.out.println(secondLargest(arr,n));
    }
}
