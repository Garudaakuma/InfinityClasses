# IMPORT
import os

# Seletor de atividades!
n = int(input("Selecione uma atividade\n:"))
if n == 0:
  ...

# Array(lista) e suas funções:
"""
.
arryInt = [0,1,0,1,1,1]
for i in arryInt:
  if i == 0:
    arryInt.remove(i)
print(arryInt)
"""

# Dicionário:
'''
.
dic = {
  'abc':"ABC",
  123:123,
  1.05:2.5,
  True:False
      }
'''

# DICT COMPREHENSION
'''
.
dic = {num: num*10 for num in range(1,11)}
print(dic)
'''

# MÉTODO CONSTRUTOR
'''
.
dic = dict(username = "Renan",password = '123')
dic1 = dict( [ ("abc", '123'), ('0,5', 'True') ] )
print(dic,dic1)
'''

#Atividade 1
if n == 1:
  cpf,nom,ida,tele,dic,lop = 0,"",0,0,{},0
  while lop == 0:
    cpf = int(input("Digite seu CPF\n: "))
    nom = input("Digite o seu nome!\n: ")
    ida = int(input("Digite a sua Idade!\n: "))
    tele = int(input("Digite o seu telefone!\n: "))
    dic[cpf] = {'Nome':nom,'Idade':ida,'Telefone':tele}
    os.system('cls')
    print(dic)
    lop = int(input("Deseja continuar?\n[0] - Não\n[1] - Sim\n:"))
  while lop == 1:
    os.system('cls')
    cpfCall = int(input("Digite um CPF\n:"))
    confCPF = False
    for i in dic:
      if i == cpfCall:
        confCPF = True
    if confCPF == True:
      os.system('cls')
      print(dic[confCPF])
      break
    else:
      os.system('cls')
      print("CPF NÃO ENCONTRADO!\nTente novamnete!")
        

  # REVER APPEND E ADD NESTA LISTA!
  # QUER 3 DADOS QUE SEJAM INFORMADOS DE FORMA INFINITA

#Atividade 2
if n == 2:
  ''' Exercicio:
Leia os dados de um usuário - nome, sobrenome, idade, email - e
imprima-os enumerando os mesmos.
  '''
  cont,lop = 0,0
  dados,nome,sobrenome,idade,email = {},"","",0,""
  while lop == 0:
    id = len(dados)
    nome = input("Digite seu nome!\n:")
    sobrenome = input("Digite seu sobrenome!\n:")
    idade = int(input("Digite sua idade!\n:"))
    email = input("Digite seu email!\n:")
    dados[f"#{id}"] = [nome,sobrenome,idade,email]
    os.system('cls')
    print(dados)
    lop = int(input("Quer continuar?\n[0] - Sim\n[1] - Não\n:"))
  os.system('cls')
  #Dados coletados:
  for i in range(len(dados)):
    print(dados[f"#{i+1}"])

#Atividade 3
if n == 3:
  alunos,nota = {},[]
  soma,lop,Situ,nomAlu = 0,0,'',''
  while lop == 0:
    idAlu = len(alunos)
    nomAlu = input("Digite o nome do aluno: ")
    for i in range(4):
      nota.append(float(input(f"Digite a {i+1}º nota: ")))
      for o in range(int(nota[i])):
        soma+=1
    nota.sort()
    MaiorN = nota[3]
    MenorN = nota[0]
    if MaiorN == MenorN:
      MaiorN = 'Notas Iguais!'
    media = soma/4
    if media >= 7:
      Situ = "Passado!"
    else:
      situ = "Não Passado!"
    alunos[idAlu] = [nomAlu,nota,MaiorN,MenorN,media,Situ]
    nota,soma,media = [],0,0
    lop = int(input("Deseja continuar?\n[1] - Não\n[0] - Sim\n:"))
    nota.clear()
  # Print: 'alunos'
  os.system('cls')
  for i in alunos:
    print(f'AlunoID [{i}] -→ {alunos[i]}')

#Atividade 4
if n == 4:
  alunos,nota = {},[]
  soma,lop,Situ,nomAlu = 0,0,'',''
  while lop == 0:
    nomAlu = input("Digite o nome do aluno: ")
    for i in range(4):
      nota.append(float(input(f"Digite a {i+1}º nota: ")))
      for o in range(int(nota[i])):
        soma+=1
    nota.sort()
    media = soma/4
    if media >= 7:
      Situ = "Passado!"
    else:
      situ = "Não Passado!"
    alunos[media] = [nomAlu,nota,media,Situ]
    nota,soma,media = [],0,0
    lop = int(input("Deseja continuar?\n[1] - Não\n[0] - Sim\n:"))
    nota.clear()
  # Print: 'alunos'
  os.system('cls')
  sorted(alunos)    # Organiza as chaves para o Maior pro menor
  a=0
  for i in alunos:
    a+=1
    print(f'ID {a} -→ {alunos[i]}')