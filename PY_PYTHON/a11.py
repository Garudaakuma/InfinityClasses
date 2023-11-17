#Import
from atividade_seletor import ativ_sel as a_s
from os import system as sy
from datetime import datetime
import random as rd

#Atividade seletor
n = a_s()

# P.O.O. -→ {Programação Orientada a Objetos}
'''
    Classe → conceito (ex:Carro)
    Objeto → execução (ex:Celta rebaixado)

        class Carro():
            def __init__ (self, marca:str, modelo:str, ano:int, peso:float, possui_4_portas:bool):
                self.marca = marca
                self.modelo = modelo
                self.ano = ano
                self.peso = peso
                self.possui_4_portas = possui_4_portas
                
            def definir_idade_carro(self):
                idade_carro = datetime.today().year - self.ano
                print(f'{self.marca} - {self.modelo} tem {idade_carro} anos!')
            
            buzinar = lambda self: print(f'{self.marca} - {self.modelo} está emitindo som!')
            ligar = lambda self: print(f'{self.marca} - {self.modelo} ligou!')
            desligar = lambda self: print(f'{self.marca} - {self.modelo} desligou!')
            frear = lambda self: print(f'{self.marca} - {self.modelo} está freando!')
    carro_do_pf_renan = Carro('Toyota','Hilux',2011,2000,True)
    carro_do_pf_renan.ligar()
'''

#Atividade 1
if n == 1:
    phase = 0
    p_i = False
    id_fat = 0
    fatura = {}
    class ClFatura():
            '''Definição de itens e calculo de fatura
            \n.fatura → calculo da fatura (quantidade * preço)'''
            def __init__ (self, nome:str,preco:float,quant:int):
                self.nome = nome
                self.preco = preco
                self.quant = quant
            fatura = lambda self: float(self.quant * self.preco)
    while True:
        match phase:
            # Nome do item
            case 0:
                nome_item = input('Digite o nome do item\n-> ')
                sy('cls')
                if nome_item.isalpha() is False:
                    print('Erro!\nApenas Aceita caracteres!')
                    continue
                else:
                    phase = 1
                    continue
            # Preço do item
            case 1:
                preco_item = input('Digite o preço do item\n-> ')
                sy('cls')
                for i in preco_item:
                    if i == ',':
                        print('Erro!\nApenas aceita [.] como divisão decimal')
                        p_i = False
                        break
                    if i.isnumeric() is True:
                        p_i = True
                    else:
                        p_i = False
                if p_i == False:
                    print('Erro!\nO correu um erro!\nApenas aceita números inteiros e quebrados!')
                else:
                    phase = 2
                    continue
            # Quantidade do item
            case 2:
                quant_item = input('Digite a quantidade do item\n-> ')
                sy('cls')
                if quant_item.isnumeric() is False:
                    print('Erro!\nApenas aceita números inteiros!')
                else:
                    phase = 3
                    if len(fatura) > 0:
                        id_fat += 1
                    fatura[id_fat] = ClFatura(nome_item,float(preco_item),int(quant_item))
                    continue
            # Continuar ask?
            case 3:
                user_continue_ask = input('Deseja continuar?\n[0] - Sim\n[1] = Não\n-> ')
                sy('cls')
                if user_continue_ask.isnumeric() is False:
                    print('Erro!\nApenas aceita 0 e 1 como resposta!')
                elif len(user_continue_ask) > 1:
                    print('Erro\nEscolha não encontrada!')
                else:
                    if user_continue_ask == '0':
                        phase = 0
                        continue
        #Show all
        tot_qnt = 0
        tot_prc = 0
        for key_id,item in fatura.items():
            tot_qnt+=fatura[key_id].quant
            tot_prc+=fatura[key_id].preco
            print(f'''
    |]-( ID → {key_id} )------------------------------------------------→>|
    |
    |   Nome do item:           {fatura[key_id].nome}
    |   Preço do produto:       {fatura[key_id].preco}
    |   Quantidade do produto:  {fatura[key_id].quant}
    |   
    |   Valor total da fatura do item → {fatura[key_id].fatura()}
    |]------------------------------------------------------------------→>|
                ''')
        print(f'''
        Fatura total = {tot_qnt*tot_prc}
              ''')
        break