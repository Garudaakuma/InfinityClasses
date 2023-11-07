
''' [PY-A02]
Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista.
Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de
números pares e ímpares presentes na lista, e a soma de todos os números
pares e ímpares, respectivamente.

Feito por: Lucas Aioria Serpa
Turma: 713
'''

#Import
from os import system as sy

num_arry = []
par,impar,som = [],[],0
for i in range(10):
    sy('cls')
    num_arry.append(int(input('Digite um número!\n-> ')))
for i in range(len(num_arry)):
    if num_arry[i]%2 == 0:
        par.append(num_arry[i])
    else:
        impar.append(num_arry[i])
    som+=num_arry[i]
par_tuple,impar_tuple = tuple(par),tuple(impar)
print(f"""
Aqui o resultado:
    Pares:
        Números pares:          {par_tuple}
        Quantia de pares:       [{len(par)}]
    Impares:
        Números impares:        {impar_tuple}
        Quantia de impares:     [{len(impar)}]
    Soma de pares e impares:    [{som}]
""")