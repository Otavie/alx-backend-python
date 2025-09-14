import sqlite3

conn = sqlite3.connect('users.db')  # creates users.db in the current directory
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute("INSERT INTO users (name) VALUES ('Otavie')")
cursor.execute("INSERT INTO users (name) VALUES ('Charles')")
cursor.execute("INSERT INTO users (name) VALUES ('Adewale')")
cursor.execute("INSERT INTO users (name) VALUES ('Hassan')")
cursor.execute("INSERT INTO users (name) VALUES ('Chinedu')")

conn.commit()
conn.close()

print("Database and users tables created successfully.")