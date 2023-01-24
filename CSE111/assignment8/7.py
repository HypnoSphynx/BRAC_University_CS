class PokemonBasic:

  def __init__(self, name = 'Default', hp = 0, weakness = 'None', type = 'Unknown'):
    self.name = name
    self.hit_point = hp
    self.weakness = weakness
    self.type = type

  def get_type(self):
    return 'Main type: ' + self.type

  def get_move(self):
    return 'Basic move: ' + 'Quick Attack'

  def __str__(self):
    return "Name: " + self.name + ", HP: " + str(self.hit_point) + ", Weakness: " + self.weakness

class PokemonExtra(PokemonBasic):
  def __init__(self,*args):
    super().__init__(args[0],args[1],args[2],args[3])
    if len(args)>4:
      self.secondary=args[4]
      self.other=args[5]
    else:
      self.secondary=None
      self.other=None
    
  def get_type(self):
    if self.secondary==None:
      return super().get_type()
    else:
      return f'{super().get_type()} Secondary type:{self.secondary}'
  def get_move(self):
    if self.other==None:
      return super().get_move()
    else:
      return f"{super().get_move()}\nOther move:{','.join(self.other)}"

      




print('\n------------Basic Info:--------------')
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())

print('\n------------Pokemon 1 Info:-------------')
charmander = PokemonExtra('Charmander', 39, 'Water', 'Fire')
print(charmander)
print(charmander.get_type())
print(charmander.get_move())

print('\n------------Pokemon 2 Info:-------------')
charizard = PokemonExtra('Charizard', 78, 'Water', 'Fire', 'Flying', ('Fire Spin', 'Fire Blaze'))
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
