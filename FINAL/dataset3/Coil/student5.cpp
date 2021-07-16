#include <iostream>
using namespace std;

int main(){

int n,m;
cin >>n>>m;
// MEanignful comment
int vals[n][m]; //Double array

int Fr=0,Fc=0;
int Lr=n,Lc=m;

for (int i=0 ; i<=n ;i++){
    if (i!=n){
    for (int j=0;j<m;j++){
        cin >> vals[i][j];
    }}
}

while (Lr>=1 && Lc>=1){

for (int i=Fc;i<Lc+Fc;i++) {cout << vals[Fr][i] <<" ";}
    
for (int i=Fr+1;i<Fr+Lr;i++) cout << vals[i][Fc+Lc-1]<<" ";
if (not (Lr==1)) {for (int i=Fc-2+Lc ; i >= Fc;i--) cout << vals[Fr+Lr-1][i]<<" ";}
    
    if (not (Lc==1)) {for (int i = Fr+Lr-2;i>Fr;i--) {cout << vals[i][Fc]<<" ";}
        
    }
    
    Lr-=2;
    Lc-=2;
Fr++;
Fc++;

}
}
