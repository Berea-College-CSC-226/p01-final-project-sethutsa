import sqlite3

class Trail:
    def __init__(self, name, length, elevation, difficulty):
        """

        :param name:
        :param length:
        :param elevation:
        :param difficulty:
        """

        self.name = name
        self.length = length
        self.elevation = elevation
        self.difficulty = difficulty

    @classmethod
    def get_database_connection(cls):
        """

        :return:
        """
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def get_all_trails(cls):
        """

        :return:
        """
        conn = cls.get_database_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM trails ORDER BY name')
        trails = []

        for row in cursor.fetchall():
            trail = cls(
                name=row['name'],
                length=row['length'],
                elevation=row['elevation'],
                difficulty=row['difficulty']
                )
            trails.append(trail)

        conn.close()
        return trails

    @classmethod
    def get_trail_by_name(cls, name):
        """

        :param name:
        :return:
        """
        conn = cls.get_database_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM trails WHERE name = ?', (name,))
        row = cursor.fetchone()

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
