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

    def getReviewsForTopRatedRestaurantByType(self, type, state):
        query = ''' 
        select stars, text
        from reviews
        where 
        business_id = (
            select business_id
            from businesses
            where state = ? 
            and categories like ? 
            and stars = (
                select max(stars)
                from businesses
                where state = ? and categories like ?
            )
        )
        order by stars DESC
        limit 5
        '''
        return self.cursor.execute(query, (state, '%' + type + '%', state, '%' + type + '%')).fetchall()

    def get5RandomReviewsForRestaurantByName(self, name):
        query = '''
        select stars, text
        from reviews
        where business_id = (
            select business_id
            from businesses
            where name = ?
        )
        order by RANDOM()
        limit 5
        '''
        return self.cursor.execute(query, (name,)).fetchall()

    def printReviewData(self, data):
        print('Stars:', data[0])
        print('Text:', data[1])
        print('')