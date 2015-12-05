import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class GameObject(sprite.Sprite):

    def __init__(self, img, obj_id, column, row, batch):
        super(GameObject, self).__init__(img, column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE, batch=batch)
        self.column = column
        self.row = row
        self.obj_id = obj_id

    def move(self, row, column):
        self.column = column
        self.row = row
        self.set_position(column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE)


class Box(GameObject):

    def __init__(self, column, row, batch):
        super(Box, self).__init__(res.box, 4, column, row, batch)


class Player(GameObject):

    def __init__(self, column, row, batch):
        super(Player, self).__init__(res.player, 1, column, row, batch)

