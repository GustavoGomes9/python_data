from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = client.dataTest
user = db.user
read = user.find()
"""
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
"""
# loop de interação
while True:
    # Tela inicial de opções do usuario (CRUD)
    print('=============================================')
    print('                 PYTHON_DATA                 ')
    print('=============================================')
    print('Escolha uma opção abaixo: ')
    print(' [1]-Cadastrar\n [2]-Listar\n [3]-Sair do sistema' )
    print('=============================================')
    option = input('Digite aqui: ')

    # Rotas para opções
    if option == '1':
        os.system('clear')
        print('Opção 1')
    elif option == '2':
        os.system('clear')
        print('Opção 2')
    elif option == '3':
        os.system('clear')
        print('Opção 3')
    else:
        print("Entrada não correspondente, escolha um número acima")


# Tela cadastro
# Tela mostrar
    # Pesquisar
    # opção atualizar
    # opção deletar 
# Banco na nuvem (CLUSTER)
# UPAR para repl.it
