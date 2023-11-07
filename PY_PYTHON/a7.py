# IMPORT
from atividade_seletor import ativ_sel
from os import system as sy

# Seletor de atividade
n = ativ_sel()

# Python Package index ( Comunidade de criação de modulos/bibliotecas )

# try and accept
'''.
palavra = input('Digite uma palavra!\n -> ')
def cont_word(word: str):
  "Conta a quantidade de caracteres em uma palavra!"
  try:
    if ' ' in word:
      raise Exception
  except Exception:
    print('Essa função apenas conta palavras!')
  else:
    return len(word)
print(cont_word(palavra))
'''

# Criação de modulos!
''' Modulo de palavra!
from a7_Modulos import caracteres as carac
palavra = input('Digite uma palavra!\n -> ')
print(f'\nquantidade de caracteres da palavra: {carac.cont_word(palavra)}\nPalavra: {palavra}\n')
'''
''' - Modulo de frase!
frase = input('Digite uma frase!\n -> ')
print(f'\nquantidade de caracteres da frase: {carac.cont_frase(frase)}\nFrase: {frase}\n')
'''

# Dunder objects __name__ e __main__

# Atividade 1
if n == 1:
  '''Fazer uma calculadora, tendo um menu!'''
  sy('cls')
  from a7_Modulos import calculadora as cal
  lop = 0
  while True:
    if lop == 0:
      choice_call = input(
      '''
  Bem vindo à calculadora Usuario!
  [som] - Some dois números!
  [sub] - Subtraia dois números!
  [mul] - Multiplique dois números!
  [div] - Dividade dois números!
      
  -> ''')
      cal_catch = cal.user_choice(choice_call)
      if cal_catch == 'error':
        sy('cls')
        print("\nVocê usuario digitou algo de errado!\nTente novamente!\n")
      else:
        sy('cls')
        lop = 1
        print(f'''
  Aqui está o resultado!
        
  primeiro número:      {cal_catch[0]}
  segundo número:       {cal_catch[1]}
  operação escolhida:   {cal_catch[3]}
  resultado:            {cal_catch[2]}
        ''')
    if lop == 1:
      continue_ask = input('''
  Deseja continuar?
    (sim) (não) 
  -> ''')
      if continue_ask == 'n' or continue_ask == 'não':
        sy('cls')
        print('programa finalizado')
        break
      elif continue_ask == 's' or continue_ask == 'sim':
        sy('cls')
        lop = 0
      else:
        sy('cls')
        print('\nerror você digitou algo de errado!\ntente novamente!\n')