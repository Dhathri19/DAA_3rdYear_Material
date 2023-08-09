#include<iostream> 
#include<algorithm> 
using namespace std; 
// A structure to represent a job 
struct Job 
{ 
char id;   
int dead; 
int profit; 
}; 
// This function is used for sorting all the jobs according to the profit 
bool compare(Job a, Job b) 
{ 
  return (a.profit > b.profit); 
} 
void jobschedule(Job arr[], int n) 
{ 
  // Sort all jobs according to decreasing order of prfit 
  sort(arr, arr+n, compare); 
  int result[n]; // To store result 
  bool slot[n];  
  // Initialize all slots to be free 
  for (int i=0; i<n; i++) 
    slot[i] = false; 
  for (int i=0; i<n; i++) 
  { 
  // Find a free slot for this job (Note that we start 
  // from the last possible slot) 
  for (int j=min(n, arr[i].dead)-1; j>=0; j--) 
  { 
    // Free slot found 
    if (slot[j]==false) 
    { 
      result[j] = i; // Add this job to result 
      slot[j] = true; // Make this slot occupied 
      break; 
    } 
  } 
  } 
  // Print the result 
  for (int i=0; i<n; i++) 
  if (slot[i]) 
    cout << arr[result[i]].id << " "; 
} 
int main() 
{ 
  Job arr[] = { {'a', 2, 20}, {'b', 2, 15}, {'c', 1, 10}, 
        {'d', 3, 5}, {'e', 3, 1}}; 
  int n = 5; 
  cout << "maximum profit sequence of jobs is-->"; 
  jobschedule(arr, n); 
   
} 