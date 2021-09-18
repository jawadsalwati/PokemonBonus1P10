from Pokemon_class import*
from Trainer_class import*
import time
import random

## Just made a rough function to help create user's pokemon as an object. Extra functions help allow users to instantly reenter incorrect attack/def/stamina values 

def make_pokemon(name):
  element = input("Type ")
  name= Pokemon(name,element)
  print("Your pokemon has been created!")
  time.sleep(1.5)
  print("Time to update your pokedex!")
  time.sleep(1.5)
  CP=int(input("Combat Power: "))
  name.set_CP(CP)
  attack=set_attack()
  defense= set_defense()
  stamina= set_stamina()
  name.set_stats(attack, defense, stamina)
  name.set_attacks()
  return name
  
  
def set_attack():
  while True:
      attack= int(input("Attack Value: "))
      if attack<= 15 and attack>0 :
        return attack
        break
      else:
        print("Sorry, values cannot exceed 15. Re-enter values")

def set_defense():
  while True:
    defense= int(input("Defense Value: "))
    if defense<= 15 and defense>0 :
        return defense
        break
    else:
      print("Sorry, values cannot exceed 15. Re-enter values")

def set_stamina():
  while True:
    stamina= int(input("Stamina Value: "))
    if stamina<= 15 and stamina>0 :
      return stamina
      break
    else:
      print("Sorry, values cannot exceed 15. Re-enter values")
    
def display_pokemon(trainer_list):
  for trainer in trainer_list:
    print("\n\n"+trainer.name+"'s Pokemon\n\n")
    for pokemon in trainer.pokemon_team:
      pokemon.display_details()
      print("\n")

def attack_enemy(attacking_pokemon, defending_pokemon,index):
  #Calculating the total damage done
  index -= 1 
  attack_power = attacking_pokemon.get_combat_attack(index)[1]
  combat_power = attacking_pokemon.get_CP()
  luck_factor = random.randrange(80,120,10)

  combined_power = attack_power*combat_power*(luck_factor/100)

  damage_done = combined_power/defending_pokemon.get_defence()
  
  #Adjusting the defending pokemon's Stamina
  current_stamina = defending_pokemon.get_stamina()

  new_stamina = current_stamina - damage_done

  #Setting the pokemon's new stamina
  defending_pokemon.set_stamina(new_stamina)

  #Displaying new Stamina
  defending_pokemon.updated_stats(damage_done)
  
  return new_stamina


  

    

  


def battle_pokemon(trainer_list):
  #Chooses the first trainer to play in battle
  first_trainer = random.randint(0,1)

  order  = []
  if first_trainer == 0:
    order = [0,1]
  else:
    order = [1,0]

  battling = True
  
  
  #Battle loop
  while (battling):
    for i in order:
      dead=[]
      if trainer_list[i].pokemon_team==dead:
        print(str(trainer_list[i].name),"lost the game.",str(trainer_list[i-1].name),"is the winner!")
        battling = False
        break
      elif trainer_list[i-1].pokemon_team==dead:
        print(str(trainer_list[i-1].name),"lost the game.",str(trainer_list[i].name),"is the winner!")
        battling = False
        break

      #Gets the first pokemon in the trainer's team and the first pokemon in the opponent's team
      current_pokemon = trainer_list[i].pokemon_team[0]
      current_opponent = trainer_list[i-1].pokemon_team[0]
      
      print("\n\nPlayer",trainer_list[i].name,"'s turn")
      print("Pokemon :",current_pokemon.name)
      print("Stamina :",round(current_pokemon.get_stamina(),2))
      ##We display all types of attacks
      for a in range(len(current_pokemon.get_combat_attacks())):
            print("\n", str(a+1), "-\tAttack Type", str(current_pokemon.get_combat_attacks()[a][0]),"\t", "Attack power",str(current_pokemon.get_combat_attacks()[a][1]))
      ##User chooses which attack
      choice = input("\n\nChoose attack by entering attack number ")

      try:
        choice = int(choice)
      except:
        print("\nAn error happened when processing your choice - please try again")

      new_stamina=attack_enemy(current_pokemon,current_opponent,choice)

      if new_stamina<=0:
        ##print(str(current_opponent.name),"fainted!!")
        trainer_list[i-1].remove_from_team()
      
      
      

    
      
      

  #use random.randint to decide who goes first - DONE
  #Send out trainer's first pokemon's-DONE
  #who ever won the luck battle gets to go first- DONE
  #Attacks are presented on the screen and press 1,2,3 or 4 to choose an attack- DONE
  #The average of the attack power and the combat power multiplied by a luck factor between 0.8 and 1.2 decides the power of the attack - DONE
  #The attack is subtracted from the other pokemon's stamina - DONE
  
  #If the other pokemon faints then another pokemon is sent out
  #This goes back and forth until one trainer has no pokemon left - in that case they loose and the trainer with pokemon left wins 