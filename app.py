from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dataTest
user = db.user
read = user.find()

# Insert funcional
post = {
    'name': 'Random Guy',
    'age': 65,
    'email': "v-v@email.com" 
}
user_id = user.insert_one(post).inserted_id 

print("Id do usuario ",user_id)

# Update funcional

myQuery = {"name": "Someone-else"}
newValue = {"$set": {"name": "Nadiya Ismail"}}
user.update_one(myQuery, newValue)

# Delete funcional
try:
    user.delete_one({"name": "Random Guy"})
except:
    print("Erro")


# Read funcional

for doc in read:
    print(doc)

# Tela de opções do usuario (CRUD)
# Banco na nuvem (CLUSTER)
# UPAR para repl.it
