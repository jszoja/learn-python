import arcade
import PIL.Image

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def changeSpriteColor(self, color):
        image = PIL.Image.new(
            'RGBA', (self.mySprite.width, self.mySprite.height), color)
        self.mySprite.texture = arcade.Texture("Solid", image)

    def setup(self):
        # Set up your game here
        defaultColor = arcade.color.RED
        self.mySprite = arcade.SpriteSolidColor(100, 100, defaultColor)
        self.mySprite.set_position(200, 200)
        self.mySprite.defaultColor = defaultColor
        self.mySprite.dragging = False

        self.spriteList = arcade.SpriteList()
        self.spriteList.append(self.mySprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.spriteList.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.spriteList.update()

    def on_key_release(self, symbol, modifiers):
        self.mySprite.color = self.mySprite.defaultColor

    def on_key_press(self, symbol, modifiers):
        #self.mySprite.color = arcade.color.GREEN
        self.changeSpriteColor(arcade.color.WILD_WATERMELON)
        if symbol == arcade.key.RIGHT:
            self.mySprite.change_x += 3
        elif symbol == arcade.key.LEFT:
            self.mySprite.change_x -= 3
        if symbol == arcade.key.UP:
            self.mySprite.change_y += 3
        elif symbol == arcade.key.DOWN:
            self.mySprite.change_y -= 3

    def on_mouse_press(self, x, y, button, modifiers):
        if self.mySprite.collides_with_point(arcade.Point(x, y)):
            self.mySprite.dragging = (
                self.mySprite.center_x - x, self.mySprite.center_y - y)
            self.changeSpriteColor(arcade.color.WHITE)

    def on_mouse_release(self, x, y, button, modifiers):
        if self.mySprite.collides_with_point(arcade.Point(x, y)):
            self.mySprite.dragging = False
            self.changeSpriteColor(self.mySprite.defaultColor)

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
