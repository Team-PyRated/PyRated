/*
##  Program by the other guy
 
##
##  Determine if a given series of numbers can be added or subtracted to give a target number
*/
#include <iostream>
using namespace std;



bool isAchievable(int target, int* arr, int n) {
  bool* added = new bool[n];
  for (int i = 0; i < n; ++i) {
    added[i] = false;
  }

  for (unsigned long long int k = 0; (k >> n) < 1; k++) {
    int sum = 0;
    for(int i = 0; i < n; ++i)
      sum += arr[i] * (((k >> i) & 1) ? 1 : -1);

    if (sum == target)
      return true;
    /*
    bool done = false;
    for (int i = 0; i < n; ++i) {
      if (added[i]) {
        added[i] = false;
        if (i == n - 1) done = true;
      } else {
        added[i] = true; break;
      }
    }

    if (done) break;*/
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

    cout << (isAchievable(target, arr, n) ? "Possible" : "Impossible") << '\n';
  }

  return 0;
}
