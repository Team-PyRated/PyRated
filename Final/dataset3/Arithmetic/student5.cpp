#include <iostream>
using namespace std;
/* totally made by me. */

bool poss(int array[], int n, int x, int sum){
    
    if (n==0) {
        if (sum==x){
            return true;
        }
        else return false;
        // Na legit I didn't cheat.
    }

    return poss(&array[1], n-1, x, sum-array[0]) || poss(&array[1], n-1, x, sum+array[0]);
    }

int main(){

int n, m;
cin >> n >> m;

int arr[3][n];

for (int i=0;i<3;i++)
{
    
    for (int j=0;j<n;j++)
{
        
        cin >> arr[i][j];
    }
}

for ( int i=0; i < 3; i++)  {
    
    if (poss(arr[i],n, m, 0)){
        cout << "Possible"<<"\n";
    }
    
    else cout << "Impossible"<<"\n";
}
}
