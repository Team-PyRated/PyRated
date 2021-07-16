

int eat(int x, int y, int A[][10], int n){
    if (A[x][y]==0) return 0;
    int a, b;
    if (y<9 && x<n-1){
        a = eat(x+1,y,A,n);
        b = eat(x,y+1,A,n);
        if (a > b){
        return a + A[x][y];
        }
        else {return b + A[x][y];}
    }
    if (x<n-1) return eat(x+1,y,A,n) + A[x][y];
    if (y<9) return eat(x+1,y,A,n) + A[x][y];
    return A[x][y];
    }


#include <iostream>
using namespace std;
int main(){

int n; cin >> n;
int vals[n][10];
for (int i=0;i<n;i++){
    for (int j=0;j<10;j++){
        cin >> vals[i][j];
    }
}

cout << eat(0,0,vals,n);
}
