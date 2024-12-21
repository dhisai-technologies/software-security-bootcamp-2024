#include <iostream>
using namespace std;

int main() {
    int a = 2147483647; 
    int b = 1;
    int c = a + b; 

    int x = 0;
    int y = -1;
    int z = x - y; 

    long long_val = 12345678901234;
    int unsafe_cast = (int) long_val; 

    unsigned int u = 4294967295;
    int v = (int) u; 
    return 0;
}
