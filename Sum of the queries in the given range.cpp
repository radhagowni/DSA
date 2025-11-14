// to find the sum in the given range
#include<iostream>
using namespace std;
int main()
{
    int n,queries;
    int first,last;
    cin>>n;
    int a[n];
    int s[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    s[0]=a[0];
    for(int i=1;i<n;i++)
    {
       s[i]=a[i]+s[i-1];
    }
    
    
    cin>>queries;
    for(int j=0;j<queries;j++)
    {
       cin>>first>>last; 
   
    if(first==0)
    {
        cout<<s[last];
    }
    else{
        cout<<s[last]-s[first-1];
    }
    }
}
