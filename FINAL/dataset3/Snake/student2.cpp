int max(int b[][10], int n, int i, int j, int min)
{
  if(b[i][j]==0||j==10||i==n)
  {
    return min;
  }
  else
  {
    min=min+b[i][j];
  }
  if(max(b,n,i+1,j,min)>max(b,n,i,j+1,min))
  {
    return max(b,n,i+1,j,min);
  }
  else
  {
    return max(b,n,i,j+1,min);
  }
}
#include <iostream>
using namespace std;

int main(){
int n;
cin >> n;
int a[n][10];
int i,j,m;
for(i=0;i<n;i++)
{
  for(j=0;j<10;j++)
  {
    cin >> a[i][j];
  }
}
cout << max(a,n,0,0,0);
}
