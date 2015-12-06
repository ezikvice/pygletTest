import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class GameObject(sprite.Sprite):
    def __init__(self, img, obj_id, batch, arr):
        row, column = arr
        super(GameObject, self).__init__(img, column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE, batch=batch)
        self.column = column
        self.row = row
        self.obj_id = obj_id

    def move(self, arr):
        row, column = arr
        self.column = column
        self.row = row
        self.set_position(column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE)


class Player(GameObject):
    def __init__(self, batch, arr):
        super(Player, self).__init__(res.player, 1, batch, arr)


class Tree(GameObject):
    def __init__(self, batch, arr):
        super(Tree, self).__init__(res.pinetree, 2, batch, arr)


class Brick(GameObject):
    def __init__(self, batch, arr):
        super(Brick, self).__init__(res.brick, 3, batch, arr)


class Box(GameObject):
    def __init__(self, batch, arr):
        super(Box, self).__init__(res.box, 4, batch, arr)


class BoxTarget(GameObject):
    def __init__(self, batch, arr):
        super(BoxTarget, self).__init__(res.target, 10, batch, arr)
