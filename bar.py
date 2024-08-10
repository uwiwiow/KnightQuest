from settings import *
from entity import Entity


class Bar(Entity):
    def __init__(self, app, name, screen_pos):
        super().__init__(app, name, screen_pos=screen_pos)
        self.frame_index = self.attrs['animations']['idle'][1] - 1
        self.image = self.images['idle'][self.frame_index]

    def animate(self):
        if self.name == "red_bar":
            if self.app.life_trigger:
                self.frame_index -= 1
                if self.frame_index == 0:
                    # lose
                    pg.event.post(pg.event.Event(self.app.death_event))

                self.image = self.images['idle'][self.frame_index]
        if self.name == "blue_bar":
            if self.app.att_trigger:
                self.frame_index -= 1
                if self.frame_index <= 0:
                    # win
                    self.frame_index = 0
                    pg.event.post(pg.event.Event(self.app.en_death_event))
                self.image = self.images['idle'][self.frame_index]

    def set_rect(self):
        self.rect.x = self.screen_pos[0]
        self.rect.y = self.screen_pos[1]