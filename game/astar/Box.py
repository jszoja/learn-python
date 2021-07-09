#from astar import SCREEN_HEIGHT, SCREEN_MARGIN
from enum import Enum

import math
import arcade
from game.astar.pathf import PathNode, PathNodeInterface

SCREEN_MARGIN = 25
SCREEN_HEIGHT = 800

COLOR_DEFAULT = arcade.color.BLUE
COLOR_WALL = arcade.color.GRULLO


class BoxType(Enum):
    DEFAULT = arcade.color.BLUE
    WALL = arcade.color.GRULLO
    START = arcade.color.GREEN
    END = arcade.color.RED
    CHECKED = arcade.color.LIGHT_DEEP_PINK


class Box(PathNodeInterface):

    ConnectColor = arcade.color.YELLOW

    def __init__(self, x, y, size, map):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.colour = BoxType.DEFAULT.value
        self.margin = 5
        self.type = BoxType.DEFAULT
        self.map = map
        self.l = SCREEN_MARGIN+(self.size*self.x)-self.margin
        self.t = SCREEN_HEIGHT-SCREEN_MARGIN-self.margin-(self.size*self.y)
        self.r = self.l+self.size-self.margin
        self.b = self.t-self.size+self.margin
        self.mx = (self.r-self.l)/2+self.l
        self.my = self.t - (self.t-self.b)/2
        self.connectedTo = None

    def render(self):
        arcade.draw_lrtb_rectangle_filled(
            self.l, self.r, self.t, self.b, self.colour)
        #arcade.draw_circle_filled(self.mx, self.my, 3., arcade.color.RED)
        if self.connectedTo:
            arcade.draw_line(self.mx, self.my, self.connectedTo.mx,
                             self.connectedTo.my, Box.ConnectColor, 3.)

    def toggleWall(self):
        self.type = BoxType.WALL if self.type in [
            BoxType.DEFAULT, BoxType.CHECKED] else BoxType.DEFAULT
        self.colour = self.type.value

    def setType(self, type):
        self.colour = type.value
        self.type = type

    def getDistance(self, target):
        dx = self.x-target.x
        dy = self.y-target.y
        return math.sqrt(dx*dx+dy*dy)

    def markChecked(self):
        return self.setType(BoxType.CHECKED)

    def getNeighbours(self):
        neighbours = []
        if self.y > 0 and self.map[self.y-1][self.x].type != BoxType.WALL:
            neighbours.append(self.map[self.y-1][self.x])
        if self.y < len(self.map)-1 and self.map[self.y+1][self.x].type != BoxType.WALL:
            neighbours.append(
                self.map[self.y+1][self.x])
        if self.x > 0 and self.map[self.y][self.x-1].type != BoxType.WALL:
            neighbours.append(self.map[self.y][self.x-1])
        if self.x < len(self.map[self.y])-1 and self.map[self.y][self.x+1].type != BoxType.WALL:
            neighbours.append(
                self.map[self.y][self.x+1])
        return neighbours

    def __str__(self):
        return f"Box {self.x}:{self.y}-{self.pathNode.globalGoal}"

    def connect(self, target):
        self.connectedTo = target
        if target:
            target.connectedTo = self
