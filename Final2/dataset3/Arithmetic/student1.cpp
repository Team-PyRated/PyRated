#include <iostream>
using namespace std;


bool poss(int A[], int n, int t, int sum){
    if (n==0) {
        if (sum==t) return true;
        else return false;}

    return poss(&A[1], n-1, t, sum+A[0]) || poss(&A[1], n-1, t, sum-A[0]);
    }

int main(){

int n, t; cin >> n>> t;
int A[3][n];
for (int i=0;i<3;i++) {
    for (int j=0;j<n;j++){
        cin >> A[i][j];}}

for (int i=0;i<3;i++) {
    if (poss(A[i],n, t, 0)) cout << "Possible"<<"\n";
    else cout << "Impossible"<<"\n";}
}
