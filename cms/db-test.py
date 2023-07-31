import sqlite3
import os

# Connect to the database
conn = sqlite3.connect("/Users/jackson.mckissack/Desktop/KCC-CMS/cms/reflex.db")

# Create a cursor
c = conn.cursor()

# Insert a row
result = c.execute("SELECT * FROM User")
#result = c.execute('''
#UPDATE User
#SET tenant = 'KCC'
#WHERE username = 'jackson'
#''')
print(list(result))

# Commit the changes
conn.commit()

# Close the connection
conn.close()