''' [PY-A08]
Você está desenvolvendo um programa para gerenciar uma lista de compras. 
O programa permite adicionar produtos à lista, visualizar a lista de produtos, atualizar
as informações de um produto existente e remover produtos da lista. Além disso, o programa
calcula o valor total de todos os produtos da lista.

O programa oferece as seguintes opções:
    1) → Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade
    e o valor unitário do produto. O programa calcula automaticamente o valor total do produto
    (quantidade * valor unitário) e atualiza o valor total de todos os produtos.

    2) → Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome
    do produto, o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total
    de todos os produtos da lista.

    3) → Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa
    solicita o nome do produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o
    valor unitário do produto. O programa recalcula automaticamente o valor total do produto e o valor total
    de todos os produtos.

    4) → Remover produto: O usuário pode remover um produto da lista informando o nome do produto que deseja
    remover. O programa atualiza automaticamente o valor total de todos os produtos.

    5) → Encerrar programa: Encerra a execução do programa.

O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um
dicionário com as informações: "produto", "valor", "quantidade" e "total". A variável totalProdutos
é utilizada para armazenar o valor total de todos os produtos da lista.

A cada operação realizada, o programa exibe mensagens indicando o resultado da operação.

Feito por: Lucas Aioria
Turma: 713
'''

#Import
from colorama import *
import random as rd
from os import system as sy
from A8_mod import proct_mod_def as p_d

totalProdutos = 0
lop_error,error_check = 0,False
d_produto = {}    # informação de produto: nome,valor,quantidade,valorTotal
l_produtos = []   # lista de produtos
while True:
    if lop_error == 0:
        user_choice = input("""
    Bem vindo ao programa de lista de compras!

        [1] → Adicionar um produto!
        [2] → Ver a lista de produtos!
        [3] → Atualizar produtos!
        [4] → Remover produto!
        
        [5] → Encerrar programa!
        
    -> """)
    else:
        user_choice = input("""
        [1] → Adicionar um produto!
        [2] → Ver a lista de produtos!
        [3] → Atualizar produtos!
        [4] → Remover produto!
        
        [5] → Encerrar programa!
        
    -> """)
    # User input check
    if user_choice.isnumeric() is False:
        sy('cls')
        print('\nO programa apenas aceita número como resposta!\nTente novamente!')
        error_check = True
    elif len(user_choice) < 1 or len(user_choice) > 1:
        sy('cls')
        print('\nNúmero fora das escolhas!\nTente novamente!')
        error_check = True
    if error_check is True or p_d.proct_check(l_produtos,user_choice) is True:
        lop_error = 1
        error_check = False
        continue
    # User choices
    match user_choice:
        # Adicionar produtos
        case '1':
            sy('cls')
            ad_pr = p_d.ad_proct()
            sy('cls')
            d_produto[ad_pr[0]] = ad_pr
            totalProdutos+=ad_pr[3]
            l_produtos.append(d_produto)
            print(f"""
        Nome do produto:        {ad_pr[0]}
        valor do produto:       R${ad_pr[1]}
        quantidade do produto:  {ad_pr[2]}
        total do produto:       R${ad_pr[3]} (quantidade X valor)
    
    {Fore.GREEN}Valor total dos produtos: R${totalProdutos}{Style.RESET_ALL}
                """)
        # Ver lista de produtos
        case '2':
            sy('cls')
            p_d.sh_procts(d_produto,totalProdutos)
        # Atualizar produto!
        case '3':
            sy('cls')
            l_update = p_d.up_procts(d_produto)
            sy('cls')
            match l_update[1]:
                # NAME UPDATE
                case '1':
                    print(f"Produto {l_update[0]} atualizado para {l_update[2]}")
                    d_produto[l_update[2]] = d_produto.pop(l_update[0])
                    d_val = d_produto[l_update[0]][1]
                    d_quan = d_produto[l_update[0]][2]
                    d_total = d_produto[l_update[0]][3]
                    d_produto.update({l_update[2]:[l_update[2],d_val,d_quan,d_total]})
                # QUANTITY UPDATE
                case '2':
                    print(f"Produto {l_update[0]} de {d_produto[l_update[0]][2]} atualizado para {l_update[2]}")
                    d_name = d_produto[l_update[0]][0]
                    d_val = d_produto[l_update[0]][1]
                    d_total = l_update[3]
                    d_produto.update({l_update[0]:[d_name,d_val,l_update[2],d_total]})
                    # Recalcula o valor total de todos os produtos
                    totalProdutos = 0
                    for key,info in d_produto.items():
                        totalProdutos+=d_produto[key][info[3]]
                # VALUE UPDATE
                case '3':
                    print(f"Produto {l_update[0]} de {d_produto[l_update[0]][1]} atualizado para {l_update[2]}")
                    d_name = d_produto[l_update[0]][0]
                    d_quan = d_produto[l_update[0]][2]
                    d_total = l_update[3]
                    d_produto.update({l_update[0]:[d_name,l_update[2],d_quan,d_total]})
                    # Recalcula o valor total de todos os produtos
                    totalProdutos = 0
                    for key,info in d_produto.items():
                        totalProdutos+=d_produto[key][info[3]]
        # Remover produto!
        case '4':
            sy('cls')
            d_remove = p_d.rm_proct(d_produto)
            sy('cls')
            print(f"Produto {d_remove} removido!")
            d_produto.pop(d_remove)
        # Encerrar programa!
        case '5':
            sy('cls')
            p_d.sh_procts(d_produto,totalProdutos)
            print(f'\n{Fore.RED}Programa finalizado!{Style.RESET_ALL}')
            break