class Building:
    def __init__(self, _id, base_cost=0, cost_growth=2, base_reward=0, base_timer=1, building_name="default"):
        self.id = _id
        self.count = 0
        self.reward_multiplier = 1
        self.timer_modifier = 1

        self.base_cost = base_cost
        self.base_reward = base_reward
        self.base_timer = base_timer
        self.cost_growth = cost_growth

        self.name = building_name
        self.count_offset = -1 if building_name == Enums.LEMON else 0    # Needed for cost calculation

    def generate_reward(self, time_passed=1):
        return int((self.count * self.base_reward * self.reward_multiplier * time_passed) / (
            self.base_timer * self.timer_modifier))

    def cost(self, num=1):
        a = self.base_cost * self.cost_growth ** (self.count + self.count_offset)
        return int(a * (1 - self.cost_growth ** num) / (1 - self.cost_growth))

    def __str__(self):
        return "(count: {}, cost: {}, rewardPer: {}, timer: {})".format(self.count, self.cost(), self.base_reward, self.base_timer)

    def __repr__(self):
        return str(self)


class Enums:
    # Building names
    LEMON = "lemon"
    NEWSPAPER = "newspaper"
    CARWASH = "carwash"
    PIZZA = "pizza"
    DONUT = "donut"
    SHRIMP = "shrimp"
    HOCKEY = "hockey"
    MOVIE = "movie"
    BANK = "bank"
    OIL = "oil"
    ALL = "all"
    DEFAULT = "default"


# id    base_cost     cost_growth     base_reward     base_timer
BUILDING_VALUES = {
    Enums.LEMON: (0, 4, 1.07, 1, 0.6),
    Enums.NEWSPAPER: (1, 60, 1.15, 60, 3),
    Enums.CARWASH: (2, 720, 1.14, 540, 6),
    Enums.PIZZA: (3, 8640, 1.13, 4320, 12),
    Enums.DONUT: (4, 103680, 1.12, 51840, 24),
    Enums.SHRIMP: (5, 1.244 * 10 ** 6, 1.11, 662080, 96),
    Enums.HOCKEY: (6, 14.93 * 10 ** 6, 1.1, 7464960, 384),
    Enums.MOVIE: (7, 179.159 * 10 ** 6, 1.09, 89579520, 1536),
    Enums.BANK: (8, 2.15 * 10 ** 9, 1.08, 1074954240, 6144),
    Enums.OIL: (9, 25.799 * 10 ** 9, 1.07, 29668737024, 36864)
}


def initialise_buildings() -> dict:
    buildings = dict()

    for name, values in BUILDING_VALUES.items():
        buildings[name] = Building(*values, name)

    buildings[Enums.LEMON].count = 1

    return buildings


if __name__ == '__main__':
    buildings = initialise_buildings()

    for k, v in buildings.items():
        print("{:10}: {}".format(k, v))

