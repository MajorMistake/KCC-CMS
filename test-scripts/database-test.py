import sqlite3

# Connect to the database
conn = sqlite3.connect("reflex.db")

# Create a cursor
c = conn.cursor()

# Insert a row
result = c.execute("SELECT * FROM sqlite_master where type = 'table'")
print(list(result))

# Commit the changes
#conn.commit()

# Close the connection
conn.close()