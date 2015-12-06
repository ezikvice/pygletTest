import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class GameObject(sprite.Sprite):

    def __init__(self, img, obj_id, row, column, batch):
        super(GameObject, self).__init__(img, column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE, batch=batch)
        self.column = column
        self.row = row
        self.obj_id = obj_id

    def move(self, row, column):
        self.column = column
        self.row = row
        self.set_position(column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE)


class Player(GameObject):

    def __init__(self, column, row, batch):
        super(Player, self).__init__(res.player, 1, column, row, batch)


class Tree(GameObject):

    def __init__(self, column, row, batch):
        super(Tree, self).__init__(res.pinetree, 2, column, row, batch)


class Brick(GameObject):

    def __init__(self, column, row, batch):
        super(Brick, self).__init__(res.brick, 3, column, row, batch)


class Box(GameObject):

    def __init__(self, column, row, batch):
        super(Box, self).__init__(res.box, 4, column, row, batch)


class BoxTarget(GameObject):

    def __init__(self, column, row, batch):
        super(Brick, self).__init__(res.brick, 10, column, row, batch)


