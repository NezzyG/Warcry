from units import Warbands
import random


class Soldier:
    def __init__(self, name, cost, attacks, strength, damage, critical, toughness, health, keyword, alive=True):
        self.name = name
        self.cost = cost  # Armies will generate until they reach 1000 points at which point they will stop
        self.attacks = attacks  # number of dice rolled
        self.strength = strength  # compared to enemy toughness
        self.damage = damage
        self.critical = critical  # if d6 roll is 6 it deals a critical amount of damage
        self.toughness = toughness
        self.health = health
        self.keyword = keyword  # To determine it's race
        self.alive = alive

    def war(self,enemy_army):
     pass
    # call in armies of both player(should I call in the entire player
    # or just the army?) im only using one element from player
    # shuffle army lists
    # randomly decide which player attacks first
    # Each player takes turn attacking a
    # random unit(Similar to hearthstone battlegrounds combat)
    # plays out until one army is completely vanquished
    # when dead, alive attribute is changed to false
    # I need to update win/losses too
    # when it's over, before exiting I should set all units to alive

    def attack(self, enemy_unit):
        hits = 0
        critical_hits = 0
        for f in range(self.attacks):
            roll = random.randrange(1, 7)
            if roll == 6:
                critical_hits = critical_hits + 1
            elif (roll == 5) or\
                 (roll == 4 and (self.strength == enemy_unit.toughness or self.strength>enemy_unit.toughness)) or \
                 (roll == 3 and (self.strength > enemy_unit.toughness)):
                hits = hits+1

        print(f"critical hits :  {critical_hits} \n hits: {hits}")
        enemy_unit.health = enemy_unit.health-(self.damage * hits + self.critical * critical_hits)


def get_army(race):
    army_value = 0
    army_list = {}
    key = 0
# the following for iteration looks attempts multiple times to find a
# better fit should the total go over 1000,
# the key variable is here to make sure  there is no key error
# ( using f would create breaks if the iterator found better fits)
# E.G. :{key 0, 1, 2 ,3, 6, 9} and would generate errors.
# Using while might have been smarter so I have more control over the iterator
    for f in range(20):
        army_list[key] = get_random_soldier(race)
        army_value = army_value + army_list[key].cost
        if army_value >= 1000:
            army_value = army_value-army_list[key].cost
            army_list.popitem()
            key = key-1
        key = key+1

    print(army_value)
    return army_list


def get_random_soldier(race):
    imported_unit = random.choice(Warbands[race])
    object_unit = Soldier(imported_unit["name"],
                          imported_unit["cost"],
                          imported_unit["attacks"],
                          imported_unit["strength"],
                          imported_unit["damage"],
                          imported_unit["critical"],
                          imported_unit["toughness"],
                          imported_unit["health"],
                          imported_unit["keyword"])
    return object_unit



