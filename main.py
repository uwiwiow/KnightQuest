import sys
from settings import *
from scene import Scene
from player import Player  # I think this should go in main because monster.py needs to know players position


class App:
    def __init__(self):
        pg.init()
        self.run_app = True
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0.01
        self.bg = pg.image.load(BG)

        # user events
        self.life_trigger = False
        self.life_event = pg.USEREVENT + 0
        self.death_trigger = False
        self.death_event = pg.USEREVENT + 1
        self.att_trigger = False
        self.att_event = pg.USEREVENT + 2
        pg.time.set_timer(self.att_event, 2000)
        #   animation event
        self.anim_trigger = False
        self.anim_event = pg.USEREVENT + 3
        pg.time.set_timer(self.anim_event, 150)  # time for the next frame in the animation

        # groups
        self.main_group = pg.sprite.Group()
        self.collision_group = pg.sprite.Group()

        # game objects
        self.scene = Scene(self)
        self.player = Player(self, 'knight', screen_pos=((H_WIDTH // 2) + 150, H_HEIGHT - 90))
        pg.display.set_caption("Knight Quest")
        pg.mouse.set_visible(False)

    def check_events(self):
        self.anim_trigger = False
        self.life_trigger = False
        self.att_trigger = False
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif e.type == self.anim_event:
                self.anim_trigger = True
            elif e.type == self.life_event:
                self.life_trigger = True
            elif e.type == self.death_event:
                self.death_trigger = True
            elif e.type == self.att_event:
                self.att_trigger = True

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def update(self):
        self.main_group.update()
        pg.display.set_caption(f'Knight Quest – Running at{self.clock.get_fps(): .1f} fps')
        self.delta_time = self.clock.tick()

    def draw(self):
        self.screen.fill("#000000")
        self.screen.blit(self.bg, vec2(0))
        self.main_group.draw(self.screen)
        pg.display.flip()

    def run(self):
        while self.run_app:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
