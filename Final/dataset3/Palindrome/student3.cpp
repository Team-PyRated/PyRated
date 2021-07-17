/*
##  Program by Varad Mahashabde
##
##  Check if any n-length line (row, column, major diagonal
##  in the 2D array is a palindrome and print the count of such lines
*/
#include <iostream>
using namespace std;

int main() {
  int n, no_of_palindromes = 0;
  char** arr;

  cin >> n;

  arr = new char*[n];
  for (int i = 0; i < n; ++i) {
    arr[i] = new char[n];
    for (int j = 0; j < n; ++j)
      cin >> arr[i][j];
  }

  // Check for row palindromes
  for (int i = 0; i < n; i++) {
    bool is_palindrome = true;

    for (int j = 0; j < n / 2 and is_palindrome; ++j)
      is_palindrome &= (arr[i][j] == arr[i][n - 1 - j]);

    if (is_palindrome)
      ++no_of_palindromes;
  }

  // Check for column palindromes
  for (int j = 0; j < n; j++) {
    bool is_palindrome = true;

    for (int i = 0; i < n / 2 and is_palindrome; ++i)
      is_palindrome &= (arr[i][j] == arr[n - 1 - i][j]);

    if (is_palindrome)
      ++no_of_palindromes;
  }

  // Check for palindrome in the main diagonal
  bool is_palindrome = true;

  for (int i = 0; i < n / 2 and is_palindrome; i++)
    is_palindrome &= (arr[i][i] == arr[n - 1 - i][n - 1 - i]);

  if (is_palindrome)
      ++no_of_palindromes;

  // Check for palindrome in the back diagonal
  is_palindrome = true;

  for (int i = 0; i < n / 2 and is_palindrome; i++)
    is_palindrome &= (arr[i][n - 1 - i] == arr[n - 1 - i][i]);

  if (is_palindrome)
      ++no_of_palindromes;

  cout << no_of_palindromes;

  for (int i = 0; i < n; ++i)
    delete[] arr[i];
  delete[] arr;

  return 0;
}
