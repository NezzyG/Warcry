import random

from pprint import pprint
from player import player_profile

# REMEMBER TO USE PDB


class Tournament:
    def __init__(self):
        self.participants = []
        self.defeated = []
        self.tournament_players = 8
        self.init()

    def init(self):
        # Uses a function from player.py to generate player profiles and adds
        # them to a list of participants
        part = []
        for n in range(self.tournament_players):
            p = player_profile()
            part.append(p)
            print(p.name, p.nickname)
            for unit in p.army:
                pprint(unit.name)          
                # dir(name of variable)
        self.participants = part

    def tournament_standing(self):
        # will be part of the class as the project evolves,implement later
        # Will shuffle the list of players and then pit the first user vs the
        # second, third vs fourth and so on
        # Must make sure it displays tournament standing graphics
        # Might move into a second file to clean up

        random.shuffle(self.participants)
        while len(self.participants) > 1:
            losers = []
            for i in range(0, len(self.participants), 2):

                p1, p2 = self.participants[i], self.participants[i + 1]
                print(p1.name + " VS " + p2.name)
                winner_check = p1.war(p2)
                # if winner_check returns True, p1 won if false p2 won
                if winner_check:
                    losers.append(p2)
                else:
                    losers.append(p1)
            for players in losers:
                self.participants.remove(players)
        print(f"{self.participants[0].name} has won the tournament!")


tournament = Tournament()
tournament.tournament_standing()
# this is a test to make sure combat works
"""tournament.participants[0].war(tournament.participants[1])"""
