#include <iostream>
using namespace std;

int main(){
int n,m;
cin >> n >> m;
int a[n][m];
long i,j,k;
for(i=0;i<n;i++)
{
  for(j=0;j<m;j++)
  {
    cin >> a[i][j];
  }
}
int min;
if(m>n)
{
  min=n;
}
else
{
  min=m;
}
if(min%2==0)
{
for(k=0;k<(min/2);k++)
{
  for(i=k;i<m-k;i++)
  {
    cout << a[k][i] << " ";
  }
  for(j=k+1;j<n-k;j++)
  {
    cout << a[j][m-k-1] << " ";
  }
  for(i=m-k-2;i>k-1;i--)
  {
    cout << a[n-k-1][i] << " ";
  }
  for(i=n-k-2;i>k;i--)
  {
    cout << a[i][k] << " ";
  }
}
}
else
{
for(k=0;k<(min/2-1);k++)
{
  for(i=k;i<m-k;i++)
  {
    cout << a[k][i] << " ";
  }
  for(j=k+1;j<n-k;j++)
  {
    cout << a[j][m-k-1] << " ";
  }
  for(i=m-k-2;i>k-1;i--)
  {
    cout << a[n-k-1][i] << " ";
  }
  for(i=n-k-2;i>k;i--)
  {
    cout << a[i][k] << " ";
  }
}
for(i=k;i<m-k;i++)
  {
    cout << a[k][i] << " ";
  }
}
    return 0;
}
