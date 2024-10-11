class Team():
    def __init__(self,name,team_size, capital):
        self.name=name
        self.team_size=team_size
        self.capital=capital
    def show_info(self):
        print(f'Team name: {self.name}, team size: {self.team_size}, capital: {self.capital}')
