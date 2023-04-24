import json

# {"business_id":"Pns2l4eNsfO8kk83dixA6A","name":"Abby Rappoport, LAC, CMQ","address":"1616 Chapala St, Ste 2","city":"Santa Barbara","state":"CA","postal_code":"93101","latitude":34.4266787,"longitude":-119.7111968,"stars":5.0,"review_count":7,"is_open":0,"attributes":{"ByAppointmentOnly":"True"},"categories":"Doctors, Traditional Chinese Medicine, Naturopathic\/Holistic, Acupuncture, Health & Medical, Nutritionists","hours":null}
def PUTBusinessesInDB(db):
    print('putting businesses in db')
    with open('yelp_dataset/yelp_academic_dataset_business.json') as f:
        for line in f:
            business = json.loads(line)
            db.cursor.execute('INSERT INTO businesses VALUES (?,?,?,?,?,?,?)', (business['business_id'], business['name'], business['city'], business['state'], business['stars'], business['review_count'], business['categories']))
            db.db.commit()


# {"review_id":"KU_O5udG6zpxOg-VcAEodg","user_id":"mh_-eMZ6K5RLWhZyISBhwA","business_id":"XQfwVwDr-v0ZS3_CbbE5Xw","stars":3.0,"useful":0,"funny":0,"cool":0,"text":"If you decide to eat here, just be aware it is going to take about 2 hours from beginning to end. We have tried it multiple times, because I want to like it! I have been to it's other locations in NJ and never had a bad experience. \n\nThe food is good, but it takes a very long time to come out. The waitstaff is very young, but usually pleasant. We have just had too many experiences where we spent way too long waiting. We usually opt for another diner or restaurant on the weekends, in order to be done quicker.","date":"2018-07-07 22:09:11"}
def PUTReviewsInDB(db):
    print('putting reviews in db')
    with open('yelp_dataset/yelp_academic_dataset_review.json') as f:
        for line in f:
            review = json.loads(line)
            db.cursor.execute('INSERT INTO reviews VALUES (?,?,?,?)', (review['review_id'], review['business_id'], review['stars'], review['text']))
            db.db.commit()