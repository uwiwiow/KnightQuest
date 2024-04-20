from settings import *


class Entity(pg.sprite.Sprite):
    def __init__(self, app, name, screen_pos=CENTER, mirror: tuple[bool, bool] = (False, False)):
        self.app = app
        self.name = name
        self.group = app.main_group
        super().__init__(self.group)

        self.screen_pos = screen_pos
        self.mirror = mirror

        self.attrs = ENTITY_SPRITE_ATTRS[name]
        self.images = self.load_sprites()
        self.image = self.images['idle'][0]
        self.rect = self.image.get_rect()
        self.frame_index = 0

    def animate(self):
        if self.app.anim_trigger:
            self.frame_index += 1
            if self.frame_index >= self.attrs['animations']['idle'][1]:
                self.frame_index = 0
            self.image = self.images['idle'][self.frame_index]

    def update(self):
        self.set_rect()
        self.animate()

    def load_sprites(self):
        sprite_sheet = pg.image.load(self.attrs['path'])
        sprites = []
        sheet_width, sheet_height = sprite_sheet.get_size()
        for y in range(0, sheet_height, self.attrs['size'][1]):
            for x in range(0, sheet_width, self.attrs['size'][0]):
                sprite = sprite_sheet.subsurface(pg.Rect(x, y, self.attrs['size'][0], self.attrs['size'][1]))
                sprite = pg.transform.flip(sprite, self.mirror[0], self.mirror[1])
                sprites.append(pg.transform.scale(sprite, vec2(sprite.get_size()) * self.attrs['scale']))

        images = {}
        for animation_name, frame_range in self.attrs['animations'].items():
            frames = [sprites[num] for num in range(frame_range[0], frame_range[0] + frame_range[1])]
            images.update({animation_name: frames})

        return images

    def set_rect(self):
        self.rect.center = self.screen_pos
