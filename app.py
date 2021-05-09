from pymongo import MongoClient
import os

client = MongoClient('localhost', 27017)
db = client.dataTest
user = db.user

def layout(name):
     print('============================================='),
     print(f'                 {name}                 '),
     print('=============================================')


# loop de interação
while True:
    # Tela inicial de opções do usuario (CRUD)
    os.system('clear')
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
            name = input('Digite seu nome: ').lower()
            age = int(input("Digite sua idade: "))
            email = input('Digite seu email: ').lower()
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
                    os.system('clear')
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
        print(layout('LISTA'))
        # Read funcional
        try:
            for doc in user.find():
                print('Nome:',doc['name'], 'Idade:',doc['age'], ' Email:', doc['email'] )
        except:
            print('Erro ao listar dados.')
        else:
            print('=============================================')
            answer2 = input("[1]-Editar [2]-Apagar [3]-Sair ")
            if answer2 == '1':
                os.system('clear')
                print(layout('PESQUISAR'))
                # Pesquisa
                pesquisa = input("Pesquise o nome do usuario que queira editar: ")
                try:
                    query = user.find_one({"name": f"{pesquisa}"})
                    os.system('clear')
                    print(layout('PESQUISAR RESULTADO:'))
                    print('Resultado: ')
                    print("Nome:", query['name'], "Idade:", query['age'], "Email:", query['email'])
                    print('=============================================')
                except:
                    print('Erro no banco de dados')
                    break
                else:
                    option_edit = input("Este era o dado que estava procurando ? [Y/n]: ").lower()
                    if option_edit == 'y':
                        os.system('clear')
                        print(layout('PESQUISAR RESULTADO:'))
                        print(' [1]-Atualizar dados\n [2]-Cancelar operação')
                        print('=============================================')
                        option_edit2 = input(': ')
                        if option_edit2 == '1':
                            name = input('Digite novo nome: ').lower()
                            age = int(input("Digite nova idade: "))
                            email = input('Digite novo email: ').lower()
                            # Update funcional
                            myQuery = {"name": f"{pesquisa}"}
                            newValue = {"$set": {"name": f"{name}", "age": f"{age}", "email": f"{email}"}}
                            user.update_one(myQuery, newValue)
                            print(query)
                        elif option_edit2 == '2':
                            os.system('clear')

                    elif option_edit == 'n':
                        os.system('clear')
                        print('Tente novamente')
                    else:
                        print('Não funfa')

            if answer2 == '2':
                os.system('clear')
                print(layout('PESQUISAR'))
                # Pesquisa
                pesquisa = input("Pesquise o nome do usuario que queira deletar: ")
                try:
                    query = user.find_one({"name": f"{pesquisa}"})
                    os.system('clear')
                    print(layout('PESQUISAR RESULTADO:'))
                    print('Resultado: ')
                    print("Nome:", query['name'], "Idade:", query['age'], "Email:", query['email'])
                    print('=============================================')
                except:
                    print('Erro no banco de dados')
                    break
                else:
                    option_delete = input("Deseja deletar este dado? suas ações não poderão ser desfeitas [Y/n]: ").lower()
                    if option_delete == 'y':
                        # Delete funcional
                        try:
                            user.delete_one({"name": f"{pesquisa}"})
                        except:
                            print("Erro")
                    elif option_delete == 'n':
                        os.system('clear')
            if answer2 == '3':
                os.system('clear')
    elif option == '3':
        os.system('clear')
        print('Até mais!!')
        break
    else:
        print("Entrada não correspondente, Tente novamente.")
 
# Banco na nuvem (CLUSTER)
# UPAR para repl.it
