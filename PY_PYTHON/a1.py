#Import


#seletor de atividades
n = int(input("Selecione uma atividade\n:"))
if n == 0:
    None

# Revisão de lógica:
'''
    -   Fluxo grama na programação
    -   Estruturas de controle
    -   Operadores de comparação
    -   Condições
    -   Operadores logicos (and or not)
    -   Fatorrial
'''

#Revisão lógica
''' #De forma manual
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
if n1 > n2 and n1 > n3:
    print("n1 é maior que todos!")
elif n2 > n1 and n2 > n3:
    print("n2 é maior que todos!")
else:
    print("n3 é maior que todos!")
'''
''' Com array+loop(for)
n1 = []
for i in range(0,3):
    n1.insert(i,int(input(f"Digite número {i+1}: ")))
n1.sort()
print(f"O número maior é {n1[2]}")
'''

#'eval()'
'''
n1 = 1
n2 = 2
op = "+"
re = f"{n1}{op}{n2}"
print(f"n1: {n1}\nn2: {n2}\nop: {op}\nre: {re}\neval: {eval(re)}")
'''

# Fatorial
'''
num = int(input("Fatorial: "))
re = 1
for i in range(1,num+1):
    re *= i
    print(re,i)
'''

#Atividade 1
if n == 1:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite um número: "))
    if n1 > n2:
        print(f"O maior número é {n1}")
    elif n1 == n2:
        print(f"Os números são iguais!")
    else:
        print(f"O maior número é {n2}")
#Atividade 2
if n == 2:
    n1 = float(input("Digite um número: "))
    if n1 > 0:
        print(f"O número {n1} é positivo")
    elif n1 == 0:
        print(f"O número {n1} é igual à zero")
    else:
        print(f"O número {n1} é negativa")
#Atividade 3
if n == 3:
    sexo = input("Digite o seu sexo\n[F] - Feminino\n[M] - Masculino\n:")
    if sexo.lower() == "m":
        print("Masculino.")
    elif sexo.lower() == "f":
        print("Feminino.")
    else:
        print("Sexo inválido!")
#Atividade 4
if n == 4:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("O programa pediu apenas UMA letra!")
    elif letra in "aeiou":
        print(f"A letra digitada [{letra}] é uma vogal!")
    elif letra.isdigit():
        print(f"Você digitou um número!")
    else:
        print(f"A letra digitada [{letra}] é um consoante!")
#Atividade 5
if n == 5:
    nota = 0
    for i in range(4):
        nota += float(input(f"Digite a {i+1}º nota do aluno\n:"))
    media = nota/4
    if media >= 6 and media < 10:
        print(f"Aluno aprovado!\nNota: {media:.2f}")
    elif media < 6:
        print(f"Aluno reprovado!\nNota: {media:.2f}")
    elif media == 10:
        print(f"Aprovado com distinção\nNota: {media:.2f}")
#Atividade 6
if n == 6:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    op = input(f"""
    Qual operação você deseja em fazer com esses números
        1º número: {n1}
        2º número: {n2}
    [SO] - Soma
    [MU] - Multiplicação
    [DI] - Divisão
    [MO] - Modulo
               """).upper()
    #Operações
    if op == "SO":
        r = n1+n2
    elif op == "MU":
        r = n1*n2
    elif op == "DI":
        r = n1/n2
    elif op == "MO":
        r = n1%n2
    #Resultado
    if r%2 == 1:
        print(f"O número é impar\nnúmero resultado: {r}")
    elif r%2 == 0:
        print(f"O número é par\nnúmero resultado: {r}")
    elif r > 0:
        print(f"O número é positivo\nnúmero resultado: {r}")
    elif r < 0:
        print(f"O número é negativo\nnúmero resultado: {r}")
#Atividade 7
if n == 7:
    num = int(input("digite um número no contador: "))
    for i in range(num):
        if i == 0:
            print(num)
        num -=1
        print(num)
#Atividade 8
if n == 8:
    numTab = int(input("digite um número da tabuada: "))
    for i in range(11):
        print(f"{i} X {numTab} = {numTab*i}")
#Atividade 9
if n == 9:
    palavra = input("Digite uma palavra\n:")
    cont,un = 0,0
    for i in palavra:
        if un == 0:
            if i.lower() in "aeiou":
                un = 1
        if un == 1:
            if i.lower() in "aeiou":
                cont +=1
    print(f"A palavra [{palavra}] contem {cont} de vogais")
#Atividade 10
if n == 10:
    for i in range(10):
        num = float(input(f"Digite o {i+1}º número: "))
        if num%2 != 1:
            print("O número é par!")
        else:
            print("O número é impar!")
#Atividade 11
if n == 11:
    palavra = input("Digite uma palavra\n:")
    vogal,cosoante,unV = 0,0,0
    for i in palavra:
        if unV == 0:
            if i.lower() in "aeiou":
                unV = 1
                continue
        if unV == 1:
            if i.lower() in "aeiou":
                vogal +=1
            else:
                cosoante +=1
    print(f"A palavra [{palavra}] contem {vogal} de vogais e {cosoante} de consoantes!")
#Atividade 12
if n == 12:
    nomArray,valArray = [],[]
    numComp,compSoma = 0,0
    a = str
    print("\nCaso queira encerrar a compra\nDigite '0' no nome do produto!\n")
    while True:
        print(f"\n| {numComp+1} |")
        # Verificação de nome:
        nom = input("\nDigite o nome do produto\n:")
        if nom != "0":
            if nom.isalpha() is not True:
                print("\n[ERRO 001]\nO nome do produto precisa ser uma [string] !")
                continue
            if len(nom) < 2:
                print("\n[ERRO 002]\nNome de produto não encontrado no sistema !")
                continue
        # Verificação de valor:
        if nom != "0":
            val = float(input("\nDigite o valor do produto em R$\n:"))
            if val <= 0:
                print("\n[ERRO 003]\nValor do produto invalido !")
                continue
        # Arrays conferirdos!
        if nom != "0":
            nomArray.insert(numComp,nom)
            valArray.insert(numComp,val)
        # Encerrar compra | loop
        if nom == "0":
            break
        else:
            numComp += 1
            for i in valArray:
                compSoma += 1
    # Formatação
    print(f"""
        =|{"="*150}|=
         |{" "*150}| 
        """)
    for nota in range(numComp):
        printNota = f"[{nota+1}] - {nomArray[nota]} = R${valArray:.2f}"
        print(f"""
         |{printNota:^150}| 
        """)
    print(f"""
         |{" "*150}| 
        =|{"="*150}|=
        
        TOTAL: R${compSoma:.2F}
          """
          )
# Atividade 13
if n == 13:
    while True:
        password = input("[USERNAME] digite uma senha!\n:")
        if len(password) < 8 or len(password) > 12:
            print("\n[ERRO: 010]\nSENHA INVALIDA!")
            if len(password) < 8:
                print("\n[ERRO: 011]\nA SENHA PRECISA TER MAIS QUE 8 CARACTERES!\n")
                continue
            else:
                print("\n[ERRO: 012]\nA SENHA PRECISA TER MENOS QUE 12 CARACTERES!\n")
                continue
        else:
            print("SENHA REGISTRADA!")
            break
#...