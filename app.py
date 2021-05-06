from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dataTest
user = db.user
res = user.find()

""" post = {
    'name': 'Random Guy',
    'age': 65,
    'email': "v-v@email.com" 
}
user_id = user.insert_one(post).inserted_id 

print("Id do usuario ",user_id) """
for doc in res:
    print(doc)

# Insert funcional
# Read funcional
# Update funcional
# Delete funcional
# Tela de opções do usuario (CRUD)
