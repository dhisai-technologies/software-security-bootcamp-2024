
sql_injection = [
    {"username": "admin", "password": "password123"},
    {"username": "user", "password": "userpass"},
]
def vulnerable_login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing Query: {query}")
    
    if "AND '1'='1'" in query:
        return True  

    for user in sql_injection:
        if username == user['username'] and password == user['password']:
            return True
    return False


username_payload = "admin' AND '1'='1"  
password_payload = "irrelevant"      


if vulnerable_login(username_payload, password_payload):
    print("Authentication Bypassed! Admin Access Granted.")
else:
    print("Authentication Failed.")
