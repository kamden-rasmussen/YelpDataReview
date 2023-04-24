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
    def newYorkPizzaQuery(self):
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'NY' 
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

    # How much do Utahns like Soda? -- need more digging
    def utahSodaQuery(self):
        query = '''
        SELECT AVG(stars)
        FROM businesses
        WHERE state = 'UT' 
        AND categories LIKE '%Soda%'
        '''
        return self.cursor.execute(query).fetchone()[0]


# {"business_id":"Pns2l4eNsfO8kk83dixA6A","name":"Abby Rappoport, LAC, CMQ","address":"1616 Chapala St, Ste 2","city":"Santa Barbara","state":"CA","postal_code":"93101","latitude":34.4266787,"longitude":-119.7111968,"stars":5.0,"review_count":7,"is_open":0,"attributes":{"ByAppointmentOnly":"True"},"categories":"Doctors, Traditional Chinese Medicine, Naturopathic\/Holistic, Acupuncture, Health & Medical, Nutritionists","hours":null}
    def printBusinessInfo(self, data):
        print('Business ID:', data[0])
        print('Business Name:', data[1])
        print('City:', data[2])
        print('State:', data[3])
        print('Stars:', data[4])
        print('Review Count:', data[5])
        print('Categories:', data[6])
        print('')
