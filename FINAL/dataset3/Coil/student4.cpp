#include <iostream>
using namespace std;

#define fori(x) for(int i = 0; i < x; i++)
#define forj(x) for(int j = 0; j < x; j++)


int main()
{
	int m,n;
	cin >> n >> m;
	int arr[n][m];

	fori(m) forj(n) cin >> arr[i][j]; 

	int k = 0, l = 0;
	while(k < n && l < m) {
		for(int i = l; i < m; i++) {
			cout << arr[k][i];
		}
		k++;
		for(int i = k; i < n; i++) {
			cout << arr[i][m-1];
		}
		m--;
		if(k < n) {
	 		for(int i = m - 1; i >= 0; i--) {
				cout << arr[n-1][i];
			}
			n--;
		}	
		if(l < m) {
			for(int i = n - 1; i >= k; i--) {
				cout << arr[i][l];
			}
			l++;
		}
	}
}

