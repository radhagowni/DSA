// A program to print the pattern
#include <iostream>
using namespace std;
int main()
{
    int rows;
    cout<<"Enter number of rows:"<<endl;
    cin>>rows;
    for(int i=1;i<=rows;i++)
    {
        for(int j=rows;j>0;j--)
        {
            if (i!=j)
            {
            cout<<j<<"";
            }
            else
            {
                cout<<"*";
            }
        }
        cout<<"\n";
    }
    return 0;
}
