import pygame as pg


vec2 = pg.math.Vector2

RES = WIDTH, HEIGHT = vec2(1600, 900)

CENTER = H_WIDTH, H_HEIGHT = RES // 2

BG = 'assets/interface/background.png'

ENTITY_SPRITE_ATTRS = {
    'knight': {
        'path': 'assets/entities/knight/knight.png',
        'size': (90, 80),
        'scale': 5,
        'animations': {
            'idle': (1, 4),
            'attack': (5, 7),
            'attack2': (12, 4),
            'move_backward': (16, 2),
            'move_forward': (18, 2),
            'death': (20, 2)
        }
    },
    'red_bar': {
        'path': 'assets/entities/bar/redbar.png',
        'size': (20, 16),
        'scale': 12,  # maybe 5
        'animations': {
            'idle': (0, 7)
        }
    },
    'warning': {
        'path': 'assets/entities/warning/warning.png',
        'size': (32, 32),
        'scale': 6,  # maybe 5
        'animations': {
            'idle': (0, 9)
        }
    },
    'explosion': {
        'path': 'assets/entities/explosion/explosion.png',
        'size': (143, 143),
        'scale': 1.5,
        'animations': {
            'idle': (0, 7)
        }
    },
    'mole': {
        'path': 'assets/entities/monsters/Brain Mole Monarch Sprite Sheet.png',
        'size': (32, 32),
        'scale': 5,
        'animations': {
            'idle': (0, 4),
            'attack': (7, 4),
            'hit': (14, 4),
            'death': (21, 7)
        }
    }
}
