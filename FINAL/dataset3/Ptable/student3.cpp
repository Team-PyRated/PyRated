/*
##  Program by Varad Mahashabde
##
##  Confirm whether a given string can be printed using the elements of a given periodic table
*/
#include <iostream>
using namespace std;

/*
// Apparently, std::swap exists
template <typename T>
void swap(T& a, T& b) {
  T temp = a;
   a = b;
   b = temp;
}*/

template <typename T>
void quickSort(T* arr, int end, int start,  bool f(const T&, const T&)) {
  if (end - start <= 1)
    return;

  int marker = start;

  for (int i = start; i < end; ++i)
    if ( f(arr[i], arr[end - 1]) ) {
      swap<T>(arr[i], arr[marker]);
      marker++;
    }
  swap<T>(arr[end - 1], arr[marker]);

  quickSort(arr, marker, start, f);
  quickSort(arr, end, marker + 1, f);

}

template <typename T>
int binarySearch(const T& candidate, const T* arr, int n, bool f(const T&, const T&)) {
  // f is a less than type operation i.e. f(a,a) = false
  // and if f(a,b) = f(b,a) = false iff a == b
  int lower_bound = 0, upper_bound = n, index;

  do {
    index = lower_bound / 2 + upper_bound / 2 + (upper_bound & 1 + lower_bound & 1) / 2;

    if ( f(arr[index], candidate))
      lower_bound = index;
    else if (f(candidate, arr[index]))
      upper_bound = index;
    else
      return index;

  } while(upper_bound - lower_bound > 1);

  if ( arr[lower_bound] == candidate)
    return lower_bound;
  if ( arr[upper_bound] == candidate)
    return upper_bound;

  return -1;
}

template <typename T>
int linearSearch(const T& candidate, const T* arr, int n) {
  for (int i = 0; i < n; ++i)
    if(arr[i] == candidate)
      return i;
  return -1;
}

bool singleCompare(const char& a, const char& b) {
  if ( (('a' <= a and a<= 'z') or ('A' <= a and a <= 'Z')) and (('a' <= b and b <= 'z') or ('A' <= b and b <= 'Z')) ) {
    char mod_a = a - ((a >= 'a') ? ('a' - 'A') : 0),
         mod_b = b - ((b >= 'a') ? ('a' - 'A') : 0);
    return mod_a < mod_b;
  }
  else
    return a < b;
}

struct dl {
  char letters[3];
  char& operator[](int n) {
    return letters[n];
  }
  const char& operator[](int n) const {
    return letters[n];
  }
  bool expandedCharEqual(const char& a, const char& b) const {
    return (singleCompare(a,b) == false) and (singleCompare(b,a) == false);
  }
  bool operator==(const dl& a) const {
    return letters[0] == a[0] and letters[1] == a[1];
  }
};

bool doubleCompare(const dl& a, const dl& b) {
  if (singleCompare(a[0], b[0]) == false and singleCompare(b[0], a[0]) == false)
    return singleCompare(a[1], b[1]);
  else return singleCompare(a[0], b[0]);
}

char convertToLowercase(char c) {
  if ('A' <= c and c <= 'Z')
    return c + 32;
}

bool isChemicallyFeasible(char word[], int word_length, char single_letter[], int n_single_letter, dl double_letter[], int n_double_letter, int checked_till = 0) {
  if (checked_till >= word_length)
    return true;

  dl temp;
  temp[0] = word[checked_till]; temp[1] = word[checked_till + 1]; temp[2] = '\0';

  bool single_possible = (linearSearch(word[checked_till], single_letter, n_single_letter) != -1),
       double_possible = (linearSearch(temp, double_letter, n_double_letter) != -1);

  if (checked_till == word_length - 1)
    return (single_possible and isChemicallyFeasible(word, word_length, single_letter, n_single_letter, double_letter, n_double_letter, checked_till + 1));

  return (single_possible and isChemicallyFeasible(word, word_length, single_letter, n_single_letter, double_letter, n_double_letter, checked_till + 1))
      or (double_possible and isChemicallyFeasible(word, word_length, single_letter, n_single_letter, double_letter, n_double_letter, checked_till + 2));
}

int main() {
  int n_single_letter, n_double_letter, no_of_testcases;
  char*    single_letter;
  dl* double_letter;
  char word[6 + 1];

  cin >> n_single_letter >> n_double_letter >> no_of_testcases;

  single_letter = new char[n_single_letter];
  double_letter = new dl[n_double_letter];

  for (int i = 0; i < n_single_letter; ++i)
    cin >> single_letter[i];
  for (int i = 0; i < n_double_letter; ++i) {
    cin >> double_letter[i][0] >> double_letter[i][1];
    double_letter[i][2] = '\0';

    double_letter[i][0] = convertToLowercase(double_letter[i][0]);
    double_letter[i][1] = convertToLowercase(double_letter[i][1]);

  }
  /*
  quickSort<char>(single_letter, n_single_letter, 0, singleCompare);
  quickSort<dl>(double_letter, n_double_letter, 0, doubleCompare);
  */
  while(no_of_testcases-- > 0) {
    //cin.getline(word, 6);
    cin >> word;
    for (int i = 0; i < 6; ++i)
      word[i] = convertToLowercase(word[i]);

    cout << (isChemicallyFeasible(word, 6, single_letter, n_single_letter, double_letter, n_double_letter) ? "Can" : "Cannot") << '\n';
  }

  /*
  for (int i = 0; i < n_single_letter; ++i)
    cout << single_letter[i] << ' ';
  cout << '\n';
  for (int i = 0; i < n_double_letter; ++i)
    cout << double_letter[i].letters << ' ';
  */

  return 0;
}
