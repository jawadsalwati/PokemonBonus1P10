#Authors: Muhammad Jawad, Dorian Knight
#MacID: jawadm1, knighd7
#Student# 400330872 ,400304437

import time
from Pokemon_class import*
from Trainer_class import*
from Game_logic import*




  
##Example main
def main():
  #Two trainers build their teams
  trainer_list = []
  for j in range(1,3):
    #initializing the trainer and number of pokemon on their team
    trainer_name = input("\nTrainer "+str(j)+" name: ")
    trainer = Trainer(trainer_name)
    trainer_list.append(trainer)
    num=int(input(trainer_name +", How many pokemon would you like to create? "))
    while (num>3 or num<1):
      print("\n\nYou can only have between 1 and 3 pokemon - please enter in a valid number")
      num=int(input(trainer_name +", How many pokemon would you like to create? "))
    
    #Creating the pokemon
    for i in range(num):
      print("\n\nTime to create a new Pokemon!")
      name = input("Pokemon name ")
      pokemon = make_pokemon(name)
      
      trainer.add_to_team(pokemon)
    
  #Main Menu
  playing = True

  while(playing):
    print("\n1 - Display Pokemon \n2 - Battle Pokemon \n3 - Quit")
    choice = input()

    try:
      choice = int(choice)
    except:
      print("\nAn error happened when processing your choice - please try again")

    if choice == 1:
      #Display Pokemon
      display_pokemon(trainer_list)

    elif choice == 2:
      #Battle Pokemon
      battle_pokemon(trainer_list)
      
    elif choice == 3:
      #quit
      print("Thank you for playing")
      playing = False

    else:
      print("\nYour choice not on the list - please try again")

