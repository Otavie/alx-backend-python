import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("ALTER TABLE users ADD COLUMN email TEXT")

conn.commit()
conn.close()

print("Email field added to users table successfully.")