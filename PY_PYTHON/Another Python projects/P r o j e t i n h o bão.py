#import
import os

#Projeto: 
'''
1 - Se o usuário errar a senha 3 vezes, block
2 - verificação de senha: minimo 8 caracteres
3 - verificação de senha: tem que conter números e letras
4 - precisa conter uma caractere especial
5 - precisa esconder a senha no print (****)
'''

#Variaveis
username,password,userID = "","",{}
cont,contPass,contUser,lop,trys = 0,0,0,0,3

# Username rules
def format_username(name: str) -> bool:
    '''Verifica as regras do nome do usuario!'''
    #Error checker
    error,varword,varnumber,varsignal = False,0,0,0
    if len(name) < 2:
        print("[ERRO: 001]\nPrecisa ser maior ou igual a duas caracteres")
        error = True
    for i in name.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            varword+=1  
        if i in '0123456789':
            varnumber+=1
        if i in '!@#$%¨&*()-_+=§´`[]}{ª~^º,.;:/?°\|':
            varsignal+=1
    if varword == 0:
        print("[ERRO: 002]\nPrecisa conter um caractere")
        error = True
    if varnumber != 0:
        print("[ERRO: 003]\nNão pode conter números")
        error = True
    if varsignal != 0:
        print("[ERRO: 004]\nNão pode conter sinais")
        error = True
    return error
# Password rules
def format_password(word: str) -> bool:
    '''Verifica as regras da senha do usuario!'''
    #Error Checker
    error,varword,varnumber,varsignal,varspace = False,0,0,0,0
    if len(word) < 8:
        print("[ERRO: 005]\nPrecisa ser maior ou igual à 8 caracteres")
        error = True
    for i in word.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            varword+=1  
        if i in '0123456789':
            varnumber+=1
        if i in '!@#$%¨&*()-_+=§´`[]}{ª~^º,.;:/?°\|':
            varsignal+=1
        if i in ' ':
            varspace+=1
    if varword == 0:
        print("[ERRO: 006]\nPrecisa conter caracteres")
        error = True
    elif varnumber == 0:
        print("[ERRO: 007]\nPrecisa conter números")
        error = True
    elif varsignal == 0:
        print("[ERRO: 008]\nPrecisa conter um sinal")
        error = True
    elif varspace != 0:
        print("[ERRO: 009]\nNão pode conter espaço/s")
        error = True
    return error

while True:
    # Nome loop!
    if lop == 1:
        username = input("Digite seu username novamente!\n: ")
        os.system('cls')
    elif lop == 0:
        username = input("Digite seu username!\n: ")
        os.system('cls')
    if format_username(username) is True:
        lop = 1
        continue
    # Senha loop!
    if lop == 2:    # Errou 1 ou mais vezes
        password = input("Digite sua senha novamente!\n: ")
        os.system('cls')
        hide = "*"*len(password)
        print(f"Digite sua senha novamente!\n: {hide}")
    elif lop == 0:           # Sem erros!
        password = input("Digite sua senha!\n:")
        os.system('cls')
        hide = "*"*len(password)
        print(f"Digite sua senha!\n: {hide}")
    if format_password(password) is True:
        lop = 2
        continue
    # User content pick
    if format_username(username) is False and format_password(password) is False:
        userID[username] = password
        os.system('cls')
        print(userID)
        break
    else:
        os.system('cls')
        print("[ERRO: 010]\nAlgo deu errado!")

print("Agora logue na sua conta!\n")
while True:
    lop = 0
    # USERNAME
    if lop == 1:
        nameTry = input("Digite seu Username novamente!\n: ")
        os.system('cls')
    elif lop == 0:
        nameTry = input("Digite seu Username!\n: ")
        os.system('cls')
    for i in userID:
        if i == nameTry:
            print("Username True")
            contUser = 0
            break
        else:
            contUser+=1
    if contUser != 0:
        lop = 1
        continue
    # PASSWORD
    if lop == 2:
        wordTry = input("Digite sua senha novamente!\n: ")
        os.system('cls')
    elif lop == 0:
        wordTry = input("Digite sua senha!\n: ")
        os.system('cls')
    for i in userID:
        if nameTry[i] == wordTry:
            print("Password True")
            contPass = 0
            break
        else:
            contPass+=1
    if contPass != 0:
        cont+=1
        lop = 2
        continue
    if cont < 3:
        os.system('cls')
        print("Você Tentou se conectar com sua senha mais de 3 vezes!\nApp blocked!\n")
        break
        