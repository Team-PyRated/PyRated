#include <iostream>
using namespace std;

//Rehmat Singh Chawla, 200260039

bool asElements(char A[], int l, char el1[], char el2[][2], int n1, int n2){
    if (l<=0) return true;

    bool t1=false,t2=false;

    for (int i=0;i<n1;i++){
        if (el1[i]==A[0]) {t1=true;break;}  }

    if (l>=2) {
        for (int i=0;i<n2;i++){
            if (el2[i][0]==A[0] && el2[i][1]==A[1]) {t2=true;break;}  }  }

    return (t1 && asElements(&A[1], l-1, el1, el2, n1, n2)) || (t2 && asElements(&A[2], l-2, el1, el2, n1, n2));
}

int main(){
int n1,n2,m, length=6; cin >> n1>>n2>>m;

char el1[n1], el2[n2][2], words[m][length];

for (int i=0;i<n1;i++) {
    cin >> el1[i];}

for (int i=0;i<n2;i++) {
    for (int j=0;j<2;j++){
        cin >> el2[i][j];}}

for (int i=0;i<m;i++) {
    for (int j=0;j<length;j++){
        cin >> words[i][j];}}

for (int i=0;i<m;i++) {
    if (asElements(words[i],length, el1, el2, n1, n2)) cout << "Can"<<"\n";
    else cout << "Cannot"<<"\n";
    }
}
