#include <iostream>
#include <cstdio>
using namespace std;
void vulnerable_function()
{
    char buffer[256];
    cout << "Enter a string: ";
    cin >> buffer;
    fprintf(stdout, buffer);
}
int main()
{
    vulnerable_function();
    return 0;
}
