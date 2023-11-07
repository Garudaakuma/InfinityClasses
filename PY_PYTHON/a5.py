# IMPORT
import os
import random

# Seletor de atividades
def sa(n: int):
  '''Função que seleciona uma atividade!'''
  if n == 0:
    os.system('cls')
    print("Nenhuma atividade foi selecionado!\n")
  return n
n = sa(int(input("Selecione uma atividade\n:")))

# Revisão de função:
'''.
def maior_menor(n1: float,n2: float) -> str:
  if n1 == n2:
    return "n1 e n2 são iguais!"
  elif n1 > n2:
    return "n1 é maior!"
  else:
    return "n2 é maior!"
num01,num02 = random.randint(0,10),random.randint(0,10)
print(maior_menor(num01,num02))
'''

# '*'args: <-- Estudar mais afundo sobre!
'''.
def args_def(a,b,*args):
  return print(a,b,*args)
print(args_def(1,1,10,5))
'''

# '**'kwargs: <-- Estudar mais afundo sobre!
'''.
def kwargs_def(**kwargs):
  print(kwargs)
  for key, valor in kwargs.items():
    print(f"{key}:{valor}")
print(kwargs_def(number=random.randint(0,10),string='abobora!',floated=0.10))
'''

# lambda: <-- Estudar mais afundo sobre!
'''.
quad = lambda number: number**2
print(quad(20))
impar_par = lambda number: 'Par' if number % 2 == 0 else 'Impar'
print(impar_par(5))
  # LISTEM COMPRESSION LAMBDA
par = lambda start,final: [i for i in range(start,final) if i % 2 == 0]
print(par(0,10))
'''

# lambda functions (map,filter,reduce)
'''.
nums = [1,2,3,4,5]
  # map()     # Aplica algo na sua lista!
print(list(map(lambda x: x**2,nums)))
  # filter()  # Se for verdade a função ele retorna a função!
print(list(filter(lambda x: x%2 == 0,nums)))
  # reduce()  # Reduz/Soma sua lista!
from functools import reduce
print(reduce(lambda x,y: x+y,nums))
'''

# Atividade 1
if n == 1:
  varStr = input("Digite uma palavra\n: ")
  """. Metodo lop+arry
  def reverse_string(word: str) -> str:
    '''Inverte uma string'''
    arry_str,rev_str = [],''
    for i in word:
      arry_str.append(i)
    arry_str.reverse()
    for arry_i in range(len(arry_str)):
      rev_str+=arry_str[arry_i]
    return rev_str
  print(reverse_string(varStr))
  """
  """. Metodo arry
  def reverse_str(word: str) -> str:
    return word[::-1]
  print(reverse_str(varStr))
  """
# Atividade 2
if n == 2:
  def maior_menor(n1: float,n2: float) -> str:
    if n1 == n2:
      return "n1 e n2 são iguais!"
    elif n1 > n2:
      return "n1 é maior!"
    else:
      return "n2 é maior!"
  num01,num02 = random.randint(0,10),random.randint(0,10)
  print(maior_menor(num01,num02))
# Atividade 3
if n == 3:
  def bigger_word(words: list) -> str:
    conter,position = 0,0
    for i in range(len(words)):
      if len(words[i]) == conter:
        os.system('cls')
        print("ERRO!\n Palavras com mesmo número de letras!\nTENTE NOVAMENTE!")
        break
      elif len(words[i]) > conter:
        conter = len(words[i])
        position = i
    return words[position]
  print(bigger_word(['Paulo','Ricardo','PAULA','MAFUNTISFADIGES PEREIRA CARDOSO']))
# Atividade 4
if n == 4:
  """
  Crie uma função que recebe uma lista de cores e as imprime em sequência, criando
  um efeito visual de cores.
  use essa lista para inserir como argumento no parâmetro de sua função:
  cores = ['\033[44m','azul',
          '\033[0;0m',
          '\033[42m''verde',
          '\033[0;0m',
          '\033[43m','amarelo',
          '\033[0;0m']
  """
  def effect_color(colors: list) -> None:
    for color in colors:
      print(color)
  print(effect_color(['\033[44m','azul','\033[42m','verde','\033[43m','amarelo']))
# Atividade 5
if n == 5:
  impar_par = lambda numb: f'{numb}\nPar!' if numb%2 == 0 else f'{numb}\nImpar!'
  print(impar_par(random.randint(0,10)))
# Atividade 6
if n == 6:
  cont_lamdba = lambda str01,str02: 'Erro!' if len(str01) < 5 and len(str02) < 5 else str01 + str02
  print(cont_lamdba('a23','b23'))
# Atividade 7
if n == 7:
  lambda_num = lambda numb: numb if numb >= 10 else f'{numb}\n{numb/2}'
  print(lambda_num(random.randint(0,10)))
# Atividade 8
if n == 8:
  div_num = lambda num: 'Divisivel!' if num%3 == 0 and num%5 == 0 else 'Não divisivel!'
  print(div_num(30))
# Atividade 9
if n == 9:
  strList = ['abacate','avocato','pera','maça','pera','alface :thumbup:']
  print(list(map(lambda x: x.upper(), strList)))
# Ativadede 10
if n == 10:
  strList = ['abacate','avocato','pera','maça','pera','alface :thumbup:']
  print(list(filter(lambda x: len(x) > 5, strList)))
# Atividade 11
if n == 11:
  from functools import reduce
  intList = []
  for i in range(11):
    intList.append(random.randint(0,10))
  print(reduce(lambda x,y: x+y,intList))
# Atividade 12
if n == 12:
  dictNameAge = {0:['Carlos',20],
                 1:['Pedro',25],
                 2:['CARLINHOS DA ESQUINA',1469]}
  arry_dictName = list(map(lambda name: dictNameAge[name][0],dictNameAge))
  print(arry_dictName)
