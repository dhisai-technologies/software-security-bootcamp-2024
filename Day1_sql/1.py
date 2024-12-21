import sqlite3

# Create a database and table
def create_database():
    connection = sqlite3.connect("secure_app.db")
    cursor = connection.cursor()

    # Create a users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Insert example data
    cursor.executemany("""
        INSERT INTO users (username, password) VALUES (?, ?)
    """, [
        ("jaga", "password123"),
        ("romika", "password123"),
      
    ])

    connection.commit()
    connection.close()

# Fetch data in an unsafe way (vulnerable to SQL injection)
def fetch_user_data(username):
    connection = sqlite3.connect("secure_app.db")
    cursor = connection.cursor()

    # SQL injection vulnerability here: concatenating user input directly into the query
    query = f"SELECT username, password FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user_data = cursor.fetchall()

    connection.close()
    return user_data

if __name__ == "__main__":
    
    create_database()

    # Example usage with an SQL injection payload
    username_to_search = "alice' OR '1'='1"  # SQL Injection
    user_data = fetch_user_data(username_to_search)

    if user_data:
        print(f"User found: {user_data}")
    else:
        print("User not found.")