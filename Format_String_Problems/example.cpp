#include <regex>
#include <string>
#include <iostream>

int main() {
    std::string user_input;
    std::cin >> user_input;

    // Unsafe regex usage
    std::regex pattern(user_input);

    // Safe regex usage
    std::regex safe_pattern("^[a-zA-Z0-9]+$");

    return 0;
}
