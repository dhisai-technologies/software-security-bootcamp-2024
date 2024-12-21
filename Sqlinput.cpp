#include <iostream>
#include <cstring>
int main(){
    char buffer[50];
    char input1[]="Hello";
    char input2[]="World!";
    strcat(buffer,input1);
    strcat(buffer,input2);
    std::cout << "Concatenated String: " << buffer << std::endl;
    return 0;

}