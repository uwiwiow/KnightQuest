from entity import Entity
from attack import Attack


class WarningSignal(Entity):
    def __init__(self, app, name, screen_pos, mirror=(False, False)):
        super().__init__(app, name, screen_pos=screen_pos, mirror=mirror)
        self.rect.center = screen_pos
        self.screen_pos = screen_pos

    def animate(self):
        if self.app.anim_trigger:
            self.frame_index += 1
            if self.frame_index >= self.attrs['animations']['idle'][1]:
                self.kill()
                Attack(self.app, "explosion", self.screen_pos)
            else:
                self.image = self.images['idle'][self.frame_index]
