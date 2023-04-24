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
        self.cursor.execute('CREATE TABLE IF NOT EXISTS businesses (business_id text PRIMARY KEY, name text, city text, state text, stars float64, review_count INTEGER, categories text)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS reviews (review_id text PRIMARY KEY, business_id text, stars float64, text text)')

    def firstTimeSetup(self):
        if self.cursor.execute('SELECT * FROM businesses').fetchone() is None:
            print('first time setup businesses')
            setup.PUTBusinessesInDB(self)
        if self.cursor.execute('SELECT * FROM reviews').fetchone() is None:
            print('first time setup reviews')
            setup.PUTReviewsInDB(self)


