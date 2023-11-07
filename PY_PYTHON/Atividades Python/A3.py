''' [PY-A03]
Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números 
de matrícula usando um dicionário.

O programa deve fornecer as seguintes funcionalidades:
    Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de 
    um aluno ao dicionário.

    Remover um aluno: O usuário poderá remover um aluno do dicionário informando o 
    número de matrícula.

    Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados
    no dicionário, exibindo seus respectivos números de matrícula.

    O programa deve ser executado em um loop contínuo até que o usuário escolha sair.

Feito por: Lucas Aioria Serpa
Turma: 713
'''

#Import
from os import system as sy 

input_check = 0
alunos = {}
while True:
    if input_check == 0:
        user_choice = input("""
Bem vindo ao programa de alunos e matriculas!
    
    O que você deseja fazer?
        [1] - Adicionar um Aluno!
        [2] - Remover um Aluno!
        [3] - Visualizar todos os alunos!
        
        [4] - Sair do programa!
                            
            -> """)
    else:
        user_choice = input("""
    O que você deseja fazer?
        [1] - Adicionar um Aluno!
        [2] - Remover um Aluno!
        [3] - Visualizar todos os alunos!
        
        [4] - Sair do programa!
                            
            -> """)
    # Sinaliza o erro do input
    if user_choice.isnumeric() is False:
            sy('cls')
            print("\nErro!\nVocê precisa digitar o número da escolha!\nPor favor, tente novamente!")
            input_check = 1
            continue
    # Adiciona um aluno
    if user_choice == '1':
        sy('cls')
        while True:
            # Verifica o input do nome (Apenas aceita caracteres)
            if input_check != 2:
                aluno_name_call = input("Por favor, digite o nome do aluno!\n-> ")
                if aluno_name_call.isalpha() is False:
                    sy('cls')
                    print("Erro!\nO nome aluno só pode ter caracteres!")
                else:
                    input_check = 2
            # Verifica o input da matricula (Apenas aceita númerors)
            else:
                matricula_call = input("Pefeito, agora digite a matricula do aluno\n-> ")
                if matricula_call.isnumeric() is False:
                    sy('cls')
                    print("Erro!\nO número da matricula apenas aceita números!")
                else:
                    input_check = 3
            # Mostra o aluno adicionado
            if input_check == 3:
                sy('cls')
                alunos[matricula_call] = aluno_name_call
                print(f"\nAluno adicionado!\nMatricula -> {matricula_call}\nAluno -> {aluno_name_call}")
                input_check = 1
                break
    # Remove um aluno
    elif user_choice == '2':
        sy('cls')
        remove_try = 0
        if len(alunos) == 0:
            print("não tem nenhum aluno para remover!")
        else:
            while True:
                # Mostrar todos os alunos que podem ser removidos
                for i in alunos:
                    print(f"Matricula (chave) -> {i}\nNome do aluno -> {alunos[i]}")
                remove_aluno = input("\nDigite a matricula do aluno que deseja remover!\n-> ")
                # Verifica se o input está no dicionarrio
                for matri in alunos:
                    if remove_aluno == matri:
                        alunos.pop(remove_aluno)
                        remove_try = 0
                        break
                    else:
                        remove_try = 1
                if remove_aluno.isnumeric() is False:
                    sy('cls')
                    print('Erro!\nA matricula apenas contem números!\nTente novamente!')
                elif remove_try != 0:
                    sy('cls')
                    print('Erro!\nMatricula não encontrada\nTente novamente!')
                else:
                    sy('cls')
                    print("\nAluno removido!")
                    input_check = 1
                    break
    # Mostra todos os alunos
    elif user_choice == '3':
        sy('cls')
        if len(alunos) == 0:
            print("não tem nenhum aluno no dicionario!")
        else:
            for i in alunos:
                print(f"Matricula -> {i}\nNome do aluno -> {alunos[i]}")
        input_check = 1
    # Finaliza o program/while
    elif user_choice == '4':
        sy('cls')
        print('Programa Finalizado!')
        break