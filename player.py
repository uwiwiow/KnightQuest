from settings import *
from entity import Entity
from bar import Bar


class Player(Entity):
    def __init__(self, app, name, screen_pos):
        super().__init__(app, name, screen_pos=screen_pos)
        self.animations = ['idle', 'attack', 'attack2', 'move_backward', 'move_forward', 'death',]
        self.animation = self.animations[0]
        self.can_attack = True
        Bar(self.app, 'red_bar', screen_pos=(20, 20))

    def control(self):
        key_state = pg.key.get_pressed()

        if key_state[pg.K_k] and self.can_attack:
            self.can_attack = False
            self.frame_index = 0
            self.animation = self.animations[1]

        if key_state[pg.K_l] and self.can_attack:
            self.can_attack = False
            self.frame_index = 0
            self.animation = self.animations[2]

        if self.can_attack and self.animation != 'death':
            self.animation = self.animations[0]
            if key_state[pg.K_w] or key_state[pg.K_UP]:
                self.rect.y -= 330
            if key_state[pg.K_s] or key_state[pg.K_DOWN]:
                self.rect.y += 330
            if key_state[pg.K_a] or key_state[pg.K_LEFT]:
                self.animation = self.animations[3]
                self.rect.x -= 330
            if key_state[pg.K_d] or key_state[pg.K_RIGHT]:
                self.animation = self.animations[4]
                self.rect.x += 330

        if key_state[pg.K_p]:
            print(self.rect.center)

    def check_death(self):
        if self.app.death_trigger:
            self.animation = self.animations[5]

    def check_collision(self):
        hit = pg.sprite.spritecollide(self, self.app.collision_group,
                                      dokill=True, collided=pg.sprite.collide_mask)
        # maybe not do kill, TO DO ? I would need to add a lock to only send once the life event per attack

        if hit:
            pg.event.post(pg.event.Event(self.app.life_event))
            # TODO could try to pass this as a parameter to bar object

    def update(self):
        super().update()
        self.control()
        self.check_death()
        self.check_collision()

    def animate(self):
        if self.app.anim_trigger:
            self.frame_index += 1
            if self.frame_index >= self.attrs['animations'][self.animation][1]:
                if self.animation == 'attack' or self.animation == 'attack2':
                    self.animation = self.animations[0]
                    self.can_attack = True
                self.frame_index = 0
                if self.animation == 'death':
                    self.frame_index = 1
                    pg.time.set_timer(self.app.anim_event, 0)  # not sure if this is the best way
                    pg.time.set_timer(self.app.att_event, 0)
                    for sprite in self.app.collision_group:
                        sprite.kill()
            self.image = self.images[self.animation][self.frame_index]
