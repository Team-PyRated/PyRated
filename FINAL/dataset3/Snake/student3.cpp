/*
##  Program by Varad Mahashabde
##
##  Get the maximum length if the snake for a given 2D array
*/
#include <iostream>
using namespace std;

int getSnakeLength(int* arr, int n, int m, int position_x = 0, int position_y = 0) {
  if (position_x < 0 or position_x >= n or position_y < 0 or position_y >= m)
    return 0;

  int length_increase = arr[position_x*m + position_y];
  if (length_increase == 0)
    return 0;

  return length_increase + max(getSnakeLength(arr, n, m, position_x + 1, position_y),
                               getSnakeLength(arr, n, m, position_x, position_y + 1));
}

int main() {
  int n;
  int* arr;

  cin >> n;
  arr = new int[n*10];

  for (int i = 0; i < n; ++i)
    for (int j = 0; j < 10; ++j)
    cin >> arr[i * 10 + j];

  cout << getSnakeLength(arr, n, 10);

  return 0;
}
