Problem Statement :

Create a parser that identifies injection risks in dynamic query construction. Your parser should detect:
    - String joining operations
    - List comprehension in queries
    - Dynamic WHERE usage

Manual:

INTRODUCTION

SQL injection is a critical security vulnerability that can expose sensitive data, compromise systems, and spread malicious software. E-commerce and applications handling personally identifiable information (PII) are particularly vulnerable. SQL injection attacks can occur even without direct access to a system’s backend, such as when open database ports (e.g., TCP/1433 for MS SQL, TCP/3306 for MySQL) are left exposed. These attacks can lead to the theft of private or financial data without needing elevated access. Legal liabilities can arise from compromised systems, such as under the California Online Privacy Protection Act, HIPAA, and the Sarbanes-Oxley Act. The Payment Card Industry Data Security Standard (PCI DSS) also requires protection against injection flaws. Healthcare and financial sectors are especially at risk, and an SQL injection could compromise not only data but entire server or network security, allowing attackers to escalate their attacks. Proper security measures and code reviews are essential to mitigate this risk.

AFFECTED LANGUAGES

Any programming language used to interface with a database can be affected! But mainly high-level languages such as Perl, Python, Ruby, Java, server page technologies (such as ASP, [ASP.NET](http://asp.net/), JSP, and PHP), C#, and [VB.NET](http://vb.net/) are vulnerable. Sometimes lower-level
languages, such as C and C++ using database libraries or classes can be compromised as well. Finally, even the SQL language itself can be sinful.

SIN EXPLAINED

The most common variant of the sin is very simple—an attacker provides your database application with some malformed data, and your application uses that data to build a SQL statement using string concatenation. This allows the attacker to change the semantics of the SQL query. People tend to use string concatenation because they don’t know there’s another, safer method, and let’s be honest, string concatenation is easy. Easy but wrong!
             
A less common variant is SQL stored procedures that take a parameter and simply execute the argument or perform the string concatenation with the argument and then execute the result.

SINS (Security Issues Needing Solutions)

SIN 1: Direct String Concatenation

What is it?

Using string concatenation to build SQL queries by directly incorporating user input.

How to Spot

- Look for `+` operator in query construction
- String concatenation using `+=`
- Direct insertion of variables into query strings

Example (Vulnerable Code)

```python
username = input("Username: ")
query = "SELECT * FROM users WHERE username = '" + username + "'"

```

Redemption

- Use parameterized queries
- Implement prepared statements

```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))

```

### SIN 2: Unsafe Buffer Operations

What is it?
Using unsafe string buffer operations in C++ that can lead to SQL injection.

How to Spot

- Usage of `strcat()`
- `sprintf()` for query construction
- Direct buffer manipulation with SQL strings

Example (Vulnerable Code)

```cpp
char query[100];
sprintf(query, "SELECT * FROM users WHERE id = %s", user_input);

```

Redemption

- Use prepared statements
- Implement input validation
- Use safe string handling functions

### SIN 3: Dynamic Query Construction

What is it?
Building complex queries dynamically using user input in WHERE clauses, JOINs, or subqueries.

How to Spot

- Multiple WHERE conditions built dynamically
- Dynamic JOIN conditions
- Subquery construction using string concatenation

Example (Vulnerable Code)

```python
filters = []
if user_input:
    filters.append(f"column = '{user_input}'")
query = f"SELECT * FROM table WHERE {' AND '.join(filters)}"

```

Redemption

- Use query builders with parameter binding
- Implement proper input validation
- Use ORM frameworks when possible

SIN 4: Unsafe List Operations

What is it?
Unsafe handling of IN clauses and array parameters in SQL queries.

How to Spot

- Dynamic list construction in IN clauses
- String concatenation with arrays
- Unparameterized list handling

Example (Vulnerable Code)

```python
ids = "1,2,3"  # User input
query = f"SELECT * FROM users WHERE id IN ({ids})"

```

Redemption

- Use parameterized queries with list expansion
- Implement proper array parameter handling
- Validate array inputs before processing

SIN 5: Unsafe String Formatting

What is it?
Using unsafe string formatting methods to construct SQL queries.

How to Spot

- f-strings in query construction
- %-formatting in SQL queries
- `.format()` method usage in queries

Example (Vulnerable Code)

```python
query = f"SELECT * FROM users WHERE username = '{username}'"
query = "SELECT * FROM users WHERE username = %s" % username

```

Redemption

- Use parameterized queries
- Implement query parameter binding
- Use database-specific escaping functions