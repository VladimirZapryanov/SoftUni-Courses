<<<<<<< HEAD
class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game not in self.games:
            return f"{game} is not in library"
        else:
            self.played_hours += hours
            return f"{self.username} is playing {game}"

    def buy_game(self, game):
        if game in self.games:
            return f"{game} is already in your library"
        else:
            self.games.append(game)
            return f"{self.username} bought {game}"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


"""
some test:
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
"""
=======
class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game not in self.games:
            return f"{game} is not in library"
        else:
            self.played_hours += hours
            return f"{self.username} is playing {game}"

    def buy_game(self, game):
        if game in self.games:
            return f"{game} is already in your library"
        else:
            self.games.append(game)
            return f"{self.username} bought {game}"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


"""
some test:
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
"""
>>>>>>> a9fb39ed429e8e67941dee3c7a2ba2d6982bf8b8
