from entity import Entity


class Attack(Entity):
    def __init__(self, app, name, screen_pos, mirror=(False, False)):
        super().__init__(app, name, screen_pos=screen_pos, mirror=mirror)
        self.app.collision_group.add(self)
        self.rect.center = screen_pos

    def animate(self):
        if self.app.anim_trigger:
            self.frame_index += 1
            if self.frame_index >= self.attrs['animations']['idle'][1]:
                self.kill()
            else:
                self.image = self.images['idle'][self.frame_index]
