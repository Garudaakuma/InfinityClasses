''' [PY-A07]
Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos
onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve
permitir adicionar, remover, atualizar e listar os alunos.

Para isso, você deve implementar um módulo que contém as seguintes funções:

    AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um
    aluno e adicione-o ao dicionário de alunos.

    RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno
    e remove-o do dicionário de alunos.

    AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um
    aluno e atualize o nome desse aluno no dicionário .

    VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula
    e o nome de cada um.
    
Lembre Se de Modularizar o código

Feito por: Lucas Aioria
Turma: 713
'''

#Import
from os import system as sy
from A7_mod import aluno_mod_def as a_d

lop_error,error_check = 0, False
alunos = {}
while True:
    if lop_error == 0:
        user_choice = input("""
    Bem vindo ao programa de matricula de alunos!

        [1] → Adicionar um aluno!
        [2] → Remover um aluno!
        [3] → Atualizar nome de aluno!
        [4] → ver todos os alunos!
        
        [5] → Sair
        
    -> """)
    else:
        user_choice = input("""
        [1] → Adicionar um aluno!
        [2] → Remover um aluno!
        [3] → Atualizar nome de aluno!
        [4] → ver todos os alunos!
        
        [5] → Sair
        
    -> """)
    # Checando o input do usuario!
    if user_choice.isnumeric() is False:
        sy('cls')
        print('\nO programa apenas aceita número como resposta!\nTente novamente!')
        error_check = True
    elif len(user_choice) < 1 or len(user_choice) > 1:
        sy('cls')
        print('\nNúmero fora das escolhas!\nTente novamente!')
        error_check = True
    if error_check is True:
        error_check = False
        lop_error = 1
        continue
    # Escolhas
    match user_choice:
        # Adicionar um aluno!
        case '1':
            sy('cls')
            ad = a_d.adicionar_aluno(alunos)
            alunos[ad[0]] = ad[1]
            sy('cls')
            print(f'\nAluno: {alunos[ad[0]]} -|- numº: {ad[0]}\nAluno adicionado!\n')
        # Remover um aluno ou remover todos os alunos!
        case '2':
            sy('cls')
            # Verifica se tem algum aluno para remover!
            if len(alunos) == 0:
                sy('cls')
                print('Não contem nenhum aluno para ser removido!\nTente novamente!\n')
                lop_error = 1
                continue
            # Dá a escolha de remover um ou todos os alunos!
            while True:
                clear_al = input("""
        Deseja remover um aluno em espeficio ou todos?
            [1] → Todos
            [2] → um aluno
        -> """)
                if clear_al.isnumeric() is False:
                    sy('cls')
                    print('O programa apenas aceita número como resposta!\nTente novamente!\n')
                    continue
                elif len(clear_al) < 1 or len(clear_al) > 1:
                    sy('cls')
                    print('Número fora das escolhas!\nTente novamente!\n')
                    continue
                match clear_al:
                    case '1':
                        alunos.clear()
                        print('Todos os alunos removidos!')
                        break
                    case '2':
                        remov_al = a_d.remover_aluno(alunos)
                        print(f'Aluno: {alunos[remov_al]} -|- numº: {remov_al}\nRemovido!')
                        del alunos[remov_al]
                        break
                    case other:
                        sy('cls')
                        print('Escolha não encontrada!\nTente novamente!\n')
        # Atualizar o nome de um aluno!
        case '3':
            sy('cls')
            # Verifica se tem algum aluno para ser atualizado!
            if len(alunos) == 0:
                sy('cls')
                print('Não contem nenhum aluno para ser atualizado!\nTente novamente!\n')
                lop_error = 1
                continue
            al_update = a_d.atualizar_aluno(alunos)
            print(f"Atualizado!\nAluno: {alunos[al_update[0]]} -|- numº: {al_update[0]}\nfoi para:")
            alunos.update({al_update[0]: al_update[1]})
            print(f"\nAluno: {alunos[al_update[0]]} -|- numº: {al_update[0]}")
        # Ver todos os alunos!
        case '4':
            sy('cls')
            # Verifica se tem algum aluno para ser atualizado!
            if len(alunos) == 0:
                sy('cls')
                print('Não contem nenhum aluno!\nTente novamente!\n')
                lop_error = 1
                continue
            for matric,aluno in alunos.items():
                print(f"| Aluno: {aluno} -||- matricula numº: {matric} |")
        # Sair do programa
        case '5':
            sy('cls')
            print("Programa finalizado!")
            break
        # Escolha acima ou abaixo de '5' ou '1'
        case other:
            sy('cls')
            lop_error = 1
            print('Escolha não encontrada!\nTente novamente!\n')
