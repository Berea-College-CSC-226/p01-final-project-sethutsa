######################################################################
# Author: Utsa Seth
# Username: sethutsa
#
# Assignment: p01-final-project
#
# Purpose: Create a trail class and its methods to pull information from the database
#
######################################################################
# Acknowledgements:
# Check references in README.md
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sqlite3

class Trail:
    def __init__(self, name, length, elevation, difficulty):
        """
        Defines the attributes of the trail class.
        :param name: Name of the trail
        :param length: Length of the trail in miles
        :param elevation: Elevation of the trail in feet
        :param difficulty: My difficulty rating for the trail
        """
        self.name = name
        self.length = length
        self.elevation = elevation
        self.difficulty = difficulty  #all the trail attributes

    @classmethod
    def get_database_connection(cls):
        """
        Creates a connection with the database and allows retrieval of information.
        :return:
        """
        conn = sqlite3.connect('database.db') #connects to the database
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def get_all_trails(cls):
        """
        Has a class decorator that allows the class to be used directly without an instance. Makes a query to the
        database to retrieve information and stores the information about all the trails in a list.
        the attributes and
        :return:
        """
        conn = cls.get_database_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM trails ORDER BY name')  #sqlite3 query
        trails = []
        for row in cursor.fetchall(): #loops through each row of the database and makes a
            trail = cls(              #list of objects saved in a list called trails
                name=row['name'],
                length=row['length'],
                elevation=row['elevation'],
                difficulty=row['difficulty']
                )
            trails.append(trail)
        conn.close() #closes connection to database
        return trails

    @classmethod
    def get_trail_by_name(cls, name):
        """
        Uses a query to get all the attributes for one trail object based on the name of the trail
        :param name:Name of the trail
        :return:
        """
        conn = cls.get_database_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM trails WHERE name = ?', (name,))
        row = cursor.fetchone()  #fetches one row of data from the db based on what name is passed in
        if not row:
            conn.close()
            return None
        trail = cls(
            name=row['name'],
            length=row['length'],
            elevation=row['elevation'],
            difficulty=row['difficulty']
        )
        conn.close()
        return trail
