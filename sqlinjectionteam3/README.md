# Software Security Bootcamp 2024

SQL Injection Vulnerability Detection Tool

This is a Python-based tool designed to detect SQL injection vulnerabilities in C code. It checks for three common vulnerabilities:

1. Direct String Concatenation: When user input is directly concatenated into SQL queries.
2. Usage of the + Operator: When SQL queries are constructed using the + operator to combine user input.
3. Unparameterized Queries: Queries that directly include user input without using prepared statements or parameterized queries.

The tool will scan through the provided code and print the line number and the exact part of the code where the vulnerability is detected.

---

Table of Contents:

1. Installation
2. Usage
3. Functionality
4. Output
5. Test Cases
6. Contributing


---

Installation

Requirements:
- Python 3.x: Install Python from https://www.python.org/downloads/
- Text Editor: Use any text editor like VSCode, Sublime Text, or PyCharm for editing the code.

Steps to Install Python:
1. Download and install Python from the official website.
2. Make sure to add Python to your system's PATH during installation.
3. Verify the installation by running:
   python --version

---

Usage

Running the Script:
1. Clone or Download the Script to your local machine.
2. Run the script in the terminal:
   python detect_sql_injection.py
3. Modify the test cases in the script or provide your own C code for testing.

---

Functionality

This tool scans for three types of vulnerabilities:

1. Direct String Concatenation with User Input: Detects where user input is directly concatenated into SQL query strings.
   Example (vulnerable code):
   query = "SELECT * FROM users WHERE username = '" + username + "'"

2. Usage of the + Operator: Detects usage of the + operator to concatenate SQL queries with user input.
   Example (vulnerable code):
   query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

3. Unparameterized Queries: Identifies SQL queries where user input is directly included in the query, without using parameterized queries.
   Example (vulnerable code):
   query = "SELECT * FROM users WHERE id = " + user_id

The tool works by reading each line of the code and searching for patterns using regular expressions.

---

Output

When a vulnerability is detected, the script will output:
- Line number: The line of code where the vulnerability is found.
- Vulnerable code: The specific part of the code where the vulnerability occurs.
- Description: A brief explanation of the type of vulnerability.

Example Output:
Test Case 1: Direct String Concatenation
Direct string concatenation detected at line 3: 'query = "SELECT * FROM users WHERE username = '" + username + "'" in code: Test Case 1

Test Case 2: Usage of '+' Operator
Usage of '+' operator detected at line 3: 'query = "SELECT * FROM users WHERE username = 'admin' AND password = '" + password + "'" in code: Test Case 2

Test Case 3: Unparameterized Query
Unparameterized query detected at line 3: 'query = "SELECT * FROM users WHERE id = " + user_id' in code: Test Case 3

---

Test Cases

You can modify or add your own test cases in the script for scanning.

Test Case 1: Direct String Concatenation

username = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + username + "'"

Test Case 2: Usage of + Operator for SQL Queries

password = input("Enter password: ")
query = "SELECT * FROM users WHERE username = 'admin' AND password = '" + password + "'"

Test Case 3: Unparameterized Query

user_id = input("Enter user ID: ")
query = "SELECT * FROM users WHERE id = " + user_id

---

Contributing

If you'd like to contribute:
1. Fork the repository.
2. Create a branch for your feature or bug fix.
3. Implement your changes and commit them.
4. Push your branch to your fork and create a pull request.

---


