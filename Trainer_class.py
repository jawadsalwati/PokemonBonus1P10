class Trainer:
  def __init__(self,name):
    self.name = name
    self.pokemon_team = []
    self.pokemon_index = 0

  def add_to_team(self,pokemon):
    self.pokemon_team.append(pokemon)

  def remove_from_team(self):
    fainted_poke=self.pokemon_team.pop(0)
    print("\n\nOh no!",str(fainted_poke.name),"fainted!")

  def display_team(self):
    #Display each pokemon and their stats
    pass