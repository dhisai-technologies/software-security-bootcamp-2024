#include <iostream>
#include <cstring>

void test_vulnerable_printf(char* user_input) {
    // Vulnerable usage of printf with user-controlled input
    printf(user_input);  // Unsafe
}

int main() {
    char user_input[100];
    std::cout << "Enter input: ";
    std::cin.getline(user_input, 100);
    test_vulnerable_printf(user_input);
    return 0;
}
