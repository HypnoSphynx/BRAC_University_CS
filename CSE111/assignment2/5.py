class Pokemon:
    def __init__ (self,name_one,name_two,poke_one,poke_two,rate):
        self.pokemon1_name=name_one
        self.pokemon1_power=poke_one
        self.pokemon2_name=name_two
        self.pokemon2_power=poke_two
        self.damage_rate=rate



team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,
team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,
team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +
team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)

team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70, 9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name,team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name,team_bulb.pokemon2_power)
pika_combined_power = (team_bulb.pokemon1_power +team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', pika_combined_power)