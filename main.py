import random
from pprint import pprint
from player import player_profile
from player import Player


# REMEMBER TO USE PDB


class Tournament:

    def __init__(self):
        self.participants = []
        self.defeated = []
        self.player_limit = 8
        self.init()

    def init(self):
        # Uses a function from player.py to generate player profiles and adds
        # them to a list of participants
        self.participants = []
        for n in range(self.player_limit):
            p = player_profile()
            self.participants.append(p)
            print(p.name, p.nickname)
            for unit in p.army:
                pprint(unit.name)
                # dir(name of variable)

        return self.participants


    def tournament_standing(self, remaining):
        # will be part of the class as the project evolves,implement later
        # Will shuffle the list of players and then pit the first user vs the
        # second, third vs fourth and so on
        # Must make sure it displays tournament standing graphics
        # Might move into a second file to clean up
        random.shuffle(remaining)
        for f in range(0, len(remaining), 2):
            print(remaining[f].name + " VS " + remaining[f + 1].name)


tournament = Tournament()
print(tournament.participants)
for participants in tournament.participants:
    pprint(participants.name)