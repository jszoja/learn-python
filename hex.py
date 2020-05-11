import arcade
import PIL.Image
import copy
from game.KeyListenerInterface import KeyListener
from game.sprites import Hex
from game.sprites import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCALE = 0.25


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def spriteHover(self, hover=1):
        self.mySprite.set_texture(hover)

    def setup(self):
        # Set up your game here
        self.mySprite = arcade.Sprite(
            'assets/hex-sprite.png', SCALE, 0, 0, 512, 512, 256, 256, 2, 1)
        self.mySprite.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.mySprite.dragging = False
        texture = arcade.load_texture(
            'assets/hex-sprite.png', 512, 0, 512, 512)
        self.mySprite.append_texture(texture)

        sprite2 = copy.deepcopy(self.mySprite)
        sprite2.set_position(300, 100)

        self.spriteList = arcade.SpriteList()
        self.spriteList.append(self.mySprite)
        self.spriteList.append(sprite2)

        hex = Hex(100, 300)
        self.spriteList.append(hex)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.spriteList.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.spriteList.update()

    def on_key_release(self, symbol, modifiers):
        #self.mySprite.color = self.mySprite.defaultColor
        pass

    def on_key_press(self, symbol, modifiers):
        #self.mySprite.color = arcade.color.GREEN
        # self.changeSpriteColor(arcade.color.WILD_WATERMELON)

        # print('key='+str(symbol))
        for sprite in self.spriteList:
            if isinstance(sprite, KeyListener):
                sprite.onKeyPress(symbol, modifiers)

        if symbol == arcade.key.RIGHT:
            self.mySprite.change_x += 3
        elif symbol == arcade.key.LEFT:
            self.mySprite.change_x -= 3
        if symbol == arcade.key.UP:
            self.mySprite.change_y += 3
        elif symbol == arcade.key.DOWN:
            self.mySprite.change_y -= 3
        elif symbol == arcade.key.Q:
            self.mySprite.scale += 0.1
            #self.mySprite.width *= 0.5
            #self.mySprite.change_x = 10
        elif symbol == arcade.key.W:
            self.mySprite.scale -= 0.1

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mySprite.collides_with_point(arcade.Point(x, y)):
            self.mySprite.dragging = (
                self.mySprite.center_x - x, self.mySprite.center_y - y)
            self.spriteHover()

    def on_mouse_release(self, x, y, button, modifiers):
        if self.mySprite.collides_with_point(arcade.Point(x, y)):
            self.mySprite.dragging = False
            self.spriteHover(0)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if not self.mySprite.dragging:
            return
        self.mySprite.set_position(self.mySprite.dragging[0]
                                   + dx+x, self.mySprite.dragging[1]+dy+y)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
