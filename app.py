######################################################################
# Author: Utsa Seth
# Username: sethutsa
#
# Assignment: p01-final-project
#
# Purpose: Create flask routes for the pinnacles navigator
#
######################################################################
# Acknowledgements:
# Check references in README.md
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from flask import Flask, render_template, url_for
from classes import Trail

app = Flask(__name__)  #creates a flask app

@app.route("/")
def home():
    trail = Trail.get_all_trails() #calls the get_all_trails method which returns a list of trails and their attributes
    return render_template('home.html', trail=trail) #uses home.html to render the home page and
                                                                       #passes in the object trail
@app.route('/<trail_name>')
def trail_page(trail_name):
    trail = Trail.get_trail_by_name(trail_name)  ##calls the get_trail_by_name method which returns one trail
    if not trail:
        print("Trail not found in database") #prints error if the trail is not in the database
        return "Trail not found", 404

    return render_template('trail.html', trail=trail) #renders the trail page using trail

if __name__=='__main__':
    app.run(debug=True)