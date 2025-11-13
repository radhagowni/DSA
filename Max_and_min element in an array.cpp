// Finding maximum and minimum element in an array
#include<iostream>
using namespace std;
int main()
{
    int max,min;
    int n;
    cin>>n; // taking the input from user
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    min=a[0];
    for(int i=1;i<n;i++)
    {
        if (a[i]<min)
        {
            min=a[i];
        }
    }
    max=a[0];
    for(int i=1;i<n;i++)
    {
        if (a[i]>max)
        {
            max=a[i];
        }
    }
    cout<<min<<" "<<max;
    
}
