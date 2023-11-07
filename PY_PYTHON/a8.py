#Import
from atividade_seletor import ativ_sel as a_s
from os import system as sy
import random

# Atividade seletor
n = a_s()

# Atividade 1
if n == 1:
    sus_point = 0
    conclusion_arry = ["Inocente",
                       "Suspeito(a)",
                       "Cúmplice",
                       "Assassino"]
    ask_input = ["Telefonou para a vítima?",
                 "Esteve no local do crime?",
                 "Mora perto da vítima?",
                 "Devia para a vítima?",
                 "Já trabalhou com a vítima?"]
    for i in range(len(ask_input)):
        sy('cls')
        while True:
            ask = input(f'{ask_input[i]}\n(sim) (não)\n-> ').lower()
            if ask == 's' or ask == 'sim':
                sus_point+=1
                sy('cls')
                break
            elif ask == 'n' or ask == 'não':
                sy('cls')
                break
            else:
                sy('cls')
                print("Erro!\nApenas aceita (sim) or (não)\n")
    sy('cls')
    if len(conclusion_arry) < sus_point:
        sus_point = len(conclusion_arry)-1
    print(f"Você é {conclusion_arry[sus_point]}!")
    
# Atividade 2
if n == 2:
    sy('cls')
    salario = float(input("Digite seu salario\n-> "))
    prestacao = float(input("Digite sua prestação de um emprestimo\n-> "))
    emprest = lambda sal=float,prs=float: 'Empréstimo não concedido!' if (20*sal)/100 < prs else 'Empréstimo concedido!'
    print(emprest(salario,prestacao))

# Atividade 3
if n == 3:
    sy('cls')
    peso_ideal = lambda s_=str,h_=float: float((72.7*h_)-58) if s_ == 'h' else float((62.1*h_)-44.7)
    h = float(input("Digite sua altura atual!\n-> "))
    s = input("Digite seu sexo\n(H) → Homen\n(M) → Mulheres\n-> ").lower()
    print(f"Seu peso ideal é: {peso_ideal(s,h)}")
    
# Atividade 4
if n == 4:
    sy('cls')
    tab_ask = int(input("Digite uma tabela da tabuada!\n-> "))
    sy('cls')
    print("Aqui está a tabuada pedida!\n")
    for numb in range(10):
        i = numb+1
        print(f'{i}x{tab_ask} = {tab_ask*i}')

# Atividade 5
if n == 5:
    sy('cls')
    number = input('digite um número!\n-> ')
    print(len(number))
    
# Atividade 6
if n == 6:
    sy('cls')
    final_num = int(input("Digite uma posição destá sequencia!\n-> "))
    var = 0
    var_2 = 1
    result = 0
    for postision in range(final_num):
        result = var+var_2
        var = var_2
        var_2 = result
        print(f"Posição nº{postision+1}: {result}")

# Atividade 7
if n == 7:
    sy('cls')
    list_num = []
    soma = 0
    mult = 1
    for i in range(5):
        list_num.append(random.randint(1,10))
        soma+=list_num[i]
        mult*=list_num[i]
    print(f"""
    lista:  {list_num}
    soma:   {soma}
    mult:   {mult}
          """)

# Atividade 8
if n == 8:
    sy('cls')
    pessoas = []
    for i in range(5):
        pessoas.append(random.randint(1,2))
    pessoas.reverse()
    print(pessoas)
    
# Atividade 9
if n == 9:
    sy('cls')
    vetor = []
    for i in range(5):
        vetor.append((random.randint(1,10))**2)
    print(sum(vetor),vetor)