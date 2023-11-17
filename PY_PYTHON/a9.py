#Import
from atividade_seletor import ativ_sel as a_s
from os import system as sy
from tkinter import *

#atividade seletor
n = 2

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
        print(alunos)

    b_cad = Button(window,
                   text='CADASTRAR!',
                   command=cadastro)
    b_cad.place(x=75,y=10+(40*3))
    
    window.mainloop()
#Atividade 2 → to be continue
if n == 2:
    '''
    Calculadora Simples (com exibição no terminal) Desenvolva uma calculadora
    simples utilizando o Tkinter que permita ao usuário realizar operações matemáticas
    básicas, como adição, subtração, multiplicação e divisão. O programa deve exibir
    botões para os números e as operações, e ao realizar o cálculo, o resultado deve ser
    exibido no terminal.
    '''
    
    #colors
    c_bg = '#141417'
    c_txt = '#f2f2fa'
    
    # commands for buttons
    number = []
    numbers = {0:[],1:[]}
    operations = {'+':False,
                  '-':False,
                  '*':False,
                  '/':False}
    input_num = [0]
    input_ope = ['None']
    dict_num = {0:[False,False,False,False,False,False,False,False,False,False,False],
                1:[False,False,False,False,False,False,False,False,False,False,False]}
    
    #show all numbers
    def show_num(num_list: list) -> str:
        show_numb = ''
        for num in num_list:
            show_numb = show_numb+num
        return str(show_numb)
    #status print all
    def show_print(call: str):
        '''match call:
            #Call_num()
            case 'c_n':
                if len(numbers[0]) == 0 and len(numbers[1]) >= 1:
                    sy('cls')
                    second_num = int(show_num(numbers[1]))
                    return print(f'num [01]:    None\noperation:   {input_ope[0]}\nnum [02]:    {second_num}')
                elif len(numbers[0]) >= 1 and len(numbers[1]) == 0:
                    sy('cls')
                    first_num = int(show_num(numbers[0]))
                    return print(f'num [01]:    {first_num}\noperation:   {input_ope[0]}\nnum [02]:    None')
                else:
                    sy('cls')
                    first_num = int(show_num(numbers[0]))
                    second_num = int(show_num(numbers[1]))
                    return print(f'num [01]:    {first_num}\noperation:   {input_ope[0]}\nnum [02]:    {second_num}')
            #Call_ope()
            case 'c_o':
                if len(numbers[0]) == 0 and len(numbers[1]) == 0:
                    sy('cls')
                    return print(f'num [01]:    None\noperation:   {input_ope[0]}\nnum [02]:    None')
                elif len(numbers[0]) == 0 and len(numbers[1]) >= 1:
                    sy('cls')
                    second_num = int(show_num(numbers[1]))
                    return print(f'num [01]:    None\noperation:   {input_ope[0]}\nnum [02]:    {second_num}')
                elif len(numbers[0]) >= 1 and len(numbers[1]) == 0:
                    sy('cls')
                    first_num = int(show_num(numbers[0]))
                    return print(f'num [01]:    {first_num}\noperation:   {input_ope[0]}\nnum [02]:    None')
                else:
                    sy('cls')
                    first_num = int(show_num(numbers[0]))
                    second_num = int(show_num(numbers[1]))
                    return print(f'num [01]:    {first_num}\noperation:   {input_ope[0]}\nnum [02]:    {second_num}')
            #Call_next()
            case 'c_nxt':
                print(input_num[0])
                match input_num[0]:
                    #NUM[02]
                    case 1:
                        if len(numbers[0]) == 0 and len(numbers[1]) == 0:
                            sy('cls')
                            return print(f'num [01]:    None\noperation:   {input_ope[0]}\nnum [02]:    None ← SELECTED')
                        elif len(numbers[0]) == 0 and len(number[1]) >= 1:
                            sy('cls')
                            second_num = int(show_num(numbers[1]))
                            return print(f'num [01]:    None\noperation:   {input_ope[0]}\nnum [02]:    {second_num} ← SELECTED')
                        elif len(numbers[0]) >= 1 and len(numbers[1]) == 0:
                            sy('cls')
                            first_num = int(show_num(numbers[0]))
                            return print(f'num [01]:    {first_num}\noperation:   {input_ope[0]}\nnum [02]:    None ← SELECTED')
                        else:
                            sy('cls')
                            first_num = int(show_num(numbers[0]))
                            second_num = int(show_num(numbers[1]))
                            return print(f'num [01]:    {first_num}\noperation:   {input_ope[0]}\nnum [02]:    {second_num} ← SELECTED')
                    #NUM[01]
                    case 0:
                        if len(numbers[0]) == 0 and len(numbers[1]) == 0:
                            sy('cls')
                            return print(f'num [01]:    None ← SELECTED\noperation:   {input_ope[0]}\nnum [02]:    None')
                        elif len(numbers[0]) == 0 and len(number[1]) >= 1:
                            sy('cls')
                            second_num = int(show_num(numbers[1]))
                            return print(f'num [01]:    None\noperation:   {input_ope[0]}\nnum [02]:    {second_num} ← SELECTED')
                        elif len(numbers[0]) >= 1 and len(numbers[1]) == 0:
                            sy('cls')
                            first_num = int(show_num(numbers[0]))
                            return print(f'num [01]:    {first_num} ← SELECTED\noperation:   {input_ope[0]}\nnum [02]:    None')
                        else:
                            sy('cls')
                            first_num = int(show_num(numbers[0]))
                            second_num = int(show_num(numbers[1]))
                            return print(f'num [01]:    {first_num} ← SELECTED\noperation:   {input_ope[0]}\nnum [02]:    {second_num}')'''
    #Numbers calls
    def call_0():
        user_choice = input_num[0]
        dict_num[user_choice][0] = True
        return call_num(0)
    def call_1():
        user_choice = input_num[0]
        dict_num[user_choice][1] = True
        return call_num(1)
    def call_2():
        user_choice = input_num[0]
        dict_num[user_choice][2] = True
        return call_num(2)
    def call_3():
        user_choice = input_num[0]
        dict_num[user_choice][3] = True
        return call_num(3)
    def call_4():
        user_choice = input_num[0]
        dict_num[user_choice][4] = True
        return call_num(4)
    def call_5():
        user_choice = input_num[0]
        dict_num[user_choice][5] = True
        return call_num(5)
    def call_6():
        user_choice = input_num[0]
        dict_num[user_choice][6] = True
        return call_num(6)
    def call_7():
        user_choice = input_num[0]
        dict_num[user_choice][7] = True
        return call_num(7)
    def call_8():
        user_choice = input_num[0]
        dict_num[user_choice][8] = True
        return call_num(8)
    def call_9():
        user_choice = input_num[0]
        dict_num[user_choice][9] = True
        return call_num(9)
    #terminal show numbers and add digits to the list and dict
    def call_num(cl_num: int):
        '''Apply the number in the list!
        \n(input_num: number)'''
        match dict_num[input_num[0]][cl_num]:
            case True:
                number.append(f'{cl_num}')
                numbers.update({input_num[0]:number})
                dict_num[input_num[0]][cl_num] = False
                print(f'''
                number: {number}
                numbers: {numbers}
                dict_num[0]: {dict_num[0]}
                dict_num[1]: {dict_num[1]}
                input_num: {input_num[0]}
                cl_num: {cl_num}
                      ''')
                # status print
                #show_print('c_n')
            case False:
                return print('number is false!')
    
    #Operations calls
    def call_plus():
        operations['+'] = True
        return call_ope('+')
    def call_subt():
        operations['-'] = True
        return call_ope('-')
    def call_mult():
        operations['*'] = True
        return call_ope('*')
    def call_div():
        operations['/'] = True
        return call_ope('/')
    #terminal show operations and numbs
    def call_ope(cl_ope: str):
        '''Apply a operation sign in the list!
        \n(input_ope: [str])'''
        match operations[cl_ope]:
            case True:
                list_ky_op = list(operations.keys())
                for operation in range(len(list_ky_op)):
                    if operations[list_ky_op[operation]] == True:
                        input_ope.clear()
                        input_ope.append(list_ky_op[operation])
                        break
                operations[cl_ope] = False
                print(f'''
                number: {number}
                numbers: {numbers}
                dict_num[0]: {dict_num[0]}
                dict_num[1]: {dict_num[1]}
                input_num: {input_num[0]}
                      ''')
                # status print
                #show_print('c_o')
            case False:
                return print('operation is false!')
    #Next number
    def call_next():
        print(f'''
                number: {number}
                numbers: {numbers}
                dict_num[0]: {dict_num[0]}
                dict_num[1]: {dict_num[1]}
                input_num: {input_num[0]}
                      ''')
        if len(number) != 0:
            number.clear()
        match input_num[0]:
            # SELECTED NUM[02]
            case 0:
                input_num.clear()
                input_num.append(1)
            # SELECTED NUM[01]
            case 1:
                input_num.clear()
                input_num.append(0)
        #return show_print('c_nxt')
    
    window = Tk()
    window.focus()
    window.title('Calc')
    window.configure(bg=c_bg)
    window.geometry('195x100')
    window.resizable(width=False,height=False)
    
    #button - comic size botton
    b_CONFIRM = Button(
        window,bg='#38de1f',fg=c_bg,relief='flat',
        height=3,width=17,
        text='CONFIRM',
        command=...
    ).place(x=70,y=0)
    b_nextNum = Button(
        window,bg='#21a0e0',fg=c_bg,relief='flat',
        height=3,width=17,
        text='NEXT NUM',
        command=call_next
    ).place(x=70,y=50)
    
    #button - operations
    b_plus = Button(
        window, bg=c_bg, fg=c_txt, relief='flat',
        text='+',
        command=call_plus
    ).grid(column=1,row=1)
    b_subt = Button(
        window, bg=c_bg, fg=c_txt, relief='flat',
        text='-',
        command=call_subt
    ).grid(column=1,row=2)
    b_mult = Button(
        window, bg=c_bg, fg=c_txt, relief='flat',
        text='*',
        command=call_mult
    ).grid(column=1,row=3)
    b_div = Button(
        window, bg=c_bg, fg=c_txt, relief='flat',
        text='/',
        command=call_div
    ).grid(column=1,row=4)
    
    #button - numbers
    b_0 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='0',
        command=call_0
    ).grid(column=3,row=4)
    b_1 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='1',
        command=call_1
    ).grid(column=2,row=3)
    b_2 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='2',
        command=call_2
    ).grid(column=3,row=3)
    b_3 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='3',
        command=call_3
    ).grid(column=4,row=3)
    b_4 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='4',
        command=call_4
    ).grid(column=2,row=2)
    b_5 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='5',
        command=call_5
    ).grid(column=3,row=2)
    b_6 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='6',
        command=call_6
    ).grid(column=4,row=2)
    b_7 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='7',
        command=call_7
    ).grid(column=2,row=1)
    b_8 = Button(
        window, bg=c_bg, fg=c_txt, relief='flat',text='8',
        command=call_8
    ).grid(column=3,row=1)
    b_9 = Button(
        window,bg=c_bg,fg=c_txt,relief='flat',text='9',
        command=call_9
    ).grid(column=4,row=1)

    number.clear()
    
    window.mainloop()
#Atividade 3 → need to be continue
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
