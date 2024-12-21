#include <iostream>
#include <cstring>
using namespace std;

void vulnerableFunction(const char* input) {
    char buffer[6];
    strcpy(buffer, input); // Vulnerable line: no bounds checking
    cout << "Buffer content: " << buffer << endl;
}

int main() {
    char largeInput[10];
    cout<<"buffer overflow example: \n";
    cout<<"enter name:";
    cin>>largeInput;
    vulnerableFunction(largeInput); // Trigger the vulnerability
    return 0;
}
