class Player:
    def __init__(self, data):
        self.name = data['name']
        self.nationality = data['nationality']
        self.assists = data['assists']
        self.goals = data['goals']
        self.team = data['team']
        #self.games = dict['games']
        #elf.id = dict['id']

    def __str__(self):
        #return f"{self.name:20}"
        return f"""{self.name:20} from {self.nationality}
                    playing in {self.team:20} goals: {self.goals}
                    assists: {self.assists} = {self.assists + self.goals}"""

    @property
    def nimi(self):
        return f"{self.name:20}"

    @property
    def tiimi_ja_maa(self):
        return f"from {self.nationality} playing in {self.team:20}"

    @property
    def statsit(self):
        return f"goals: {self.goals} assists: {self.assists} = {self.assists + self.goals}"
