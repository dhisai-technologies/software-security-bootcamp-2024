#include <iostream>
#include <cstdio>

void test_user_input_vulnerability() {
    char user_input[100];
    std::cout << "Enter some input: ";
    std::cin.getline(user_input, 100);  // Safe input
    printf(user_input);  // Unsafe: user input used directly in printf
}

void test_format_specifier_n() {
    int variable = 42;
    printf("%n", &variable);  // Unsafe: '%n' is a dangerous format specifier
}

void test_format_specifier_x() {
    int variable = 42;
    printf("%x", variable);  // Unsafe: '%x' can reveal memory content
}

void test_safe_input() {
    char user_input[100];
    std::cout << "Enter some input: ";
    std::cin.getline(user_input, 100);  // Safe input
    printf("%s", user_input);  // Safe: controlled format specifier
}

int main() {
    test_user_input_vulnerability();
    test_format_specifier_n();
    test_format_specifier_x();
    test_safe_input();
    return 0;
}
