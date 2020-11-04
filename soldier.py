from units import Warbands
import random
from player_data import get_random_race


class Soldier:
    def __init__(self, name, cost, attacks, strength, damage, critical, toughness, health, keyword, alive=True):
        self.name = name
        self.cost = cost  # Armies will generate until they reach 1000 points at which point they will stop
        self.attacks = attacks  # number of dice rolled
        self.strength = strength  # compared to enemy toughness
        self.damage = damage
        self.critical = critical  # during the attack function, if a 6 is generated it will result in a critical hit
        self.toughness = toughness
        self.health = health
        self.current_health = health
        self.keyword = keyword  # To determine it's race
        self.alive = alive

    def attack(self, enemy_unit):
        print(f"{self.name} {self.current_health} attacks {enemy_unit.name} "
              f"{enemy_unit.current_health}")
        hits = 0
        critical_hits = 0
        for f in range(self.attacks):
            roll = random.randrange(1, 7)
            if roll == 6:
                critical_hits = critical_hits + 1
            elif (roll == 5) or\
                 (roll == 4 and (self.strength == enemy_unit.toughness or
                                 self.strength > enemy_unit.toughness)) or \
                 (roll == 3 and (self.strength > enemy_unit.toughness)):
                hits = hits+1

        print(f"critical hits :  {critical_hits} \n hits: {hits}")

        enemy_unit.current_health = enemy_unit.health-(self.damage * hits +
                                                       self.critical *
                                                       critical_hits)

        print(f"{enemy_unit.name} now has {enemy_unit.current_health} health")
        if enemy_unit.current_health <= 0:
            enemy_unit.alive = False


def get_army(race):
    army_value = 0
    army = []
    for i in range(20):
        unit = get_random_soldier(race)
        if army_value + unit.cost > 1000:
            continue
        if army_value == 1000:
            break
        if len(army) == 15:
            break
        elif len(army) > 15:
            army = army[:15]
        army.append(unit)
        army_value += unit.cost

    return army


def get_random_soldier(race):
    imported_unit = random.choice(Warbands[race])
    object_unit = Soldier(**imported_unit)
    return object_unit


