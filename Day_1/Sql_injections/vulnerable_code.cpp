#include<iostream>
#include<string>
#include <mysql/mysql.h>
using namespace std;

// Function to generate the SQL query result
string generate_sql_query(string username, string password)
{
    return "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
}

// Function to simulate the login process
void login_user(string username, string password)
{
    string result = generate_sql_query(username, password);
    cout << " User Hacked details: " << result << endl;
}

int main()
{
    string user, pass;
    cout << "Enter Username:  ";
    cin >> user;
    cout << "Enter Password: ";
    cin >> pass;
    login_user(user, pass);
    return 0;
}

