#Import
from atividade_seletor import ativ_sel as a_s
import json
from tkinter import *

#atividade seletor
n = 1

# TKINTER I
""" GUIs
Analogia - container(caixas) : Guarda os "objetos"

    Widgets
labels(Label)               → exibir texto
caixa_de_texto(Entry)       → input de dados ou texto
botões(Button)              → Botão que pode conter texto
frames(Frame)               → Usada para agrupar widgets
checkbox(Checkbutton)       → Uma caixa de seleção (liga,desliga)
radiobutton(Radiobutton)    → Uma caixa de seleção  para muitas seleções
combobox(Combobox)          → Exibir uma lista de opções disponiveis

    posicionamento
pack()
grid()
place()
'''
window = Tk()
window.focus()
window.title("Janela!")
window.geometry('640x540')
#widgets

Label
text = Label(
    text='Escreva algo aqui!'
text.pack()

#label(texto 'print')
intro = Label(text='Digite seu nome')
intro.pack()

#Input
name = Entry()
name.pack()

#Buton
def enter_data():
    print(name.get())
    name.delete(0,END)
botao = Button(window,
               text='SALVAR!',
               command=enter_data)
botao.pack()
'''
'''#Place
label_01 = Label(window,
                 width=10,
                 height=2,
                 text='nome')
label_01.place(x=10,y=100)

#Grid
label_02 = Label(window,
                 width=10,
                 height=2,
                 text='idade')
label_02.grid(row=2,column=1)
label_03 = Label(window,
                 width=10,height=2,
                 text='endereço')
label_03.grid(row=3,column=2)

window.mainloop()"""

#pode utilizar jason e sq_light

#Atividade 1
if n == 1:
    '''
    Cadastro de Alunos (com exibição no terminal) Crie um programa utilizando o Tkinter
    que permita ao usuário cadastrar alunos. O programa deve solicitar o nome, idade e
    nota do aluno por meio de caixas de entrada (Entry) e exibir um botão para
    cadastrar. Ao cadastrar um aluno, os dados devem ser exibidos no terminal.
    '''
    window = Tk()
    window.focus()
    window.title('Cadastro')
    window.geometry('255x160')
    
    #   nome_text
    text_name = Label(window,
                      height=2, width=15,
                      text='Nome do aluno →',
                      fg='#ffffff',bg='#6b6b6e')
    text_name.place(x=0,y=0)
    #entrada do nome
    input_name = Entry(fg='#ffffff',bg='#a7a7ab',
                       width=20)
    input_name.place(x=125,y=10)
    
    #   Idade_text
    text_idade = Label(window,
                      height=2, width=15,
                      text='Idade do aluno →',
                      fg='#ffffff',bg='#6b6b6e')
    text_idade.place(x=0,y=40)
    #entrada da idade
    input_idade = Entry(fg='#ffffff',bg='#a7a7ab',
                       width=20)
    input_idade.place(x=125,y=10+40)
    
    #   Nota_text
    text_nota = Label(window,
                      height=2, width=15,
                      text='nota do aluno →',
                      fg='#ffffff',bg='#6b6b6e')
    text_nota.place(x=0,y=40*2)
    #entrada da nota
    input_nota = Entry(fg='#ffffff',bg='#a7a7ab',
                       width=20)
    input_nota.place(x=125,y=10+(40*2))
    
    #Cadastro
    alunos = {}
    def cadastro():
        alunos[input_name.get()] = [input_idade.get(),input_nota.get()]
        # input_name.delete()
        # input_idade.delete()
        # input_nota.delete()
        print(alunos)

    b_cad = Button(window,
                   text='CADASTRAR!',
                   command=cadastro)
    b_cad.place(x=75,y=10+(40*3))
    
    window.mainloop()
#Atividade 2
if n == 2:
    '''
    Calculadora Simples (com exibição no terminal) Desenvolva uma calculadora
    simples utilizando o Tkinter que permita ao usuário realizar operações matemáticas
    básicas, como adição, subtração, multiplicação e divisão. O programa deve exibir
    botões para os números e as operações, e ao realizar o cálculo, o resultado deve ser
    exibido no terminal.
    '''
    window = Tk()
    window.focus()
    window.title('Calculadora')
    window.geometry('400x500')
    
    window.mainloop()
#Atividade 3
if n == 3:
    '''
    Conversor de Temperatura (com exibição no terminal) Crie um conversor de
    temperatura utilizando o Tkinter que permita ao usuário converter uma temperatura
    de Celsius para Fahrenheit ou vice-versa. O programa deve fornecer caixas de
    entrada (Entry) para o usuário inserir a temperatura de origem e exibir um botão
    para realizar a conversão. Ao realizar a conversão, o resultado deve ser exibido no
    terminal.
    '''
    ...
