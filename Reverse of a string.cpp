// to reverse the string using strlen function
#include<iostream>
#include<string>
using namespace std;
int main()
{
    string st;
    cin>>st;
    for(int i=(strlen(st))-1;i>=0;i--)
    {
        cout<<st[i];
    }
}
