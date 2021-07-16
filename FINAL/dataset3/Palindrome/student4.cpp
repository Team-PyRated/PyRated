//PALINDROME
#include <iostream>
using namespace std;


#define fori(x) for(int i = 0; i < x; i++)
#define forj(x) for(int j = 0; j < x; j++)

int main() {
	int n; cin >> n;
	char arr[n][n];
	fori(n) forj(n) cin >> arr[i][j];

	//array created
	int check = 0;
	int rcheck = 0, ccheck = 0, dcheck = 0;

	//ROWS
	for(int row = 0; row < n; row++) {
		fori(n) {
			if(arr[row][i] == arr[row][(n-1)-i]) check += 1;
			else check += 0;
		}
		if(check == n) rcheck += 1;
		check = 0;
	}

	//COLUMNS
	for(int column = 0; column < n; column++) {
		fori(n) {
			if(arr[i][column] == arr[(n-1)-i][column]) check += 1;
			else check += 0;
		}
		if(check == n) ccheck += 1;
		check = 0;
	}

	//DIAGONALS
	//D1
	fori(n) {
		if(arr[i][i] == arr[n-1-i][n-1-i]) check += 1;
		else check += 0;
	}
	if(check == n) dcheck += 1;
	check = 0;

	//D2
	fori(n) {
		if(arr[i][n-1-i] == arr[n-1-i][i]) check += 1;
		else check += 0;
	}
	if (check == n) dcheck += 1;
	cout << rcheck + ccheck + dcheck;

}

