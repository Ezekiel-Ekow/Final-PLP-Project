import sqlite3

# Connect to the database
conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

# Fetch the schema of the medications table
cursor.execute("PRAGMA table_info(medications);")
schema = cursor.fetchall()

# Display the schema
print("Medications Table Schema:")
for column in schema:
    print(column)

conn.close()
