from settings import *
from monster import Monster


class Scene:
    def __init__(self, app):
        self.app = app
        self.monsters = ['mole', 'rat']
        self.attack_names = ['explosion', 'claw']
        self.attack_times = [2000, 1600, 1200, 800]
        self.monster = 0
        self.attack_name = 0
        self.attack_time = -1

    def spawn_monster(self):
        if self.attack_time == 3:
            self.monster += 1
            self.attack_name += 1
            self.attack_time = 0
        else:
            self.attack_time += 1

        Monster(self.app, self.monsters[self.monster],
                self.attack_names[self.attack_name],
                self.attack_times[self.attack_time],
                screen_pos=((H_WIDTH // 2) * 3, H_HEIGHT),
                mirror=(True, False))

