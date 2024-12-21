import sqlite3

conn = sqlite3.connect('login1.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

users_data = [
    ('admin', 'admin123'),
    ('user1', 'user1123'),
    ('user2', 'user2123'),
    ('user3', 'user3123'),
    ('user4', 'user4123'),
]

cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users_data)
conn.commit()

def vulnerable_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Login successful!"
    else:
        return "Login failed!"

def check_user_exists(username):
    user_exists = False
    for user in users_data:
        if user[0] == username:
            user_exists = True
            break
    return user_exists

print("Enter the username and password for login test:")
input_username = input("Username: ")
input_password = input("Password: ")

print("\nChecking if the username exists in users_data:")
if check_user_exists(input_username):
    print("User exists in users_data.")
else:
    print("User does not exist in users_data.")

print("\nVulnerable Login (with potential SQL injection):")
print(vulnerable_login(input_username, input_password))

injection_username = "admin' OR '1'='1"
injection_password = ""

print("\nTesting SQL Injection (bypassing login):")
print(vulnerable_login(injection_username, injection_password))

conn.close()