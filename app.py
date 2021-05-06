from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dataTest
user = db.user

post = {
    'name': 'Ben Otto',
    'age': 12,
    'email': "toot@email.com" 
}
user_id = user.insert_one(post).inserted_id

print("Id do usuario ",user_id)

