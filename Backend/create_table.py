import sqlite3

conn = sqlite3.connect('database.db')
print("connected to database successfully")

conn.execute('CREATE TABLE trails (name TEXT, length REAL, elevation REAL, difficulty level INTEGER, Lookouts TEXT)')