#include <iostream>
using namespace std;

bool isthere1(char a[][1], char c[],int n1)
{
  for(int i=0;i<n1;i++)
  {
    bool k=true;
    for(int j=0;j<1;j++)
    {
      if(a[i][j]!=c[j])
      {
        k=false;
      }
    }
    if(k)
    {
      return true;
    }
  }
  return false;
}
bool isthere2(char b[][2], char c[], int n2)
{
  for(int i=0;i<n2;i++)
  {
    bool k=true;
    for(int j=0;j<2;j++)
    {
      if(b[i][j]!=c[j])
      {
        k=false;
      }
    }
    if(k)
    {
      return true;
    }
  }
  return false;
}
bool isptable(char a[][1], char b[][2], char w[], int i, int n1, int n2)
{
  if(i==0)
  {
    if(isthere1(a,w,n1))
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  if(i==1)
  {
    if(isthere2(b,w,n2))
    {
      return true;
    }
    else
    {
      return false;
    }
  }
  char char1[1];
  char char2[2];
  char1[0]=w[i];
  char2[0]=w[i-1];
  char2[1]=w[i];
  if(isptable(a,b,w,i-1,n1,n2)&&isthere1(a,char1,n1))
  {
    return true;
  }
  if(isptable(a,b,w,i-2,n1,n2)&&isthere2(b,char2,n2))
  {
    return true;
  }
  return false;
}

int main(){
int n1,n2,m;
cin >> n1 >> n2 >> m;
char o[15][1];
char t[15][2];
char word[10][6];
for(int i=0;i<n1;i++)
{
  for(int j=0;j<1;j++)
  {
    cin>>o[i][j];
  }
}
for(int i=0;i<n2;i++)
{
  for(int j=0;j<2;j++)
  {
    cin>>t[i][j];
  }
}
for(int i=0;i<m;i++)
{
  cin >> word[i];
}
cout << word[0] << endl;
for(int i=0;i<m;i++)
{
  if(isptable(o,t,word[i],5,n1,n2))
  {
    cout << "Can" << endl;
  }
  else
  {
    cout << "Cannot" << endl;
  }
}

}
