#include <iostream>
using namespace std;
bool check(int b[], int i, int target)
{
  if(i==0)
  {
    if(b[i]==-target||b[i]==target)
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  int k=i-1;
  return (check(b,k,target-b[i])||check(b,k,target+b[i]));
}


int main(){
int n,target1;
cin >> n >> target1;
int a[10];
int b[10];
int c[10];
int i;
for(i=0;i<n;i++)
{
    cin >> a[i];
}
for(i=0;i<n;i++)
{
    cin >> b[i];
}
for(i=0;i<n;i++)
{
    cin >> c[i];
}
if(check(a,n-1,target1))
{
  cout << "Possible" << endl;
}
else
{
  cout << "Impossible" << endl;
}
if(check(b,n-1,target1))
{
  cout << "Possible" << endl;
}
else
{
  cout << "Impossible" << endl;
}
if(check(c,n-1,target1))
{
  cout << "Possible" << endl;
}
else
{
  cout << "Impossible" << endl;
}
    return 0;
}
