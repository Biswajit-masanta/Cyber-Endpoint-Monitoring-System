import sqlite3

connection = sqlite3.connect('monitoring.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    hostname TEXT PRIMARY KEY,
    os TEXT,
    version TEXT,
    cpu REAL,
    memory REAL,
    disk REAL,
    timestamp TEXT
)
''')

connection.commit()
connection.close()

print("Database initialized successfully!")
