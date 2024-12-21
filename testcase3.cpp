#include <iostream>using namespace std;

int main() {
    int x = INT_MAX;
    try {
        x = x + 1;
        cout << "Test failed: Overflow not handled" << endl;
    } catch (...) {
        cout << "Overflow detected and handled" << endl;
    }
    return 0;
}