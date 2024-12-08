import sqlite3
from optparse import Values
from tkinter.constants import INSERT
from unittest.mock import DEFAULT

conn = sqlite3.connect('database.db')
print("connected to database successfully")
#
# # Create the 'trails' table
# conn.execute('CREATE TABLE trails (name TEXT, length REAL, elevation REAL)')
# print("Table created successfully")

# the data as a list of tuples
data = [
    ('Bluegrass Overlook', 0.9, 629),
    ('East Pinnacle', 1.7, 587),
    ('West Pinnacle', 1.5, 511),
    ('Eagle’s Nest', 1.6, 632),
    ('Buzzard’s Roost', 1.8, 550)
]

# Inserts the data into the 'trails' table
conn.executemany('INSERT INTO trails (name, length, elevation) VALUES (?, ?, ?)', data)
print("Data inserted successfully")

conn.commit()

conn.close()
print("Connection closed")
