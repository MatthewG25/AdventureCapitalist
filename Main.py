import threading
import time

import Buildings
import GUI
import Unlocks
import Upgrades

# PLAYER STATS #
MONEY = 100
TIME_INTERVAL = 1


def get_money():
    return MONEY


def reduce_money(by):
    global MONEY
    MONEY -= by


def increase_money(by):
    global MONEY
    MONEY += by


def progress_time(t=1):
    for name, b, in buildings.items():
        increase_money(b.generate_reward(t))


def initialise_play():
    while True:
        time.sleep(TIME_INTERVAL)
        progress_time(TIME_INTERVAL)


if __name__ == '__main__':
    buildings = Buildings.initialise_buildings()
    unlocks = Unlocks.generate_unlocks()
    upgrades = Upgrades.generate_upgrades()

    threading.Thread(target=GUI.initialise_gui, args=(buildings,)).start()
    threading.Thread(target=initialise_play).start()
