#Import
from colorama import *
from os import system as sy

# Caso este arquivo for aberto mostar uma mensagem de erro!
if __name__ == '__main__':
  sy('cls')
  print('\noops~!\nArquivo errado!\nEste arquivo não deve ser executado!\nPor favor, execute arqui "A8.py"!\n')

def proct_check(l_proct: list,c_user: str) -> bool:
    if c_user == '1' or c_user == '5':
        return False
    else:
        if len(l_proct) < 1:
            sy('cls')
            match c_user:
                case '2':
                    print('Não contem nenhum produto na lista!\nTente novamente!\n')
                case '3':
                    print('Não contem nenhum produto à ser atualizado!\nTente novamente!\n')
                case '4':
                    print('Não contem nenhum produto à ser removido!\nTente novamente!\n')
                case other:
                    print('Escolha não encontrada!\nTente novamente!\n')
            return True

def ad_proct() -> list:
    '''Pede ao usuario informaçõe sobre o produto que quer adicionar
    \n Assim retornando uma lista com [ nome , valor , quantidade , valorTotal ]'''
    # Nome do produto
    while True:
        name_proct = input('Por favor digite o nome do produto!\n-> ')
        if name_proct.isalpha() is False:
            sy('cls')
            print('O nome do produto só pode conter caracteres!\nTente novamente!\n')
            continue
        elif len(name_proct) < 3:
            sy('cls')
            print('O nome só pode ser maior que 3 caracteres!\nTente novamente!\n')
            continue
        else:
            break
    # Valor do produto
    while True:
        valor_proct = input(f'Agora digite o valor da(o) {name_proct}!\n-> ')
        if valor_proct.isnumeric() is False:
            sy('cls')
            print('O valor do produto só pode conter números!\nTente novamente!\n')
            continue
        elif len(valor_proct) < 1 or valor_proct == '0':
            sy('cls')
            print('O produto precisa ser maior que zero!\nTente novamente!\n')
            continue
        else:
            break
    # Quantidade de produtos
    while True:
        quant_proct = input(f'Agora digite o número de produtos de {name_proct}!\n-> ')
        if quant_proct.isnumeric() is False:
            sy('cls')
            print('O número de produtos só pode conter números!\nTente novamente!\n')
            continue
        elif len(quant_proct) < 1 or quant_proct == '0':
            sy('cls')
            print('Precisa conter pelo menos 1 produto!\nTente novamente!\n')
            continue
        else:
            break
    q_p = int(quant_proct)
    v_p = float(valor_proct)
    total_proct = q_p*v_p
    return [name_proct,valor_proct,quant_proct,total_proct]

def sh_procts(d_proct_infos: dict,t_proct: float):
    '''Mostra todos os produtos e suas informações!'''
    for key,infos in d_proct_infos.items():
        print(f"""    
        nome do produto:        {key}
        valor do produto:       R${infos[1]}
        quantidade do produto:  {infos[2]}
        valor total do produto: R${infos[3]}
        """)
    print(f'{Fore.GREEN}Valor total dos produtos: R${t_proct}{Style.RESET_ALL}')

def up_procts(d_proct_infos: dict) -> list:
    '''Menu de atualização de produtos!
    \n Retorna uma lista [ nome , escolha , update ]'''
    # Produto que deseja mudar
    while True:
        names = []
        for key,infos in d_proct_infos.items():
            print(f"Nome do produto: {infos[0]}\n")
            names.append(infos[0])
        name_call = input("Digite o nome do produto que deseja atualizar!\n-> ")
        error_name = False
        for name in range(len(names)):
            if names[name] == name_call:
                error_name = False
                break
            else:
                error_name = True
        if error_name is True:
            sy('cls')
            print('Nome não encontrado!\nTente novamente!\n')
            continue
        else:
            break
    # Menu de edição dos produtos!
    error_check = False
    while True:
        user_choice = input("""
        [1] → Editar nome!
        [2] → Editar quantidade!
        [3] → Editar valor unitário!

    -> """)
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
            continue
        match user_choice:
            # Edita o nome!
            case '1':
                while True:
                    name_up = input('Por favor digite o novo nome do produto!\n-> ')
                    if name_up.isalpha() is False:
                        sy('cls')
                        print('O nome do produto só pode conter caracteres!\nTente novamente!\n')
                        continue
                    elif len(name_up) < 3:
                        sy('cls')
                        print('O nome só pode ser maior que 3 caracteres!\nTente novamente!\n')
                        continue
                    else:
                        break
                return [name_call,user_choice,name_up]
            # Edita a quantidade!
            case '2':
                while True:
                    quant_proct = input(f'Agora digite o novo número de produtos de {name_call}!\n-> ')
                    if quant_proct.isnumeric() is False:
                        sy('cls')
                        print('O número de produtos só pode conter números!\nTente novamente!\n')
                        continue
                    elif len(quant_proct) < 1 or quant_proct == '0':
                        sy('cls')
                        print('Precisa conter pelo menos 1 produto!\nTente novamente!\n')
                        continue
                    else:
                        break
                q_p = int(quant_proct)
                v_p = float(d_proct_infos[name_call][1])
                total_proct = q_p*v_p
                return [name_call,user_choice,quant_proct,total_proct]
            # Edita valor unitário
            case '3':
                while True:
                    valor_proct = input(f'Agora digite o valor da(o) {name_call}!\n-> ')
                    if valor_proct.isnumeric() is False:
                        sy('cls')
                        print('O valor do produto só pode conter números!\nTente novamente!\n')
                        continue
                    elif len(valor_proct) < 1 or valor_proct == '0':
                        sy('cls')
                        print('O produto precisa ser maior que zero!\nTente novamente!\n')
                        continue
                    else:
                        break
                q_p = int(d_proct_infos[name_call][2])
                v_p = float(valor_proct)
                total_proct = q_p*v_p
                return [name_call,user_choice,valor_proct,total_proct]
            case other:
                sy('cls')
                print('Escolha não encontrada!\nTente novamente!')
                continue

def rm_proct(d_proct_infos: dict) -> str:
    while True:
        names = []
        for key,infos in d_proct_infos.items():
            print(f"Nome do produto: {infos[0]}\n")
            names.append(infos[0])
        name_call = input("Digite o nome do produto que deseja remover!\n-> ")
        error_name = False
        for name in range(len(names)):
            if names[name] == name_call:
                error_name = False
                break
            else:
                error_name = True
        if error_name is True:
            sy('cls')
            print('Nome não encontrado!\nTente novamente!\n')
            continue
        else:
            break
    return name_call