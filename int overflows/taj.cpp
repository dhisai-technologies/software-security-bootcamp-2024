#include <iostream>

int main() {
    try {
        throw std::runtime_error("An error occurred");
    } catch (std::exception &e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    return 0;
}
