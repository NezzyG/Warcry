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

    @property
    def army_alive(self):
        return any(unit.alive for unit in self.army)
    
    def war(self, enemy_player):

        random.shuffle(self.army)
        random.shuffle(enemy_player.army)

        while self.army_alive and enemy_player.army_alive:
            for unit1, unit2 in zip_longest(self.army, enemy_player.army,
                                            fillvalue=None):

                if unit1 is not None and unit1.alive:
                    target = random.choice(enemy_player.army)
                    while not target.alive and enemy_player.army_alive:
                        target = random.choice(enemy_player.army)
                    unit1.attack(target)

                if unit2 is not None and unit2.alive:
                    target = random.choice(self.army)
                    while not target.alive and self.army_alive:
                        target = random.choice(self.army)

                    unit2.attack(target)

        if self.army_alive:
            print(f"{self.name} wins")
            return True
        else:
            print(f"{enemy_player.name} wins")
            return False
    
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