#Import
from os import system as sy

# Caso este arquivo for aberto mostar uma mensagem de erro!
if __name__ == '__main__':
  sy('cls')
  print('\noops~!\nArquivo errado!\nEste arquivo não deve ser executado!\nPor favor, execute arqui "A7.py"!\n')

# Check nome e matricula
def name_checker(name_call: str) -> bool:
    '''Verifica todos os criterios de um nome!
    \n retornando um booleano:
    \n 1) → False caso foi encontrado um erro!
    \n 2) → True caso não foi encontrado um erro!'''
    if name_call.isalpha() is False:
        sy('cls')
        print('O nome aluno só pode conter caracteres!\nTente novamente!\n')
        return False
    elif len(name_call) < 3:
        sy('cls')
        print('O nome só pode ser maior que 3 caracteres!\nTente novamente!\n')
        return False
    else:
        return True
def matric_checker(matric_call: str,list_call: bool,dict_call: dict) -> bool:
    '''Verifica todos os criterios da matricula e compara matriculas
    \n retornando um booleano:
    \n 1) → False caso foi encontrado um erro!
    \n 2) → True caso não foi encontrado um erro!'''
    if matric_call.isnumeric() is False:
            sy('cls')
            print('A matricula apenas aceita números!\nTente novamente!\n')
            return False
        # Verifica se contem uma matricula igual ao que foi digitado!
    if list_call is True:
        al_list = []
        for i in dict_call:
            al_list.append(i)
        for nums in range(len(al_list)):
            if matric_call == al_list[nums]:
                check_al = True
                break
            else:
                check_al = False
        if check_al is False:
            sy('cls')
            print('Matricula não encontrada!\nTente novamente!\n')
            return False
        else:
            return True

# Funções utlizadas no programa
def adicionar_aluno(d_c: dict) -> list:
    '''Pede ao usuario matricula e nome
    \nretornando uma lista com [ matricula , nome ]'''
    while True:
        matric = input("""
Digite o número da matricula do aluno!
    -> """)
        if matric_checker(matric,False,d_c) is False:
            continue
        else:
            break
    while True:
        alu_nome = input("""
Agora Digite o nome do aluno!
    -> """)
        if name_checker(alu_nome) is False:
            continue
        else:
            break
    return [matric,alu_nome]

def remover_aluno(al: dict) -> str:
    '''Ira pedir ao usuario qual aluno em especifico quer remover.
    \n retornando o número da matricula do aluno que será removido!'''
    while True:
        # Show All
        for alu in al:
            print(f"\naluno: {al[alu]} -|- numº: {alu}\n")
        matric_call = input("""
Por favor digite o número da matricula do aluno que deseja remover!
    -> """)
        if matric_checker(matric_call,True,al) is False:
            continue
        else:
            break
    return matric_call

def atualizar_aluno(al: dict) -> list:
    """Pede ao usuario a matricula do aluno que deseja atualizar o nome!
    \n assim retornando uma lista com [ matricula , nome atualizado ]"""
    #Verificar a matricula para mudança
    while True:
        # Show All
        for alu in al:
            print(f"\naluno: {al[alu]} -|- numº: {alu}\n")
        matric_call = input("""
Por favor digite o número da matricula do aluno que deseja atualizar!
    -> """)
        if matric_checker(matric_call,True,al) is False:
            continue
        else:
            sy('cls')
            break
    # digitar o nome atualizado do aluno
    while True:
        # Show All
        for alu in al:
            print(f"\naluno: {al[alu]} -|- numº: {alu}\n")
        name_update = input("""
Por favor digite o novo nome do aluno!
    -> """)
        if name_checker(name_update) is False:
            continue
        else:
            break
    return [matric_call,name_update]
