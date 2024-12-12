import sqlite3

conn = sqlite3.connect('database.db')
print("connected to database successfully")
#
# # Create the 'trails' table
# conn.execute('CREATE TABLE trails (name TEXT, length REAL, elevation REAL)')
# print("Table created successfully")

# the data as a list of tuples
# data = [
#     ('Bluegrass Overlook', 0.9, 629),
#     ('East Pinnacle', 1.7, 587),
#     ('West Pinnacle', 1.5, 511),
#     ('Eagle’s Nest', 1.6, 632),
#     ('Buzzard’s Roost', 1.8, 550)
# ]
#
# # Inserts the data into the 'trails' table
# conn.executemany('INSERT INTO trails (name, length, elevation) VALUES (?, ?, ?)', data)
# print("Data inserted successfully")
#
# cursor = conn.cursor()
# cursor.execute("ALTER TABLE trails ADD COLUMN difficulty FLOAT;")
# print("columns added successfully")
#
# new_data = [
#     ('Bluegrass Overlook', 1),
#     ('East Pinnacle', 1.5),
#     ('West Pinnacle',2.5),
#     ('Eagle’s Nest', 2),
#     ('Buzzard’s Roost', 2)
# ]
#
# cursor.executemany('''
#             UPDATE trails
#             SET difficulty = ?
#             WHERE name = ?;
#             ''', [(row[1], row[0]) for row in new_data])
#
# cursor.execute("UPDATE trails SET name = ? WHERE rowid = ?", ("Eagle's Nest", 4))
# cursor.execute("UPDATE trails SET name = ? WHERE rowid = ?", ("Buzzard's Roost", 5))

# cursor = conn.cursor()
#
# basin_mountain = ('Basin Mountain', 2.8, 1437, 3)
#
# cursor.execute("""
#         INSERT INTO trails (name, length, elevation, difficulty)
#         VALUES (?, ?, ?, ?);
#     """, basin_mountain)
# print("New row added successfully.")

conn.commit()

conn.close()
print("Connection closed")
