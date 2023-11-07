# IMPORT
from os import system
import random

def game_win_stats(player_choice: str,comp_choice: str) -> list[bool]:
  '''Define quem ganha e retorn uma lista
  \n sendo respectivamente [ 'jogador' , 'empate , 'computador' ]'''
  player_win,comp_win,both_win = False,False,False
  if player_choice.lower() == 'pedra' and comp_choice == 'papel':
    comp_win = True
  elif player_choice.lower() == 'papel' and comp_choice == 'tesoura':
    comp_win = True
  elif player_choice.lower() == 'tesoura' and comp_choice == 'pedra':
    comp_win = True
  elif player_choice.lower() == comp_choice:
    both_win = True
  else:
    player_win = True
  return [player_win,both_win,comp_win]

lop = True
game_stats,player_score,comp_score = True,0,0
while game_stats is True:
  compChoice = random.choice(['pedra','papel','tesoura'])
  if lop == True:
    nameAsk = input("Bem vindo ao jogo pedra, papel e tesoura!\nDigite seu nome!\n-> ")
  while True:
    playerChoice = input("""
  Escolha entre:
a) Pedra
b) Papel
c) Tesoura
  -> """)
    match playerChoice:
      case 'a':
        playerChoice = 'pedra'
      case 'b':
        playerChoice = 'papel'
      case 'c':
        playerChoice = 'tesoura'
    if playerChoice.lower() != 'pedra' and playerChoice.lower() != 'papel' and playerChoice.lower() != 'tesoura':
      system('cls')
      print('você digitou algo errado!\ntente novamente!\n')
    else:
      break
  # who won?
  gameWin = game_win_stats(playerChoice.lower(),compChoice)
  if gameWin[0] is True:      # JOGADOR GANHOU!
    player_score+=1
    gameContinue = input(f"""
    {nameAsk} ganhou!
    computador escolheu {compChoice}        
    {nameAsk}:{player_score} | computador:{comp_score}
  
    Deseja continuar?
      (sim) (não)
  -> """)
  elif gameWin[2] is True:    # O COMPUTADOR GANHOU!
    comp_score+=1
    gameContinue = input(f"""
    O computador ganhou!
    computador escolheu {compChoice}
    {nameAsk}:{player_score} | computador:{comp_score}

    Deseja continuar?
      (sim) (não)
  -> """)
  else:             # EMPATE!
    gameContinue = input(f"""
    Empate!
    {nameAsk} e o computador escolheram {compChoice}    
    {nameAsk}:{player_score} | computador:{comp_score}

    Deseja continuar?
      (sim) (não)
  -> """)
  # Continue?
  if gameContinue == 's' or gameContinue == 'sim':
    lop = False
  else:
    system('cls')
    print("jogo finalizado!")
    break
      