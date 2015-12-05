import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class Brick(sprite.Sprite):

    id = 3

    def __init__(self, column, row, batch):
        super(Brick, self).__init__(res.brick, x=column*CELL_SIZE, y=WIN_HEIGHT - row*CELL_SIZE, batch=batch)
        self.column = column
        self.row = row


