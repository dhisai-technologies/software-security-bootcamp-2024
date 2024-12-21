import sqlite3

conn = sqlite3.connect(":memory:") 
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.executemany("""
INSERT INTO users (username, password)
VALUES (?, ?)
""", [("admin", "admin123"), ("user1", "password1"), ("user2", "password2")])

conn.commit()

def vulnerable_login(input_username, input_password):
    query = f"SELECT * FROM users WHERE username = '{input_username}' AND password = '{input_password}'"
    print(f"Executing query: {query}")
    try:
        return cursor.execute(query).fetchall()
    except Exception as e:
        print(f"Error during execution: {e}")
        return []

def test_payloads(file_path):
    print("\nStarting SQL Injection tests...\n")
    with open(file_path, "r") as payloads_file:
        payloads = [line.strip() for line in payloads_file.readlines() if line.strip()]

    for payload in payloads:
        print(f"Testing payload: {payload}")
        results = vulnerable_login(payload, "any_password")
        if results:
            print(f"Payload succeeded! Retrieved rows: {results}\n")
        else:
            print("Payload failed.\n")

def main():
    file_path = "payloads.txt"

    try:
        test_payloads(file_path)
    except FileNotFoundError:
        print("Error: File not found. Please upload a valid file.")

if __name__ == "__main__":
    main()

conn.close()
