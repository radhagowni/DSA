#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int j=1;j<=n;j++)
    {
    for(int i=n;i>0;i--)
    {
        if(j!=i)
        {
        cout<<i;

        }
        else{
            cout<<"*";
        }
    }
    cout<<endl;
    }
}