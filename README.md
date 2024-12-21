# SQL Injection Payload Tester

## Overview
The **SQL Injection Payload Tester** is a Python script designed to simulate a login system vulnerable to SQL injection attacks. This project demonstrates how SQL injection exploits insecure query handling and teaches secure coding practices to mitigate such vulnerabilities. By testing various payloads against the system, you can see how malicious inputs can bypass authentication or manipulate database queries.

This project is ideal for:
- Learning about SQL injection vulnerabilities.
- Understanding the importance of secure query practices.
- Educational and research purposes in cybersecurity.

## Features
- **In-Memory Database**: Uses SQLite to create and populate a temporary database.
- **Vulnerable Login Function**: Executes unsafe queries with string interpolation to demonstrate risks.
- **Payload Testing**: Reads payloads from an external file and tests them for successful exploitation.
- **Verbose Output**: Displays executed queries, payload results, and retrieved data.

## File Structure
```
project-directory/
|-- sql_injection_tester.py   # Main Python script
|-- payloads.txt              # File containing SQL injection payloads
|-- README.md                 # Project documentation
```

## Setup

### Prerequisites
Ensure the following are installed on your system:
- Python 3.7 or higher

### Installation
1. Clone or download this repository.
2. Create a `payloads.txt` file in the same directory as `sql_injection_tester.py`.
3. Populate `payloads.txt` with SQL injection payloads. Example contents:
   ```
   ' OR 1=1 --
   ' OR ''='
   -- or #
   " OR "1"="1
   admin' --
   ```

### Running the Script
1. Navigate to the project directory in your terminal or command prompt.
2. Execute the script:
   ```bash
   python sql_injection_tester.py
   ```
3. Observe the output in your terminal.

## Script Details

### Database Initialization
- The script creates an SQLite in-memory database with a `users` table containing sample user credentials.
- Sample data:
  | ID   | Username | Password   |
  |------|----------|------------|
  | 1    | admin    | admin123   |
  | 2    | user1    | password1  |
  | 3    | user2    | password2  |

### Vulnerable Login Function
The `vulnerable_login` function constructs and executes a SQL query using unsanitized inputs. This demonstrates how malicious inputs can inject harmful SQL code.

#### Query Format:
```sql
SELECT * FROM users WHERE username = '{input_username}' AND password = '{input_password}'
```

### Payload Testing
- The `test_payloads` function reads payloads from `payloads.txt` and passes them to `vulnerable_login`.
- Each payload is tested with a dummy password (`"any_password"`).
- The function prints whether the payload succeeded and, if successful, displays the retrieved rows.

### Sample Output
```text
Starting SQL Injection tests...

Testing payload: ' OR 1=1 --
Executing query: SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = 'any_password'
Payload succeeded! Retrieved rows: [(1, 'admin', 'admin123'), (2, 'user1', 'password1'), (3, 'user2', 'password2')]

Testing payload: admin' --
Executing query: SELECT * FROM users WHERE username = 'admin' --' AND password = 'any_password'
Payload succeeded! Retrieved rows: [(1, 'admin', 'admin123')]
```

## Key Learnings
This project emphasizes:
- **Risks of Insecure Query Handling**: Shows how improper handling of user inputs leads to SQL injection.
- **Best Practices**: Advocates for parameterized queries to mitigate risks.

## Mitigation Strategies
To prevent SQL injection in real-world applications:
1. **Parameterized Queries**: Use placeholders instead of concatenating inputs:
   ```python
   query = "SELECT * FROM users WHERE username = ? AND password = ?"
   cursor.execute(query, (input_username, input_password))
   ```
2. **Input Validation**: Validate and sanitize all user inputs to ensure they conform to expected formats.
3. **Least Privilege Principle**: Limit database user permissions to minimize damage from an exploited query.
4. **Regular Audits**: Periodically review code and queries for potential vulnerabilities.

## Security Disclaimer
This project is for educational purposes only. Do not use it to exploit vulnerabilities on systems you do not own or have explicit permission to test. Unauthorized use is unethical and illegal.

