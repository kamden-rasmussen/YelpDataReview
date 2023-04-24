# class for reviews queries

class Reviews:

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor

    def getAllReviews(self):
        return self.cursor.execute('SELECT * FROM reviews').fetchall()

    # Which state has the most reviews?
    def mostReviewsQuery(self):
        query = '''
        SELECT state, COUNT(*) AS count
        FROM businesses
        JOIN reviews ON businesses.business_id = reviews.business_id
        GROUP BY state
        ORDER BY count DESC
        LIMIT 1
        '''
        return self.cursor.execute(query).fetchone()

    def listTop10statesReviewed(self):
        query = '''
        SELECT state, COUNT(*) AS count
        FROM businesses
        JOIN reviews ON businesses.business_id = reviews.business_id
        GROUP BY state
        ORDER BY count DESC
        LIMIT 10
        '''
        return self.cursor.execute(query).fetchall()

    def printReviewData(self, data):
        print('Review ID:', data[0])
        print('Business ID:', data[1])
        print('Stars:', data[2])
        print('Text:', data[3])
        print('')