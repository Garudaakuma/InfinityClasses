#Import
from atividade_seletor import ativ_sel as a_s
from os import system as sy
import random

# Seletor de ativds
n = a_s()

#Atividade 1
if n == 1:
    '''Faça um algoritmo que calcule a media ponderada das notas de 3 provas.
    A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final,
    mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
    A nota para aprovação deve ser igual ou superior a 60 pontos.'''
    notas = []
    for n_nota in range(3):
        notas.append(float(input(f"Digite a nota n{n_nota+1}º\n-> ")))
    media = (notas[0]+notas[1]+(notas[2]*2))/4
    print(f'{media}\n{notas}\n')
    if media < 60:
        print('Aluno reprovado!')
    else:
        print('Aluno aprovado')
#Atividade 2
if n == 2:
    ...