#include <stdio.h>
#include <iostream>
using namespace std;
int main(){

    int array[100];
    int n, value;

    cout << "Enter size:";
    cin >> n;

    cout << "Enter the array:";
    for(int i = 0; i < n; i++){
        cin >> array[i];
    }

    cout << "Enter value to search:";
    cin >> value;

    int low = 0;
    int high = n - 1;
    int mid = 0;

    while(low <= high){
        mid = (low + high)/2;
        if(value > array[mid]){
            low = mid + 1;
        }
        else if(value < array[mid]){
            high = mid - 1;
        }
        else if(value == array[mid]){
            cout << "Element found: " << (mid + 1);
            exit(0);
        }
    }

    cout << "Element not found.";
    return 0;
}