import sqlite3

# Setup a sample database for demonstration
conn = sqlite3.connect(":memory:")  # In-memory database for testing
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Insert some dummy data
cursor.executemany("""
INSERT INTO users (username, password)
VALUES (?, ?)
""", [("admin", "admin123"), ("user1", "password1"), ("user2", "password2")])

conn.commit()

# Vulnerable query function
def vulnerable_login(input_username, input_password):
    query = f"SELECT * FROM users WHERE username = '{input_username}' AND password = '{input_password}'"
    print(f"Executing query: {query}")
    try:
        return cursor.execute(query).fetchall()
    except Exception as e:
        print(f"Error during execution: {e}")
        return []

# Test for SQL injection using uploaded payloads
def test_payloads(file_path):
    print("\nStarting SQL Injection tests...\n")
    with open(file_path, "r") as payloads_file:
        payloads = [line.strip() for line in payloads_file.readlines() if line.strip()]

    for payload in payloads:
        print(f"Testing payload: {payload}")
        results = vulnerable_login(payload, "any_password")  # Testing username injection
        if results:
            print(f"Payload succeeded! Retrieved rows: {results}\n")
        else:
            print("Payload failed.\n")

# Main program
def main():
    print("Please upload your payloads file.")
    file_path = input("Enter the path to the uploaded payloads file: ").strip()

    try:
        test_payloads(file_path)
    except FileNotFoundError:
        print("Error: File not found. Please upload a valid file.")

if __name__ == "__main__":
    main()

conn.close()
