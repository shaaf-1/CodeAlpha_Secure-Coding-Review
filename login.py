import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")

cursor.execute("INSERT INTO users VALUES ('admin','admin123')")
conn.commit()

print("===== LOGIN SYSTEM =====")

username = input("Username: ")
password = input("Password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

print(query)

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Username or Password")

conn.close()