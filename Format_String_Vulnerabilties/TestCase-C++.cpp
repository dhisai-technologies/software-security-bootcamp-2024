#include <iostream>
#include <cstdio>
using namespace std;
int main() {
    char *userInput="username";
    std::printf(userInput);
    std::fprintf("%s",stdout,userInput);
    return 0;
}