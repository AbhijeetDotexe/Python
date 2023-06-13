import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO employees VALUES (1, 'John Doe', 30)")
cursor.execute("INSERT INTO employees VALUES (2, 'Jane Smith', 25)")
cursor.execute("INSERT INTO employees VALUES (3, 'Bob Johnson', 35)")
conn.commit()

# Select and display all rows from the table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update a record
cursor.execute("UPDATE employees SET age = 40 WHERE id = 1")
conn.commit()

# Delete a record
cursor.execute("DELETE FROM employees WHERE id = 2")
conn.commit()

# Select and display all rows from the table after modifications
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
conn.close()
