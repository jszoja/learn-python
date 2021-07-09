# Basic arcade program
# Displays a white window with a blue circle in the middle

# Imports
from arcade.key import MOD_CTRL, MOD_SHIFT
from game.astar.Box import Box, BoxType
from game.astar.pathf import PathFinder
import arcade

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Find a path"
SCREEN_MARGIN = 25
BOX_SIZE = 30


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.maxW = int((SCREEN_WIDTH - 2*SCREEN_MARGIN) / BOX_SIZE)
        self.maxH = int((SCREEN_HEIGHT - 2*SCREEN_MARGIN) / BOX_SIZE)
        self.map = []
        self.start = self.end = None
        self.newRoute = False
        self.searching = False

    def setup(self):
        # Set up your game here
        for y in range(self.maxH):
            row = []
            for x in range(self.maxW):
                row.append(Box(x, y, BOX_SIZE, self.map))
            self.map.append(row)
        self.map[2][2].connect(self.map[2][3])

    def run(self):
        arcade.run()

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        for row in self.map:
            for box in row:
                box.render()
        if self.route:
            i = 1
            for box in self.route:
                if i == len(self.route):
                    break
                arcade.draw_line(
                    box.mx, box.my, self.route[i].mx, self.route[i].my, arcade.color.YELLOW, 3)
                i += 1

    def showRoute(self):
        pathFinder = PathFinder(self.start, self.end)
        path = pathFinder.find()
        path.reverse()
        if len(path):
            self.route = [self.start]
            self.route.extend(path)
            self.route.append(self.end)

    def cleanRoute(self):
        for row in self.map:
            for box in row:
                box.pathNode.reset()
                box.connect(None)
                if(box in [self.start, self.end]) or box.type == BoxType.WALL:
                    continue
                box.setType(BoxType.DEFAULT)

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        if self.searching:
            self.start.colour = BoxType.DEFAULT.value if self.start.colour == BoxType.START.value else BoxType.START.value

    def findBox(self, x, y):
        if x < SCREEN_MARGIN or x > SCREEN_WIDTH-SCREEN_MARGIN:
            return None
        if y < SCREEN_MARGIN or y > SCREEN_HEIGHT - SCREEN_MARGIN:
            return None
        col = int((x-SCREEN_MARGIN)/BOX_SIZE)
        row = self.maxH - int((y-SCREEN_MARGIN)/BOX_SIZE)-1
        return self.map[row][col]

    def on_key_release(self, symbol, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass
        #self.start = self.map[3][3]
        #self.end = self.map[8][12]
        #self.newRoute = True
        # self.start.setType(BoxType.START)
        # self.end.setType(BoxType.END)

    def on_mouse_press(self, x, y, button, modifiers):
        box = self.findBox(x, y)
        if box == None:
            return

        if modifiers & MOD_SHIFT:
            if self.end:
                self.end.setType(BoxType.DEFAULT)
            box.setType(BoxType.END)
            self.end = box
            if self.start:
                # self.showRoute()
                self.newRoute = True
        elif modifiers & MOD_CTRL:
            if self.start:
                self.start.setType(BoxType.DEFAULT)
            box.setType(BoxType.START)
            self.start = box
            if self.end:
                self.newRoute = True
        # elif (box.type != BoxType.END and box.type != BoxType.START):
        elif box.type not in [BoxType.END, BoxType.START]:
            box.toggleWall()
            if self.start and self.end:
                self.newRoute = True

        if self.newRoute:
            self.newRoute = False
            self.cleanRoute()
            self.searching = True
            self.showRoute()
            self.searching = False


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    game.run()


if __name__ == "__main__":
    main()
