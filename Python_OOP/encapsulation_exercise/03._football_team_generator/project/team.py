<<<<<<< HEAD
from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for team_player in self.__players:
            if player.name == team_player.name:
                return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player

        return f"Player {player_name} not found"
=======
from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for team_player in self.__players:
            if player.name == team_player.name:
                return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player.name == player_name:
                self.__players.remove(player)
                return player

        return f"Player {player_name} not found"
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
