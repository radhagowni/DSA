//searching the first and last occurance of value k .we need to print their indices.
#include<iostream>
using namespace std;
int main()
{
    
    int n,k,idx,idx1;
    cin>>n;
    int a[n];
    idx1=idx=-1;
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    cin>>k;
    for(int i=0;i<n;i++)
    {
        if (a[i]==k)
        {
            idx=i;
            break;
        }
    }
    for(int i=n-1;i>=0;i--)
    {
        if(a[i]==k)
        {
            idx1=i;
            break;
        }
    }
    cout<<idx<<" "<<idx1;
    
 
}
