from Buildings import Enums as BuildingEnums


class Upgrade:
    def __init__(self, building, upgrade_type, cost=0, modifier=1):
        self.upgrade_type = upgrade_type
        self.building = building
        self.cost = cost
        self.modifier = modifier

    def __str__(self):
        return "Building: {:10}, Modifier: {}, Type: {}, Cost: {}".format(self.building, self.modifier,
                                                                          self.upgrade_type, self.cost)

    def __repr__(self):
        return str(self)


class Enums:
    TYPE_COST_MODIFIER = "cost_modifier"
    TYPE_REWARD_MODIFIER = "reward_modifier"


# building      reward_type     cost        modifier
UPGRADE_VALUES = (
    (BuildingEnums.LEMON, Enums.TYPE_REWARD_MODIFIER, 250000, 3),
    (BuildingEnums.NEWSPAPER, Enums.TYPE_REWARD_MODIFIER, 500000, 3),
    (BuildingEnums.CARWASH, Enums.TYPE_REWARD_MODIFIER, 10 ** 6, 3),
    (BuildingEnums.PIZZA, Enums.TYPE_REWARD_MODIFIER, 5 * 10 ** 6, 3),
    (BuildingEnums.DONUT, Enums.TYPE_REWARD_MODIFIER, 10 * 10 ** 6, 3),
    (BuildingEnums.SHRIMP, Enums.TYPE_REWARD_MODIFIER, 25 * 10 ** 6, 3),
    (BuildingEnums.HOCKEY, Enums.TYPE_REWARD_MODIFIER, 500 * 10 ** 6, 3),
    (BuildingEnums.MOVIE, Enums.TYPE_REWARD_MODIFIER, 10 * 10 ** 9, 3),
    (BuildingEnums.BANK, Enums.TYPE_REWARD_MODIFIER, 50 * 10 ** 9, 3),
    (BuildingEnums.OIL, Enums.TYPE_REWARD_MODIFIER, 250 * 10 ** 9, 3),
    (BuildingEnums.ALL, Enums.TYPE_REWARD_MODIFIER, 10 ** 12, 3),

    (BuildingEnums.LEMON, Enums.TYPE_REWARD_MODIFIER, 20 * 10 ** 12, 3),
    (BuildingEnums.NEWSPAPER, Enums.TYPE_REWARD_MODIFIER, 50 * 10 ** 12, 3),
    (BuildingEnums.CARWASH, Enums.TYPE_REWARD_MODIFIER, 100 * 10 ** 12, 3),
    (BuildingEnums.PIZZA, Enums.TYPE_REWARD_MODIFIER, 500 * 10 ** 12, 3),
    (BuildingEnums.DONUT, Enums.TYPE_REWARD_MODIFIER, 10 ** 15, 3),
    (BuildingEnums.SHRIMP, Enums.TYPE_REWARD_MODIFIER, 2 * 10 ** 15, 3),
    (BuildingEnums.HOCKEY, Enums.TYPE_REWARD_MODIFIER, 5 * 10 ** 15, 3),
    (BuildingEnums.MOVIE, Enums.TYPE_REWARD_MODIFIER, 7 * 10 ** 15, 3),
    (BuildingEnums.BANK, Enums.TYPE_REWARD_MODIFIER, 10 * 10 ** 15, 3),
    (BuildingEnums.OIL, Enums.TYPE_REWARD_MODIFIER, 20 * 10 ** 15, 3),
    (BuildingEnums.ALL, Enums.TYPE_REWARD_MODIFIER, 50 * 10 ** 15, 3),
)


def generate_upgrades():
    upgrades = []

    for u in UPGRADE_VALUES:
        upgrades.append(Upgrade(*u))

    return upgrades


if __name__ == '__main__':
    upgrades = generate_upgrades()
    print(*sorted(upgrades, key=lambda u: u.cost), sep="\n")
