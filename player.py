from soldier import get_army
from player_data import get_name,get_nickname,get_random_race


class Player:

    def __init__(self, name, nickname, army, wins=0, losses=0, disqualified=False):
        self.name = name
        self.nickname = nickname
        self.wins = wins
        self.losses = losses
        self.army = army  # Army
        self.disqualified = disqualified


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


