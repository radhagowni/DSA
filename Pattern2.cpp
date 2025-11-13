//program to print the pattern
#include<iostream>
using namespace std;
int main()
{
    int n;
    // we need n value to know how many lines that pattern should consists of
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
