# class for business queries

class Businesses:

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor

    def getAllBusinesses(self):
        return self.cursor.execute('SELECT * FROM businesses').fetchall()
    
    def getCountAllBusinesses(self):
        return self.cursor.execute('SELECT COUNT(*) FROM businesses').fetchone()[0]
    
    def getBusinessesByCity(self, city):
        return self.cursor.execute('SELECT * FROM businesses WHERE city = ?', (city,)).fetchall()

    def getCountBusinessesByCity(self, city):
        return self.cursor.execute('SELECT COUNT(*) FROM businesses WHERE city = ?', (city,)).fetchone()[0]

    def getBusinessesByState(self, state):
        return self.cursor.execute('SELECT * FROM businesses WHERE state = ?', (state,)).fetchall()
    
    def getCountBusinessesByState(self, state):
        return self.cursor.execute('SELECT COUNT(*) FROM businesses WHERE state = ?', (state,)).fetchone()[0]

    def getBusinessesByStateAndName(self, state, name):
        return self.cursor.execute('SELECT * FROM businesses WHERE state = ? AND name = ?', (state, name)).fetchall()

    # how much do New Yorkers like pizza?
    def newYorkPizzaQuery(self): # We dont have data for NY
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'NY' 
        AND categories LIKE '%Pizza%'
        '''
        return self.cursor.execute(query).fetchone()[0]

    # How much do Floridians like Pizza?
    def floridaPizzaQuery(self):
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'FL' 
        AND categories LIKE '%Pizza%'
        '''
        return self.cursor.execute(query).fetchone()[0]

    # how much do Californians like Mexican?
    def californiaMexicanQuery(self):
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'CA' 
        AND categories LIKE '%Mexican%'
        '''
        return self.cursor.execute(query).fetchone()[0]

    # how many pizza places are in California?
    def californiaPizzaQuery(self):
        query = '''
        SELECT COUNT(*)
        FROM businesses
        WHERE state = 'CA' 
        AND categories LIKE '%Pizza%'
        '''
        return self.cursor.execute(query).fetchone()[0]

    # How much do Utahns like Soda? -- need more digging
    def utahSodaQuery(self): # We dont have data for UT
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'UT' 
        AND categories LIKE '%Soda%'
        '''
        return self.cursor.execute(query).fetchone()[0]

    # How is the bar scene in LA?
    def PhiladelphiaBarQuery(self):
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'PA' 
        AND city = 'Philadelphia'
        AND categories LIKE '%Bars%'
        '''
        return self.cursor.execute(query).fetchone()[0]

    def getCountOfTypeOfRestaurantsByState(self, type, state):
        return self.cursor.execute('SELECT COUNT(*) FROM businesses WHERE state = ? AND categories LIKE ?', (state, '%' + type + '%')).fetchone()[0]

    # Give me the top rated restaurant in the state by type
    def getTopRatedRestaurantByType(self, type, state):
        query = '''
        SELECT *
        FROM businesses
        WHERE state = ?
        AND categories LIKE ?
        AND review_count > 100
        ORDER BY stars DESC
        LIMIT 1
        '''
        data = self.cursor.execute(query, (state, '%' + type + '%')).fetchone()
        if data is None:
            query = '''
            SELECT *
            FROM businesses
            WHERE state = ?
            AND categories LIKE ?
            ORDER BY stars DESC
            LIMIT 1
            '''
            data = self.cursor.execute(query, (state, '%' + type + '%')).fetchone()

        return data


# {"business_id":"Pns2l4eNsfO8kk83dixA6A","name":"Abby Rappoport, LAC, CMQ","address":"1616 Chapala St, Ste 2","city":"Santa Barbara","state":"CA","postal_code":"93101","latitude":34.4266787,"longitude":-119.7111968,"stars":5.0,"review_count":7,"is_open":0,"attributes":{"ByAppointmentOnly":"True"},"categories":"Doctors, Traditional Chinese Medicine, Naturopathic\/Holistic, Acupuncture, Health & Medical, Nutritionists","hours":null}
    def printBusinessInfo(self, data):
        print('Business Name:', data[1])
        print('City:', data[2])
        print('State:', data[3])
        print('Stars:', data[4])
        print('Review Count:', data[5])
        print('Categories:', data[6])
        print('')
