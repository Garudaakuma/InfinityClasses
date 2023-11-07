
''' [PY-A01]
 Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma
 senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um 
 email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se 
 o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente.
 E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados
 ele continue em um loop.

Feito por: Lucas Aioria Serpa
turma: 713
'''

#Import
from os import system as sy

email = input("Olá!\nSeja bem vindo ao programa!\nPor favor, digite seu email!\n->")
sy('cls')
senha = input("Agora, digite sua senha!\n-> ")
user_data = [email,senha]
lop = 0
while True:
    if lop == 0:
        sy('cls')
        email_check = input("Agora, para entrar no programa\nPor favor digite email cadastrados no sistema!\n-> ")
        # Primeira confirmação [email]
        if email_check != user_data[0]:
            lop = 1
            sy('cls')
            print("Oops!\nEste email não foi encontrado no sistema!\nTente novamente!")
            continue
        sy('cls')
        senha_check = input("Perfeito!\nAgora digite sua senha!\n-> ")
        # Segunda confirmação [senha]
        if senha_check != user_data[1]:
            lop = 1
            sy('cls')
            print("Oops!\nEste email não contem está senha!\nTente novamente!")
            continue
    else:
        sy('cls')
        email_check = input("Digite seu email cadastrado no sistema!\n-> ")
        # Primeira confirmação [email]
        if email_check != user_data[0]:
            lop = 1
            sy('cls')
            print("Oops!\nEste email não foi encontrado no sistema!\nTente novamente!")
            continue
        sy('cls')
        senha_check = input("Digite sua senha cadastrado no sistema deste email!\n-> ")
        # Segunda confirmação [senha]
        if senha_check != user_data[1]:
            lop = 1
            sy('cls')
            print("Oops!\nEste email não contem está senha!\nTente novamente!")
            continue
    sy('cls')
    print(f'''
Parabéns você se conectou à sua conta bem vindo ao programa!
    email:      [{email}]
    senha:      [{senha}]
        ''')
    break