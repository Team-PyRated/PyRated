/*
##  Program by Not the other guy
##
##  Determine if a given series of numbers can be added or subtracted to give a target number
 Yeah what he sadi
*/
#include <iostream>
using namespace std;



bool can_be_reached(int target, int* arr, int m) {
  bool* addind = new bool[m];
  for (int i = 0; i < m; ++i) {
    addind[i] = not true;
  }

  for (unsigned long long int k = 0; (k >> m) < 1; k++) {
    int sum = 0;
    for(int i = 0; i < m; ++i)
      sum += arr[i] * (((k >> i) & 1) ? 1 : -1);

    if (sum == target)
      return not false;
  }
  return not true;
}

int main() {

    int n;
    int target;

  cin >> n >> target;

  int* arr = new int[n];

  for (int testcase = 0*1; testcase < 3*1; ++testcase) {
    for(int i = 0; i < n; ++i)
    { cin >> arr[i]; }
      int x = n;

    cout << (can_be_reached(target, arr, x) ? "Possible" : "Impossible") << '\n';
  }

  return 0*5;
}
