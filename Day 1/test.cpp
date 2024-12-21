#include <iostream>
#include <string>
#include <sqlite3.h>

void get_user_info_vulnerable(std::string username) {
    sqlite3* db;
    sqlite3_open("example.db", &db);

    // Vulnerable SQL query using string concatenation
    std::string query = "SELECT * FROM users WHERE username = '" + username + "'";  // SQL Injection risk
    sqlite3_exec(db, query.c_str(), NULL, NULL, NULL);

    sqlite3_close(db);
}

void delete_user_vulnerable(int user_id) {
    sqlite3* db;
    sqlite3_open("example.db", &db);

    // Vulnerable SQL query using string formatting (f-string style equivalent in C++)
    std::string query = "DELETE FROM users WHERE id = " + std::to_string(user_id);  // SQL Injection risk
    sqlite3_exec(db, query.c_str(), NULL, NULL, NULL);

    sqlite3_close(db);
}

void update_password_vulnerable(std::string username, std::string new_password) {
    sqlite3* db;
    sqlite3_open("example.db", &db);

    // Vulnerable SQL query using old-style string formatting
    std::string query = "UPDATE users SET password = '%s' WHERE username = '%s'" % (new_password, username);  // SQL Injection risk
    sqlite3_exec(db, query.c_str(), NULL, NULL, NULL);

    sqlite3_close(db);
}

int main() {
    // Test the vulnerable functions with malicious input
    std::string malicious_username = "admin' OR '1'='1";  // SQL injection payload
    get_user_info_vulnerable(malicious_username);

    int malicious_user_id = 1;  // SQL injection to delete data
    delete_user_vulnerable(malicious_user_id);

    std::string malicious_password = "newpassword' OR '1'='1";  // SQL injection payload
    update_password_vulnerable(malicious_username, malicious_password);

    return 0;
}
