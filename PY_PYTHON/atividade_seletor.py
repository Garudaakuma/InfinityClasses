# Import
from os import system

# format Seletor!
n = int
def ativ_sel() -> int:
  num = 0
  while True:
    num_call = input("Selecione uma atividade!\n -> ")
    if num_call.isnumeric():
      num = int(num_call)
      break
    else:
      system('cls')
      print("Você digitou algo de errado!\nTente novamente!\n")
  if num == 0:
    system('cls')
    print("\nNenhuma Atividade selecionada!\n")
  return num
# Atividade debug
if n == 1:
    print('Primeira Atividade selecionada!')