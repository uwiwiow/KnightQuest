from settings import *
from entity import Entity
from warning_signal import WarningSignal
from random import randint, sample
from bar import Bar


class Monster(Entity):
    def __init__(self, app, name, attack_time, screen_pos, mirror=(False, False)):
        super().__init__(app, name, screen_pos=screen_pos, mirror=mirror)
        self.curr_position = vec2(0)
        self.positions = [(190, 120), (520, 120), (850, 120),
                          (190, 450), (520, 450), (850, 450),
                          (190, 780), (520, 780), (850, 780)]
        self.animations = ['idle', 'attack', 'hit', 'death']
        self.animation = self.animations[0]
        self.death = False
        self.bar = Bar(self.app, 'blue_bar', screen_pos=(WIDTH - 260, 20))

        pg.time.set_timer(self.app.en_att_event, attack_time)

    def attack(self):
        if self.app.en_att_trigger:
            # TODO I should make it so that the attack doesn't always hit the players position
            self.curr_position: pg.rect.RectType = self.app.player.rect
            if randint(1, 3) == 1:
                WarningSignal(self.app, "warning", (self.curr_position.centerx - 30, self.curr_position.centery + 90))

            random_positions = sample(self.positions, randint(1, 3))
            for position in random_positions:
                if position is not self.curr_position:
                    WarningSignal(self.app, "warning", position)

            self.frame_index = 0
            self.animation = self.animations[1]

    def check_hit(self):
        if self.app.att_trigger and not self.death:
            self.frame_index = 0
            self.animation = self.animations[2]

    def check_death(self):
        if self.app.en_death_trigger:
            if not self.death:
                self.frame_index = 0
            self.death = True
            pg.time.set_timer(self.app.en_att_event, 0)
            self.animation = self.animations[3]

    def update(self):
        super().update()
        self.attack()
        self.check_hit()
        self.check_death()

    def animate(self):
        if self.app.anim_trigger:
            self.frame_index += 1
            if self.frame_index >= self.attrs['animations'][self.animation][1]:
                self.frame_index = 0
                if self.animation == 'attack' or self.animation == 'hit' and not self.app.en_death_trigger:
                    self.animation = self.animations[0]
                if self.animation == 'death':
                    for sprite in self.app.collision_group:
                        sprite.kill()

                    self.bar.kill()
                    self.kill()
            self.image = self.images[self.animation][self.frame_index]
