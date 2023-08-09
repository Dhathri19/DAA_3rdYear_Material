//Tiem complexity is O(n).

#include <stdio.h>
#include <iostream>
using namespace std;
int main(){
    int pos = -1;
    int key, array[10], n;

    cout<<"Enter the key:";
    cin>>key;
    
    cout<<"Enter the number of elements:";
    cin>>n;
    
    cout<<"Enter the array:";

    for(int i = 0; i < n; i++){
        cin>>array[i];
    }

    for(int i = 0; i < n; i++){
        cout<<array[i]<<" ";
    }

    for(int i = 0; i <= n; i++){
        if(array[i] == key){
            pos = i;
        }
    }

    cout <<"\nThe position is:"<<pos + 1;
}