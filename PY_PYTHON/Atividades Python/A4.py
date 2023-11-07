''' [PY-A04]
Desenvolva um programa em Python que permita ao usuário digitar várias notas.
Em seguida, crie uma função chamada "calcular_media" que irá receber as notas
digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao"
que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média
for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10"
se a média for igual a 10.

Feito por: Lucas Aioria
Turma: 713
'''

#Import
from os import system as sy

def calcular_media(notas:list[float]) -> float:
    '''Fara o trabalho de somar todas as notas e as dividindo.
    \n Desta forma retornando à média.'''
    soma,total_notas = 0,0
    for nota in notas:
        soma+=nota
        total_notas+=1
    media = soma/total_notas
    return media

def verificar_situacao(media_call:float) -> str:
    """Fara a verificação de aprovado e reprovado!
    \n Desta forma retornando:
    \n      1º → 'Parabéns, sua média é 10!'
    \n      2º → 'Passado'
    \n      3º → 'Reprovado' """
    ver_sit = lambda media=float: True if media >= 7.0 else False
    if media_call == 10:
        return 'Parabéns, sua média é 10!'
    elif ver_sit(media_call) is True:
        return 'Passado'
    else:
        return 'Reprovado'
    
notas,media = [],0
lop = 0
while True:
     if lop == 0:
         choiceUser = input('''
     Bem vindo ao programa de notas!
        
         O que deseja fazer?
         [1] → Adicionar uma nota
         [2] → Verificar a situação do aluno
         [3] → Limpar notas
        
         [4] → Sair
                    
     -> ''')
     elif lop == 1:
         choiceUser = input('''
         O que deseja fazer?
         [1] → Adicionar uma nota
         [2] → Verificar a situação do aluno
         [3] → Deletar todas as notas
        
         [4] → Sair
                        
     -> ''')
     if choiceUser.isnumeric() is False:
         sy('cls')
         lop = 1
         print("\n[Erro#001]\nAs escolhas apenas aceitam números!\nTente novamente!")
         continue
     elif len(choiceUser) > 1:
         sy('cls')
         lop = 1
         print("\n[Erro#002]\nEscolha não encontrada!\nTente novamente!")
     elif choiceUser != '1' and choiceUser != '2' and choiceUser != '3' and choiceUser != '4':
         sy('cls')
         lop = 1
         print("\n[Erro#003]\nEscolha não encontrada!\nTente novamente!")
     match choiceUser:
         # Adicionar uma nota
         case '1':
             sy('cls')
             quantNotasAsk = input('\nQuantas notas você deseja digitar?\n-> ')
             # Verificação de input
             if quantNotasAsk.isnumeric() is False:
                     sy('cls')
                     print("\n[Erro#004]\nA nota apenas aceita números!\nTente novamente!")
             quntNotas = int(quantNotasAsk)
             for i in range(quntNotas):
                 nota = input('\nDigite uma nota do aluno!\n-> ')
                 # Verificação de input
                 if nota.isnumeric() is False:
                     sy('cls')
                     print("\n[Erro#005]\nA nota apenas aceita números!\nTente novamente!")
                 elif float(nota) > 10:
                     sy('cls')
                     print("\n[Erro#006]\nA nota só pode ser igual ou menor que 10!\nTente novamente!")
                 elif float(nota) <= 0:
                     sy('cls')
                     print("\n[Erro#007]\nA nota não pode ser menor que zero!\nTente novamente!")
                 else:
                     notas.append(float(nota))
             media = calcular_media(notas)
             sy('cls')
         # Verificar a situação do aluno
         case '2':
             if media == 0 or len(notas) == 0:
                 sy('cls')
                 print("\n[Erro#008]\nNão contem nenhuma nota ou média no sistema!\nTente por notas no sistema primeiro!")
                 lop = 1
             else:
                 sy('cls')
                 for i in range(len(notas)):
                     print(f"nota{i+1}º: {notas[i]}")
                 print(f"\nMédia: {media:.2f}\nSituação: {verificar_situacao(media)}")
         # Deletar todas as notas na lista
         case '3':
             if media == 0 or len(notas) == 0:
                 sy('cls')
                 print("\n[Erro#009]\nNão contem nenhuma nota para ser deletado!\nTente por notas no sistema primeiro!")
                 lop = 1
             else:
                 sy('cls')
                 confirm = input("""
     Tem certeza se quer deletar todas as notas no sistema?
         [1] → Sim
         [2] → Não
            
     -> """)
                 # Imput confirm
                 if confirm.isnumeric is False:
                     sy('cls')
                     print('\n[Erro#010]\nApenas aceita números!\nSerá negado automaticamente!')
                     lop = 1
                 elif confirm != '1' and confirm != '2':
                     sy('cls')
                     print('\n[Erro#011]\nOpção não encontrada!\nSerá negado automaticamente!')
                     lop = 1
                 elif confirm == '2':
                     sy('cls')
                     lop = 1
                 else:
                     sy('cls')
                     print("\nNotas no sistema deletado!")
                     notas.clear()
         # Sair do programa!
         case '4':
             sy('cls')
             print("Programa de notas finalizado!")
             break
