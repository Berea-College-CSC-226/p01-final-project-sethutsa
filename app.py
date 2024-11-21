from flask import Flask
from peewee import SqliteDatabase, Model, CharField, ForeignKeyField

db = SqliteDatabase('database.db')

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!!!!"


