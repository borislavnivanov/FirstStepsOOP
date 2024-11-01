class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild: str = 'Unaffiliated'

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self) -> str:
        formated_string = [f'Name: {self.name}',
                           F'Guild: {self.guild}',
                           F'HP: {self.hp}',
                           F'MP: {self.mp}']
        for skill, mana in self.skills.items():
            formated_string.append(f'==={skill} - {mana}')
        return '\n'.join(formated_string) + '\n'