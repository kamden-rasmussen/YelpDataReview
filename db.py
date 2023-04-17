import sqlite3
import setup

class DBClass:
    def __init__(self):
        print('db init')
        self.db = sqlite3.connect('yelp.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('SELECT SQLITE_VERSION()')
        data = self.cursor.fetchone()
        print("SQLite version: %s" % data)
        self.cursor.execute('CREATE TABLE IF NOT EXISTS businesses (business_id varchar PRIMARY KEY, name varchar, city varchar, state varchar, stars float64, review_count INTEGER, categories varchar)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS reviews (review_id varchar PRIMARY KEY, business_id varchar, stars float64, text varchar)')

    def firstTimeSetup(self):
        print('first time setup')
        setup.PUTBusinessesInDB(self)
        print('businesses put in db')

