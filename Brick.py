import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class Brick(sprite.Sprite):

    id = 3

    def __init__(self, row, column, batch):
        super(Brick, self).__init__(res.brick, x=row*CELL_SIZE, y=column*CELL_SIZE, batch=batch)
        self.row = row
        self.column = column


