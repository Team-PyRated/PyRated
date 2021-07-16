#include <iostream>
using namespace std;

bool Pal(char A[], int n){

    for (int i=0;i<n/2;i++){
        if (A[i]!=A[n-i]){
            return false;
        }
    }
    return true;
}

int main(){

int n, r=0; cin>>n;
char words[n][n], t[n];
for (int i=0;i<n;i++){
    for (int j=0;j<n;j++){
        cin >> words[i][j];
    }
}

for (int i=0;i<n;i++){
    r += Pal(words[i],n);
    for (int j=0;j<n;j++){
        t[j] = words[j][i];}
    r+= Pal(t,n);
}

for (int i=0;i<n;i++){t[i] = words[i][i];}
r+= Pal(t,n);
for (int i=0;i<n;i++){t[i] = words[n-i-1][i];}
r+= Pal(t,n);
cout << r;
}
