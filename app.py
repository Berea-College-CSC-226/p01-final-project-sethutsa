from flask import Flask, render_template, url_for
from classes import Trail
import os
# from peewee import SqliteDatabase, Model, CharField, ForeignKeyField
#
# db = SqliteDatabase('database.db')

app = Flask(__name__)

@app.route("/")
def home():
    trail = Trail.get_all_trails()
    return render_template('home.html', trail=trail)

@app.route('/<trail_name>')
def trail_page(trail_name):
    print(f"Trail name received: {trail_name}")
    trail = Trail.get_trail_by_name(trail_name)
    if not trail:
        print("Trail not found in database")
        return "Trail not found", 404
    print(f"Trail details: {trail.__dict__}")
    return render_template('trail.html', trail=trail)

if __name__=='__main__':
    app.run(debug=True)