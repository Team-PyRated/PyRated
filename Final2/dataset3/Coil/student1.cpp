#include <iostream>
using namespace std;

int main(){

int n,m;
cin >>n>>m;

int vals[n][m], Fr=0,Fc=0,Lr=n,Lc=m;
for (int i=0;i<n;i++){
    for (int j=0;j<m;j++){
        cin >> vals[i][j];
    }
}

while (Lr>=1 && Lc>=1){
    for (int i=Fc;i<Fc+Lc;i++) cout << vals[Fr][i] <<" ";
    for (int i=Fr+1;i<Fr+Lr;i++) cout << vals[i][Fc+Lc-1]<<" ";
    if (Lr!=1) {for (int i=Fc+Lc-2;i>=Fc;i--) cout << vals[Fr+Lr-1][i]<<" ";}
    if (Lc!=1) {for (int i=Fr+Lr-2;i>Fr;i--) cout << vals[i][Fc]<<" ";}
	Fr++;Fc++;
    Lr-=2;Lc-=2;
}
}
