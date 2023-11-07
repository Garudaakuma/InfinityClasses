''' [PY-A05]
Considere uma lista de números inteiros:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
    1.Função map() para obter uma nova lista com o quadrado de cada número da lista numeros

    2.Função filter() para obter uma nova lista com números pares da lista numeros

    3.Função reduce()  para obter a soma de todos os números da lista numeros
Qual o resultado obtido após a execução das operações acima?

Feito por: Lucas Aioria
Turma: 713
'''

#Import
from os import system as sy
from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]
funMap = list(map(lambda num: num**2,numeros))
funFilter = list(filter(lambda num: False if num%2 else True,numeros))
funReduce = reduce(lambda x,y: x+y,numeros)
sy('cls')
print(f'''
    Números → {numeros}
    
        1º- Números ao quadrado →           {funMap}
        2º- Apenas os números pares →       {funFilter}
        3º- A soma de todos os números →    {funReduce}
      ''')