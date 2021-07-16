/*
##  Program by Varad Mahashabde
##
##  Print the entries of a 2D array in a coil pattern
*/
#include <iostream>
using namespace std;

int main() {
  int n, m;
  int** arr;

  cin >> n >> m;

  arr = new int*[n];
  for (int i = 0; i < n; ++i) {
    arr[i] = new int[m];
    for (int j = 0; j < m; ++j)
      cin >> arr[i][j];
  }

  int upper_bound = m, lower_bound = -1, left_bound = -1, right_bound = n;
  int direction[2] = {0,1}, position[2] = {0,0};

  while(upper_bound != lower_bound and left_bound != right_bound) {
    for(;  left_bound < position[0] and position[0] < right_bound and lower_bound < position[1] and position[1] < upper_bound; position[0] += direction[0], position[1] += direction[1])
        cout << arr[ position[0] ][ position[1] ] << ' ';
    // Check if we hit any of the walls
    if (not ( left_bound < position[0])) {
      ++position[0];
      ++lower_bound; ++position[1];
    }
    else if (not (position[0] < right_bound)) {
      --position[0];
      --upper_bound; --position[1];
    }
    else if (not (lower_bound < position[1])) {
      ++position[1];
      --right_bound; --position[0];
    }
    else if (not (position[1] < upper_bound)) {
      --position[1];
      ++ left_bound;  ++position[0];
    }

    int temp_0 = direction[0], temp_1 = direction[1];
    // Multiply direction by -i
    // direction = {direction[1], -direction[0]};
    direction[0] = temp_1;
    direction[1] = -temp_0;
  }

  for (int i = 0; i < n; ++i)
    delete[] arr[i];
  delete[] arr;

  return 0;
}

/*
##
##  GDB testing data :
##  Input :
3 3
1 2 3
4 5 6
7 8 9
##  Variable tracking commands :
display /d upper_bound
display /d lower_bound
display /d left_bound
display /d right_bound
display /d direction
display /d position
##
*/
