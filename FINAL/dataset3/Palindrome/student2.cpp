#include <iostream>
using namespace std;

bool ispalin(char *b,int n)
{
  bool f=true;
  int i;
  for(i=0;i<n;i++)
  {
    if(b[i]!=b[n-i-1])
    {
      f=false;
    }
  }
  return f;
}


int main(){
int n,m;
cin >> n;
char a[n][n];
int i,j;
for(i=0;i<n;i++)
{
  cin >> a[i];
}
int count=0;
for(i=0;i<n;i++)
{
  bool flag=ispalin(a[i],n);
  if(flag)
  {
    count++;
  }
}
for(i=0;i<n;i++)
{
  bool k=true;
  for(j=0;j<n;j++)
  {
    if(a[j][i]!=a[n-1-j][i])
    {
      k=false;
    }
  }
  if(k)
  {
    count++;
  }
}
bool g=true;
for(i=0;i<n;i++)
{
  if(a[i][i]!=a[n-1-i][n-i-1])
  {
    g=false;
  }
}
if(g)
{
  count++;
}

g=true;
for(i=0;i<n;i++)
{
  if(a[i][n-1-i]!=a[n-1-i][i])
  {
    g=false;
  }
}
if(g)
{
  count++;
}
cout << count;
}
