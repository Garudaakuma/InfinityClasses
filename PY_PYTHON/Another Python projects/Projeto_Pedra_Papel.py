'''
Projeto: Pedra, papel e tesoura

Feito por Lucas Aioria Serpa
Turma: 713
'''

# IMPORT
from os import system
import random

# TRANSFORMANDO LISTA EM STRING
def player_choice(user_arry: list[bool]) -> str:
    for i in range(len(user_arry)):
        if i == 0 and user_arry[i] is True:
            user_cho = 'pedra'
        elif i == 1 and user_arry[i] == True:
            user_cho = 'papel'
        elif i == 2 and user_arry[i] == True:
            user_cho = 'tesoura'
    return user_cho

# DEFINIÇÃO DA REGRA
def game_rules(user_cho: str,comp_cho: str) -> list[bool]:
    '''Recebe a escolha do computador e do usuario!
    \n retorna uma lista onde [user, iguais, computador]'''
    win_comp,win_user,draw_game = False,False,False
    if user_cho == 'pedra' and comp_cho == 'papel':
        win_comp = True
    elif user_cho == 'papel' and comp_cho == 'tesoura':
        win_comp = True
    elif user_cho == 'tesoura' and comp_cho == 'pedra':
        win_comp = True
    elif user_cho == comp_cho:
        draw_game = True
    else:
        win_user = True
    return [win_user,draw_game,win_comp]

# Menu de escolhas
def rock_menu(choice:int) -> list[bool]:
    # Verifica se a resposta do usuario digitada está corretamente.
    choice_agreed = lambda ch_yes=str: True if ch_yes.lower() == 's' or ch_yes.lower() == 'sim' else False
    pedra = False
    if choice == 0:     # CHOICE SELECTOR [0]
            player_choice = input("""
    [ Deseja escolher PEDRA? ]
           (sim)  (não)
        _______
-------'   ____)
        (_______)
        (________)
        (_______)
-------.__(___)

                -> """)
            # Rock check
            if choice_agreed(player_choice) is True: # ROCK CHECKED
                system('cls')
                print("""
        [ PEDRA SELECIONADA!!! ]
        _______
-------'   ____)
        (_______)
        (________)
        (_______)
-------.__(___)
                            """)
                pedra = True
            else:
                choice+=1
    return [pedra,choice]

def paper_menu(choice:int) -> list[bool]:
    # Verifica se a resposta do usuario digitada está corretamente.
    choice_agreed = lambda ch_yes=str: True if ch_yes.lower() == 's' or ch_yes.lower() == 'sim' else False
    papel = False
    if choice == 1:     # CHOICE SELECTOR [1]
            player_choice = input("""
    [ Deseja escolher PAPEL? ]
        (sim)  (não)
        _______
-------'    ____)____
            _________)
            ___________)
            __________)
-------.__________)
                                    
                -> """)
            # Paper check
            if choice_agreed(player_choice) is True: # PAPER CHECKED
                system('cls')
                print("""
        [ PAPEL SELECIONADA!!! ]
        _______
-------'    ____)____
            _________)
            ___________)
            __________)
-------.__________)
                            """)
                papel = True
            else:
                choice+=1
    return [papel,choice]

def scissors_menu(choice:int) -> list[bool]:
    # Verifica se a resposta do usuario digitada está corretamente.
    choice_agreed = lambda ch_yes=str: True if ch_yes.lower() == 's' or ch_yes.lower() == 'sim' else False
    tesoura = False
    if choice == 2:     # CHOICE SELECTOR [2]
            player_choice = input("""
    [ Deseja escolher TESOURA? ]
        (sim)  (não)
        _______
-------'   ____)____
            ________)
        ______________)
        (______)
-------.__(___)

                -> """)
            # Scissors check
            if choice_agreed(player_choice) == True: # SCISSORS CHECKED
                system('cls')
                print("""
        [ TESOURA SELECIONADA!!! ]
        _______
-------'   ____)____
            ________)
        ______________)
        (______)
-------.__(___)
                            """)
                tesoura = True
            else:
                choice = 0
    return [tesoura,choice]
    
def player_choice_event(event:bool) -> list[bool]:
    '''Evento onde o jogador escolhe entre
    \n Pedra, Papel e tesoura respectivamente'''
    pedra,papel,tesoura = False,False,False
    choice = 0
    # Menu de escolhas! 
    while event is True:
        # Rock
        rock_menu_get = rock_menu(choice)
        pedra,choice = rock_menu_get[0],rock_menu_get[1]
        # Paper
        paper_menu_get = paper_menu(choice)
        papel,choice = paper_menu_get[0],paper_menu_get[1]
        # Scissors
        scissors_menu_get = scissors_menu(choice)
        tesoura,choice = scissors_menu_get[0],scissors_menu_get[1]
        # Menu break check
        if pedra or papel or tesoura:
            break
    return [pedra,papel,tesoura]

lop = True
playerScore,CompScore = 0,0
gameStats,nameUser = True,''
# Inicio
while gameStats is True:
    system('cls')
    compChoice = random.choice(['pedra','papel','tesoura'])
    if lop is True:
        nameUser = input(
        """
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣤⠞⠋⠈⣷⠶⠶⠶⠶⣤⣤⣄⣀⣀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣧⣤⣤⠤⣼⣷⣤⣄⣀⢿⠛⠛⠿⢿⣿⣷⣦⣤⡀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⢀⡿⢸⡆⠀⠀⠀⣿⣿⣿⣿⣿⣷⣦⡀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠀⠀⠀⣀⣀⣀⣀⣠⠞⠁⢸⡇⠀⠀⠀⡇⠈⠙⠻⣿⣿⣿⣿⣦⡀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⠀⠀⠀⢻⡏⠉⠉⣧⠀⠀⢸⡇⠀⠀⢰⡇⠀⠀⡀⠘⣿⣿⣿⣿⣿⣦
                                    ⠀⠀⠀⠀⣠⡾⢷⣄⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣟⣛⡻⠶⢤⣼⠿⣤⣄⣸⣇⠀⢠⡇⠀⢸⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⣠⢤⣄
                                    ⠀⣰⠶⢶⣏⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠘⠋⠉⠉⠛⢶⣤⡀⠀⠉⠉⠙⠓⠾⠁⠀⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⢀⡼⠋⠀⠉⣷
                                    ⢸⡏⠀⠀⠈⠳⣄⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠦⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠟⠁⠀ ⢠⡾⠃
                                    ⠈⢻⣦⡀⠀⠀⠈⠳⣦⡀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀ ⣴⠏
                                    ⣴⠏⠈⠻⣦⡀⠀⠀⠈⠻⣦⡀⠀⠀⠙⢿⣿⡟⠛⠛⠛⠷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣠⡞⠁
                                    ⠻⣄⠀⠀⠈⠻⣦⡀⠀⠀⠈⠻⠆⠀⠀⠀⠙⠳⣄⡀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⢀⣾⡏⠀⠀⢀⣀⣠⠤⠴⠖⠚⣆
                                    ⠀⢩⡷⣤⡀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠆⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⢠⡿⠉⠉⠙⠻⢿⣿⠛⠋⠁⠀⠀⠀⢰⣿⡿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀ ⢸
                                    ⠀⣿⡄⠈⠛⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⣴⠋⠀⠀⠀⠀⢰⡄⠈⠙⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡤⠤⠖⠚⠛⠛⠋
                                    ⠀⠈⠻⢦⣄⠀⠙⠷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⡾⠁⠀⠀⠀⠀⠀⢸⠿⢦⡄⠀⠀⣇⣀⣠⣤⢤⣴⠖⠛⠋⠉⠁
                                    ⠀⠀⠀⠀⠙⢷⣄⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⣇⠀⠀⠀⠀⠀⠀⡼⠀⠸⡇⠀⢸⠃⠀⠀⠀⠀⡏
                                    ⠀⠀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠀⢻⡄⠀⠀⠀⠀⣼⠁⢀⡟⠛⠦⠾⠤⠤⠤⢤⡴⠏
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⢳⣄⢀⣼⠏⠀⠀⠀⠀⠀⠀⠸⠷⠤⢤⣄⣀⠀⠀⢸⡇
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠙⢿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⡵⠟⠁
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣶⣦⣤⠶⠞⠛⠉⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⢀⣤⣤⣤⣤⣤⣤⣶⡾⠋
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠋
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠿⠛⠁
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⢷⣶⣤⣤⣤⣤⣴⣶⣾⣿⡿⠟⠛⠉
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉
        ██▄ ███ █▄ ▄█    █▄█ ███ █  █ ██▄ ███    ███ ███    ███ ███ ██▄ ███ ███     ███ ███ ███ ███ █      ███    ███ ███ ███ ███ █ █ ███ ███
        █▄█ █▄  █ █ █    ███  █  ██▄█ █ █ █ █    █▄█ █ █    █▄█ █▄  █ █ █▄  █▄█     █▄█ █▄█ █▄█ █▄  █      █▄      █  █▄  █▄▄ █ █ █ █ █▄  █▄█
        █▄█ █▄▄ █   █     █  ▄█▄ █ ██ ███ █▄█    █ █ █▄█    █   █▄▄ ███ █ █ █ █,    █   █ █ █   █▄▄ █▄█    █▄▄     █  █▄▄ ▄▄█ █▄█ ███ █ █ █ █

                Digite seu [USERNAME]!
                    -> """)
    system('cls')
    winArry = game_rules(player_choice(player_choice_event(True)),compChoice)
# WIN CHECK
    while True:
        if winArry[0] == True:      # Jogador ganhou !
            playerScore+=10
            gameRule_ask = input(f"""
    {nameUser} ganhou!
    computador escolheu {compChoice}        
    {nameUser}:{playerScore} | computador:{CompScore}
  
    Deseja continuar?
      (sim) (não)
  -> """)
        elif winArry[1] == True:    # Empate !
            gameRule_ask = input(f"""
    Empate!
    computador escolheu {compChoice}        
    {nameUser}:{playerScore} | computador:{CompScore}
  
    Deseja continuar?
      (sim) (não)
  -> """)
        elif winArry[2] == True:    # Computador ganhou !
            CompScore+=10
            gameRule_ask = input(f"""
    O computador ganhou!
    computador escolheu {compChoice}        
    {nameUser}:{playerScore} | computador:{CompScore}
  
    Deseja continuar?
      (sim) (não)
  -> """)
    # Game loop Check
        if gameRule_ask.lower() == 'sim' or gameRule_ask.lower() == 's':
            lop = False
            system('cls')
            break
        elif gameRule_ask.lower() == 'não' or gameRule_ask.lower() == 'n':
            gameStats = False
            system('cls')
            print(f'{nameUser}:{playerScore} | computador:{CompScore}\nJogo finalizado!')
            break
        else:
            system('cls')
            print(f"\n{nameUser} digitou algo de errado!\nTente novamente!\n")