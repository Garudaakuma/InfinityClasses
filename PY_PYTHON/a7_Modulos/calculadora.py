from os import system as sy

if __name__ == '__main__':
  sy('cls')
  print('\noops~!\nArquivo errado!\nEste arquivo não deve ser executado!\n')

soma = lambda x=int or float,y=int or float: x+y
subt = lambda x=int or float,y=int or float: x-y
mult = lambda x=int or float,y=int or float: x*y
divi = lambda x=int or float,y=int or float: x/y

def user_choice(choice:str) -> list:
  '''Faz o usuario digitar dois números
  \n retorna [ num_01, num_02, result, op_type ]'''
  choice_arry = ['som','sub','mul','div']
  if choice.isalpha() is False or choice not in choice_arry:
    print("Você não seleciono nenhuma das escolhas!")
    return 'error'
  else:
    sy('cls')
    num1 = int(input("Digite o primeiro número!\n -> "))
    num2 = int(input("Digite o segundo número!\n -> "))
    match choice:
      case 'som':
        return [num1,num2,soma(num1,num2),'soma']
      case 'sub':
        return [num1,num2,subt(num1,num2),'subtração']
      case 'mul':
        return [num1,num2,mult(num1,num2),'multiplicação']
      case 'div':
        return [num1,num2,divi(num1,num2),'divisão']