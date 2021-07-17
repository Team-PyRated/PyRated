#include <iostream>
using namespace std;
#define fori(x) for(int i = 0; i < x; i++)
#define forj(x) for(int j = 0; j < x; j++)

//int sum = 0;


void merge(int U[], int V[], int lu, int lv, int S[]) {
	int uf = 0, vf = 0;
	fori(lu+lv) {
		if(uf<lu && vf<lv) {
			if(U[uf] < V[vf]) {S[i] = U[uf]; uf++;}
			else {S[i] = V[vf]; vf++;}
		}
		else if (uf<lu) {S[i] = U[uf]; uf++;}
		else {S[i] = V[vf]; vf++;}
	}
}

void ms(int a[], int n) {
	if(n == 1) return;
	int h = n/2;
	int U[h], V[n-h];
	fori(h) U[i] = a[i];
	fori(n-h) V[i] = a[i+h];
	ms(U,h); ms(V,n-h);

	merge(U, V, h, n-h, a);
}


void check_sum(int a[], int m, int n, int sum, int count) {  //MAKE SUM = 0 everytime
	if(n > 0) {
		if(sum <= m) {
			sum += a[count];
			count++;
			//cout << "Sum = " << sum << "  Count = " << count << "  "<< "  n = " << n;
			check_sum(a, m, n-1, sum, count); 
		}

		else if(sum > m) {
			sum -= a[count];
			count++;
			//cout << "Sum = " << sum << "  Count = " << count << "  n = " << n;
			check_sum(a, m, n-1, sum, count);
		}
	}
	if(n == 0 && sum == m) cout << "Possible" << endl;
	else if(n == 0 && sum != m) cout << "Not possible" << endl;
}



int main(){
	int n, t;
	cin >> n >> t;
	
	int a[1000], b[1000], c[1000];
	fori(1000) a[i] = 0;
	fori(n) cin >> a[i];
	fori(n) cin >> b[n];
	fori(n) cin >> c[n];

	ms(a, n);
	ms(b, n);
	ms(c, n);
	//fori(n) cout << a[i] << ' ';
	check_sum(a, t, n, 0, 0);
	check_sum(b, t, n, 0, 0);
	check_sum(c, t, n, 0, 0);
	//cout << "answer: " << check_sum(a, t, n, 0, 0);
} 
