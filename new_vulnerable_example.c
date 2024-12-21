
#include <stdio.h>

int main() {
    char buffer[100];
    char user_input1[50];
    char user_input2[50];

    
    gets(user_input1);  
    gets(user_input2);  

    
    printf(user_input1); 
    sprintf(buffer, user_input2); 
    scanf(user_input1); 

    return 0;
}
