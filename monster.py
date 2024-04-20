from settings import *
from entity import Entity
from warning_signal import WarningSignal
from random import randint, sample


class Monster(Entity):
    def __init__(self, app, name, screen_pos, mirror=(False, False)):
        super().__init__(app, name, screen_pos=screen_pos, mirror=mirror)
        self.curr_position = vec2(0)
        self.positions = [(190, 120), (520, 120), (850, 120),
                          (190, 450), (520, 450), (850, 450),
                          (190, 780), (520, 780), (850, 780)]

    def attack(self):
        if self.app.att_trigger:
            # TODO I should make it so that the attack doesn't always hit the players position
            self.curr_position: pg.rect.RectType = self.app.player.rect
            WarningSignal(self.app, "warning", (self.curr_position.centerx - 30, self.curr_position.centery + 90))

            random_positions = sample(self.positions, randint(1, 3))
            for position in random_positions:
                WarningSignal(self.app, "warning", position)

    def update(self):
        super().update()
        self.attack()
