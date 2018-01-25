from Buildings import Enums as BuildingEnums


class Unlock:
    def __init__(self, building, count, reward_mod):
        self.building = building
        self.count = count
        self.reward_modifier = reward_mod


def generate_unlocks():
    unlocks = []

    for u in UNLOCK_VALUES:
        unlocks.append(Unlock(*u))

    return unlocks


# Building      count_required      reward_modifier
UNLOCK_VALUES = (
    (BuildingEnums.LEMON, 10, 2),
    (BuildingEnums.NEWSPAPER, 10, 2),
    (BuildingEnums.CARWASH, 10, 2),
    (BuildingEnums.PIZZA, 10, 2),
    (BuildingEnums.SHRIMP, 10, 2),
    (BuildingEnums.HOCKEY, 10, 2),
    (BuildingEnums.MOVIE, 10, 2),
    (BuildingEnums.BANK, 10, 2),
    (BuildingEnums.OIL, 10, 2),
    (BuildingEnums.ALL, 10, 2),

    (BuildingEnums.LEMON, 25, 2),
    (BuildingEnums.NEWSPAPER, 25, 2),
    (BuildingEnums.CARWASH, 25, 2),
    (BuildingEnums.PIZZA, 25, 2),
    (BuildingEnums.SHRIMP, 25, 2),
    (BuildingEnums.HOCKEY, 25, 2),
    (BuildingEnums.MOVIE, 25, 2),
    (BuildingEnums.BANK, 25, 2),
    (BuildingEnums.OIL, 25, 2),
    (BuildingEnums.ALL, 25, 2),
)
