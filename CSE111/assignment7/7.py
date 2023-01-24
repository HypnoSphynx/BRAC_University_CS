class Football:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(Football):
  def __init__(self,team_name,name,role,goal,match):
    super().__init__(team_name,name,role)
    self.goal=goal
    self.match=match
    self.goal_ratio=0

  def calculate_ratio(self):
    self.goal_ratio=self.goal/self.match
    self.earning_per_match=(self.goal*1000)+(self.match*10)
  
  def print_details(self):
    self.earning_per_match=(self.goal*1000)+(self.match*10)
    print(super().get_name_team())
    print(f'Total role:{self.role}')
    print(f'Total goal: {self.goal} Total played:{self.match}')
    print(f'Goal Ratio: {self.goal_ratio}')
    print(f'Match Earning: {self.earning_per_match}K')

class Manager(Football):
  def __init__(self,team_name,name,role,match):
    super().__init__(team_name,name,role)
    self.match=match


  def print_details(self):
    self.earning_per_match=self.match*1000
    print(super().get_name_team())
    print(f'Total role:{self.role}')
    print(f'Win:{self.match}')
    print(f'Match Earning: {self.earning_per_match}K')


player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()
