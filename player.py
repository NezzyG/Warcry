from soldier import get_army
from player_data import get_name, get_nickname, get_random_race
from itertools import zip_longest

import random


class Player:

    def __init__(self, name, nickname, army, wins=0, losses=0,
                 disqualified=False,):
        self.name = name
        self.nickname = nickname
        self.wins = wins
        self.losses = losses
        self.army = army  # Army
        self.dummy_army = army #For now this is similar to health/current health to make resetting post combat easier
        self.disqualified = disqualified

    def war(self, enemy_player):

        print(self.army_alive())
        random.shuffle(self.army)
        random.shuffle(enemy_player.army)
        print(self.army_alive())

        while self.army_alive and enemy_player.army_alive :
            for unit1, unit2 in zip_longest(self.army, enemy_player.army,
                                            fillvalue=None):
                if unit1 is not None:
                    target = random.choice(enemy_player.army)
                    unit1.attack(target)
                    if not target.alive:
                        enemy_player.remove(target)

                if unit2 is not None:
                    target = random.choice(self.army)
                    unit2.attack(target)
                    if not target.alive:
                        self.army.remove(target)
            #if troop dies it somehow loops back to max health, need to figure it out.
            #idea to remove units from combat log and create a dummy army list similar to health and current health

    def army_alive(self):
        return any(unit.alive for unit in self.army)

    def reset_army(self):
        for unit in self.army:
            unit.current_health = unit.health
            unit.alive = True

    def set_result(self, winner, loser):
        winner.wins += 1
        loser.losses += 1


def player_profile():
    # Generates player objects by randomizing names,starting them at the
    # default0 wins/losses and picks a random race for them
    race = get_random_race()
    army = get_army(race)
    p1 = Player(
        name=get_name(),
        nickname=get_nickname(),
        army=army
        )
    return p1


player = player_profile()
player2 = player_profile()
print(player.name)
print(player2.name)
player.war(player2)