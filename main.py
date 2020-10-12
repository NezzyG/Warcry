import random

from pprint import pprint
from player import player_profile


# REMEMBER TO USE PDB


class Tournament:

    def __init__(self):
        self.participants = []
        self.defeated = []
        self.init()

    def init(self):

        # Uses a function from player.py to generate player profiles and adds
        # them to a list of participants

        part = []
        for f in range(8):
            p = player_profile()
            part.append(p)
            print(p.name, p.nickname)
            for x in range(len(p.army)):
                # find a better formula
                pprint(p.army[x].name)
                # dir(name of variable)
        self.participants = part

        return part

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
# this is a test to make sure combat works
print(f"{tournament.participants[1].name}'s {tournament.participants[1].army[0].name} hits {tournament.participants[0].name} {tournament.participants[0].army[0].name}")
print(f"{tournament.participants[0].army[0].name}, Unit health before combat: {tournament.participants[0].army[0].health}")
tournament.participants[1].army[0].attack(tournament.participants[0].army[0])
print(f"{tournament.participants[0].army[0].name}'s health after combat: {tournament.participants[0].army[0].health}")
