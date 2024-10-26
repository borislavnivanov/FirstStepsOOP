from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {Pokemon.pokemon_details(pokemon)}'

    def release_pokemon(self, pokemon_name: str) -> str:
        for el in self.pokemons:
            if el.name == pokemon_name:
                self.pokemons.remove(el)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self) -> str:
        result = [f'Pokemon Trainer {self.name}',
                  f'Pokemon count {len(self.pokemons)}']
        for p in self.pokemons:
            result.append(f'- {p.pokemon_details()}')
        return '\n'.join(result)
