#include <stdio.h>
#include <string.h>

int main() {
    // Vulnerability 1: Direct string concatenation with user input
    char username[50];
    char query[100];
    printf("Enter username: ");
    scanf("%s", username);
    // Direct string concatenation: Concatenates user input directly into SQL query
    sprintf(query, "SELECT * FROM users WHERE username = '%s'", username);
    printf("Query: %s\n", query);

    // Vulnerability 2: Unsafe buffer operations
    char password[50];
    printf("Enter password: ");
    scanf("%s", password);
    // Unsafe buffer operation: Using sprintf with unvalidated user input
    sprintf(query, "SELECT * FROM users WHERE username = 'admin' AND password = '%s'", password);
    printf("Query: %s\n", query);

    // Vulnerability 3: Unparameterized SQL query
    char user_id[50];
    printf("Enter user ID: ");
    scanf("%s", user_id);
    // Unparameterized query: Directly inserting user input into the query without sanitization
    sprintf(query, "SELECT * FROM users WHERE id = %s", user_id);
    printf("Query: %s\n", query);

    // Vulnerability 4: SQL query with unsafe concatenation in WHERE clause
    char email[50];
    printf("Enter email: ");
    scanf("%s", email);
    // Another direct string concatenation: Insecure query construction with email
    sprintf(query, "SELECT * FROM users WHERE email = '%s'", email);
    printf("Query: %s\n", query);

    // Vulnerability 5: Multiple unsafe operations in one function
    char phone_number[50];
    printf("Enter phone number: ");
    scanf("%s", phone_number);
    // Unparameterized query with user input directly inserted
    sprintf(query, "SELECT * FROM users WHERE phone = '%s' AND email = '%s'", phone_number, email);
    printf("Query: %s\n", query);

    return 0;
}
