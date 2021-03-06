<<<<<<< HEAD
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if any([x for x in self.pokemons if x.name == pokemon.name]):
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}" + "\n" + f"Pokemon count {len(self.pokemons)}"
        for pokemon in self.pokemons:
            result += "\n"
            result += f"- {pokemon.pokemon_details()}"

        return result
=======
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if any([x for x in self.pokemons if x.name == pokemon.name]):
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}" + "\n" + f"Pokemon count {len(self.pokemons)}"
        for pokemon in self.pokemons:
            result += "\n"
            result += f"- {pokemon.pokemon_details()}"

        return result
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
