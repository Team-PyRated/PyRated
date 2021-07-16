/*
##  Program by the other guy
 
##
##  Determine if a given series of numbers can be added or subtracted to give a target number
*/
#include <iostream>
using namespace std;



bool isAchievable(int target, int* arr, int n) {

  for (unsigned long long int k = 0; (k >> n) < 1; k++) {
    int sum = 0;
    for(int i = 0; i < n; ++i)
      sum += arr[i] * (((k >> i) & 1) ? 1 : -1);

    if (sum == target)
      return true;
  }
  return false;
}

int main() {
  int n, target;

  cin >> n >> target;

  int* arr = new int[n];

  for (int testcase = 0; testcase < 3; ++testcase) {
    for(int i = 0; i < n; ++i)
      cin >> arr[i];

      
      bool ach = isAchievable(target, arr, n);
    
      if (ach) {cout << "Possible" << '\n';}
      else {cout << "Impossible" << '\n';}
  }

  return 0;
}
