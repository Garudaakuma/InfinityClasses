# IMPORT
import os

# Atividade seletor
def sa(n: int):
  '''Função que seleciona uma atividade!'''
  if n == 0:
    os.system('cls')
    print("Nenhuma atividade foi selecionado!\n")
  return n
n = sa(int(input("Selecione uma atividade\n:")))

# evento: "BAHIA TECH EXPERIENCE"

# Funções
'''.
def media_alunos():
  soma,nota = 0,0
  for i in range(5):
    nota = int(input(f"digite a {i+1}º:"))
    for i in range(nota):
      soma+=1
  media = soma/5
  os.system('cls')
  return media
print(media_alunos())
'''

# Atividade 1
if n == 1:
  def saudacao(nome: str) -> str:
    '''Parametro que retorna uma saúdação!
    \n(retorna uma str)'''
    return f"Olá, {nome}!"
  print(saudacao(input("Digite seu nome!\n: ")))
  
# Atividade 2
if n == 2:
  def imc(peso: float,altura: float) -> float:
    imcform = peso/(altura**2)
    return imcform
  arryImc = []
  for i in range(4):
    p = float(input("Digite seu peso!\n: "))
    h = float(input("Digite sua altuta!\n: "))
    arryImc.append(imc(p,h))
  print(f"Os IMCs calculados foram: {arryImc}")

# Atividade 3
if n == 3:
  def cont_word(word: str):
    '''Contador de palavras de frases!'''
    space,wordcont,sinais = 0,0,0
    for i in word:
      if i in "!@#$%¨¨''&*()_+`[]^~]}{;:/.><,\|":
        sinais+=1
      elif i == " ":
        space+=1
      else:
        wordcont+=1
    return wordcont,space,sinais
  word = input("Digite uma frase ou uma palavra!\n: ")
  print(cont_word(word))
  
# Atividade 4
if n == 4:
  def val_hora(valor: float,hora: int) -> float:
    '''Calcula o valor por hora trabalhada!'''
    valhora = valor/hora
    return valhora
  valor = float(input("Digite quanto você ganhou no seu salario!\n: "))
  hora = int(input("Digite quantas horas você trabalhou neste més!\n: "))
  print(val_hora(valor,hora))

# Atividade 5
if n == 5:
  def operador(n1: float,n2: float) -> str:
    """Seletor de operadores ! ! !
    \n soma, substração, multiplicação e divisão"""
    op = input("""
    Digite qual operação você deseja:
    "som" -> Soma
    "sub" -> Subtração
    "mul" -> Multiplicação
    "div" -> Divisão
    
    :""")
    match op.lower():
      case "som":
        n3 = n1+n2
      case "sub":
        n3 = n1-n2
      case "mul":
        n3 = n1*n2
      case "div":
        n3 = n1/n2
        if n2 == 0:
          print("ERRO!\nNão é possivel dividir por zero!")
          n3 = 0
    return n3
  lop = 0
  while True:
    os.system('cls')
    num1 = float(input("Digite seu primeiro número\n: "))
    num2 = float(input("Digite o segundo número!\n: "))
    print(f"Aqui o resultado da operação!\n:{operador(num1,num2)}")
    lop = int(input("\nDeseja continuar?\n[0] -> Sim\n[1] -> Não\n:"))
    if lop != 0:
      os.system('cls')
      print("SISTEMA FINALIZADO !!!")
      break

