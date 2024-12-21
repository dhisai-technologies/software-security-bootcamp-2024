username = input("Enter username: ")
password = input("Enter password: ")
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"


print(f"Constructed query (unsafe): {query}")


user_input = input("Enter a user input for query2: ")  # Define user_input
query2 = "SELECT * FROM users WHERE id = "
query2 += user_input  # Unsafe
print(f"Constructed query2 (unsafe): {query2}")


query3 = "SELECT * FROM users WHERE id = %s" % user_input
print(f"Constructed query3 (unsafe): {query3}")


query4 = f"SELECT * FROM users WHERE username = {user_input}"
print(f"Constructed query4 (unsafe): {query4}")


def detect_sql_injection(query):
    if "+" in query or "concat" in query or "%" in query or "f-string" in query:
        print("Potential SQL Injection vulnerability detected.")
    else:
        print("Query is safe from SQL injection.")


detect_sql_injection(query)
detect_sql_injection(query2)
detect_sql_injection(query3)
detect_sql_injection(query4)


print("\nAnalysis complete. Please use parameterized queries to prevent SQL injection.")