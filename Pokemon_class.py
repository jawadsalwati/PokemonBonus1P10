class Pokemon:

  def __init__(self, name, typ):
    self.name = name
    self.type = typ
    self.CP = 0
    self.stats = [0, 0, 0] ## [attack, defense, stamina] - max 15
    self.IV = 0

  def get_name(self):
    return self.name

  def get_type(self):
    return self.type

  def get_CP(self):
    return self.CP

  def get_stats(self):
    return self.stats

  def get_defence(self):
    return self.stats[1]

  def get_stamina(self):
    return self.stats[2] 

  def display_attacks(self):
    for i in range(len(self.combat_attacks)):
      print("Attack:",i+1,self.combat_attacks[i][0],"\t"
      "Attack power:",self.combat_attacks[i][1],"\n\n")
  
  def get_IV(self):
    return self.IV

  def display_details(self):
    print("Name:\t",self.get_name())
    print("Type:\t",self.get_type())
    print("CP:\t",self.get_CP())
    stats = self.get_stats()
    print("Attack:\t",stats[0])
    print("Defense:",stats[1])
    print("Stamina:",stats[2])
    print("IV:\t",round(self.get_IV(),2))
    for i in range(len(self.combat_attacks)):
      print("Attack:",i+1,self.combat_attacks[i][0],"\t"
      "Attack power:",self.combat_attacks[i][1],"\n\n")

  def set_CP(self, value):
    self.CP = value
    return self.CP

  def power_up(self, value):
    self.CP += value
    return self.CP

  def set_stats(self, attack, defense, stamina):
    if attack > 15 or defense > 15 or stamina > 15:
      print("Sorry, values cannot exceed 15.")
    else:
      self.stats = [attack, defense, stamina]
      self.IV = sum(self.stats)/45*100
    return self.IV

  def set_stamina(self,new_stamina):
    self.stats[2] = new_stamina

  def get_combat_attacks(self):
    return self.combat_attacks

  def get_combat_attack(self,index):
    return self.combat_attacks[index]

  def set_attacks(self):
    self.combat_attacks = []
    for i in range(2):
      attack_type=input("Enter Attack "+str(i+1)+": ")
      attack_power = int(input("Attack power: "))
      self.combat_attacks.append([attack_type,attack_power])

##Function made so that it generates stats only for the object that passes through it
  def updated_stats(self,damage_done):
    stats = self.get_stats()
    print("\n\nGood hit! You've done",str(round(damage_done,2)),"damage.",str(self.get_name()),"now has",str(round(stats[2],2)),"stamina")     

    
          
               

