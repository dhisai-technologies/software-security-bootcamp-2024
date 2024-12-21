#include <stdio.h>
#include <string.h>

int main() {

    // Test Case 1: Direct String Concatenation Vulnerability
    {
        char username[100];
        printf("Enter username: ");
        scanf("%s", username);

        // Vulnerable code: Direct string concatenation
        char query[200];
        sprintf(query, "SELECT * FROM users WHERE username = '%s'", username);
        printf("Query 1: %s\n", query);
        // Vulnerable query generated: SELECT * FROM users WHERE username = '<user_input>'
    }

    // Test Case 2: Unsafe sprintf usage (SQL Injection)
    {
        char user_input[100];
        printf("Enter user ID: ");
        scanf("%s", user_input);

        // Vulnerable code: Unsafe sprintf usage
        char query[200];
        sprintf(query, "SELECT * FROM users WHERE id = %s", user_input);
        printf("Query 2: %s\n", query);
        // Vulnerable query generated: SELECT * FROM users WHERE id = <user_input>
    }

    // Test Case 3: Unsafe IN Clause (Dynamic query construction)
    {
        char id_list[100];
        printf("Enter list of IDs (comma-separated): ");
        scanf("%s", id_list);

        // Vulnerable code: Unsafe IN clause with dynamic input
        char query[200];
        sprintf(query, "SELECT * FROM users WHERE id IN (%s)", id_list);
        printf("Query 3: %s\n", query);
        // Vulnerable query generated: SELECT * FROM users WHERE id IN (<user_input>)
    }

    // Test Case 4: Unsafe String Concatenation with strcat
    {
        char user_input[100];
        printf("Enter search keyword: ");
        scanf("%s", user_input);

        // Vulnerable code: Unsafe string concatenation with strcat
        char query[200] = "SELECT * FROM products WHERE name LIKE '%";
        strcat(query, user_input);
        strcat(query, "%'");
        printf("Query 4: %s\n", query);
        // Vulnerable query generated: SELECT * FROM products WHERE name LIKE '%<user_input>%'
    }

    // Test Case 5: Unsafe Table Name Insertion in SQL Query
    {
        char table_name[100];
        printf("Enter table name: ");
        scanf("%s", table_name);

        // Vulnerable code: Unsafe table name insertion
        char query[200];
        sprintf(query, "SELECT * FROM %s WHERE condition = 'some_value'", table_name);
        printf("Query 5: %s\n", query);
        // Vulnerable query generated: SELECT * FROM <user_input> WHERE condition = 'some_value'
    }

    return 0;
}
