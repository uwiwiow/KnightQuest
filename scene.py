from settings import *
from monster import Monster


class Scene:
    def __init__(self, app):
        self.app = app
        self.load_scene()

    def load_scene(self):
        Monster(self.app, 'mole', screen_pos=((H_WIDTH // 2) * 3, H_HEIGHT), mirror=(True, False))

