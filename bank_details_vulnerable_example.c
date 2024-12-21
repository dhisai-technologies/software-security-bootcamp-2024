
#include <stdio.h>

int main() {
    char account_number[20];
    char account_holder_name[50];
    char bank_details[100];

    
    gets(account_number);  
    gets(account_holder_name);  

    
    printf(account_holder_name); 
    sprintf(bank_details, account_number); 
    scanf(account_holder_name); 

    return 0;
}
