#include<iostream>
using namespace std;
int main()
{
   int n;
   cin>>n;
   string s;
    cin>>s;
    for(int i=0;i<n;i++)
    {
        if ((s[i]>='a')&& (s[i]<='z'))
        {
            s[i]=s[i]-32;
        }
        else if((s[i]>='A')&&(s[i]<='Z'))
        {
            s[i]=s[i]+32;
        }
    }
    cout<<s;
}