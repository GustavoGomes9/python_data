from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = client.dataTest
user = db.user
read = user.find()

def layout(name):
     print('============================================='),
     print(f'                 {name}                 '),
     print('=============================================')
    


"""
# Update funcional
myQuery = {"name": "Someone-else"}
newValue = {"$set": {"name": "Nadiya Ismail"}}
user.update_one(myQuery, newValue)

# Delete funcional
try:
    user.delete_one({"name": "Random Guy"})
except:
    print("Erro")
"""
# loop de interação
while True:
    # Tela inicial de opções do usuario (CRUD)
    print(layout('PYHTON_DATA'))
    print('Escolha uma opção abaixo: ')
    print(' [1]-Cadastrar\n [2]-Listar\n [3]-Sair do sistema' )
    print('=============================================')
    option = input('Digite aqui: ')

    # Rotas para opções
    # Tela cadastro
    if option == '1':
        os.system('clear')
        sure = False
        while not sure:
            print(layout('CADASTRO'))
            name = input('Digite seu nome: ')
            age = int(input("Digite sua idade: "))
            email = input('Digite seu email: ')
            os.system('clear')
            answer = input(f"Seus dados são: \n\n nome: {name}\n idade: {age}\n email: {email}\n\nOs dados estão corretos? [Y/n]: ").lower()
            if answer == 'y':
                insert = {
                    "name": name,
                    "age": age,
                    "email": email
                }
                try:
                    insert_id = user.insert_one(insert).inserted_id
                except:
                    print("Ocorreu algum erro")
                else:
                    print("Cadastro realizado com sucesso!")
                    sure = True
            elif answer == 'n':
                os.system('clear')
                print("Tente novamente!")
            else:
                os.system('clear')
                print("Valor inserido não correspondente.")
                sure = True

    elif option == '2':
        os.system('clear')
        # Tela mostrar
        print(layout('LISTANDO'))
        # Read funcional
        for doc in read:
            print('Nome:',doc['name'], 'Idade:',doc['age'], ' Email:', doc['email'] )
        print('=============================================')
        answer = input("[1]-Editar [2]-Apagar [3]-Sair ").lower()
        if answer == '3':
            os.system('clear')

        # Pesquisar
        # opção atualizar
        # opção deletar
    elif option == '3':
        os.system('clear')
        print('Até mais!!')
        break
    else:
        print("Entrada não correspondente, Tente novamente.")
 
# Banco na nuvem (CLUSTER)
# UPAR para repl.it
