// code to check whether the given number is power of two or not
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    while(n%4==0)
    {
        n=n/4;
    }
    if(n==1)
    {
        cout<<"True";
    }
    else{
        cout<<"False";
    }
}
