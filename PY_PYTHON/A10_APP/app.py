# Cadastro de bancos dps

#Import
from tkinter import *
from tkinter import Tk, ttk, messagebox, Checkbutton, IntVar
from cores import *

#NOSSA JANELA
janela = Tk()
janela.focus()
janela.geometry('310x300')
janela.configure(bg=cor1)
janela.title('Bem - Vindo')
janela.resizable(width=False,height=False)

#Dividindo a janela
frame_cima = Frame(
    janela,
    width=310,
    height=50,
    bg=cor1,
    relief='flat'
)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(
    janela,
    width=310,
    height=250,
    bg=cor1,
    relief='flat'
)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#COLOCANDO ELEMENTOS NO FRAME DE CIMA
l_nome = Label(
    frame_cima,
    text='LOGIN',
    font=('Ivy 25'),
    bg=cor1,
    fg=cor4
)
l_nome.place(x=5,y=5)

l_linha = Label(
    frame_cima,
    text="",
    width=275,
    font=('Ivy 25'),
    bg=cor2,
    fg=cor4
)
l_linha.place(x=10, y=45)

#Colocando elementos no frame de baixo
l_usuario = Label(
    frame_baixo,
    text="Usuário *",
    font=('Ivy 14'),
    bg=cor1,
    fg=cor4
)
l_usuario.place(x=10,y=20)

e_nome = Entry(
    frame_baixo,
    width=25,
    justify="left",
    font=("",15),
    highlightthickness=1,
    relief='solid'
)
e_nome.place(x=14,y=50)

l_senha = Label(
    frame_baixo,
    text="Senha *",
    font=('Ivy 14'),
    bg=cor1,
    fg=cor4
)
l_senha.place(x=10,y=95)

e_senha = Entry(
    frame_baixo,
    show='*',
    width=25,
    justify='left',
    font=('',15),
    highlightthickness=1,
    relief='solid'
)
e_senha.place(x=14,y=130)

def cadastrar_usuario():
    nome_digitado = e_nome.get()
    senha_digitado = e_senha.get()
    
    if nome_digitado in credenciais.keys():
        messagebox.showerror(title="ERRO!",message="Usuário já cadastrado.")
    else:
        messagebox.showinfo(title='Bem vindo!',message="Cadastrado com sucesso.")
        credenciais[nome_digitado] = senha_digitado
        with open('credenciais.txt','w') as file:
            file.write(f'{credenciais}')
        
b_cadastrar = Button(
    frame_baixo,
    text='CADASTRAR',
    width=39,
    height=2,
    font=('Ivy 8 bold'),
    bg=cor2,
    fg=cor1,
    relief='raised',
    command=cadastrar_usuario
)
b_cadastrar.place(x=15,y=165)

def checar_usuario():
    nome_digitado = e_nome.get()
    senha_digitado = e_senha.get()
    
    if nome_digitado in credenciais.keys():
        senha_armazenada = credenciais[nome_digitado]
        if senha_digitado == senha_armazenada:
            messagebox.showinfo(title="Bem vindo!",message="Logado com sucesso.")
        else:
            messagebox.showerror(title="ERRO!",message="Usuário ou senha inválidos.")
    else:
        messagebox.showerror(title="ERRO!",message="Usuário ou senha inválidos.")

b_logar = Button(
    frame_baixo,
    text='LOGAR',
    width=39,
    height=2,
    font=('Ivy 8 bold'),
    bg=cor2,
    fg=cor1,
    relief='raised',
    command=checar_usuario
)
b_logar.place(x=15,y=204)

credenciais = {"admin":"0000"}

if __name__ == "__main__":
    janela.mainloop()