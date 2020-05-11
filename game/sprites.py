from arcade import Sprite as ASprite
from game.KeyListenerInterface import KeyListener
from dataclasses import dataclass
import arcade


class Sprite(ASprite, KeyListener):
    def __init__(self, filename: str = None,
                 scale: float = 1,
                 image_x: float = 0, image_y: float = 0,
                 image_width: float = 0, image_height: float = 0,
                 center_x: float = 0, center_y: float = 0,
                 repeat_count_x: int = 1, repeat_count_y: int = 1):
        super().__init__(filename, scale, image_x, image_y, image_width,
                         image_height, center_x, center_y, repeat_count_x, repeat_count_y)


# @dataclass(init=False)
class Hex(Sprite):

 #   x: int
  #  y: int

    def __init__(self, x, y):
        super().__init__('assets/hex-sprite.png', 0.25, 0, 0, 512, 512, 256, 256, 2, 1)
        self.x = x
        self.y = y
        self.rcut = 0
        self.set_position(self.x, self.y)

    def onKeyPress(self, key, modifier):
        if key == arcade.key.G:
            self.x += 10
            self.set_position(self.x, self.y)
            print('pos x ='+str(self.x))
        if key == arcade.key.S:
            factor = 0.9
            if modifier == arcade.key.MOD_SHIFT:
                factor = 1.1
            self.scale *= factor
            print(f'scaling to {self.scale}')
        if key == arcade.key.F:

            self.rcut += 100
            #self.width *= 0.9
            #tex = arcade.load_texture('assets/hex-sprite.png', 0.25, 0, 0, 512, 512, 256, 256, 2, 1)
            tex = arcade.load_texture(
                'assets/hex-sprite.png', 0, 0, 512-self.rcut, 512)

            self._set_texture2(tex)

            #self.set_position(self.x+10, self.y)
            #self.width -= 10*0.25
