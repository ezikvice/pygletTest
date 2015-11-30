import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class Box(sprite.Sprite):

    id = 4

    def __init__(self, row, column, batch):
        super(Box, self).__init__(res.box, x=row*CELL_SIZE, y=(column+1)*CELL_SIZE, batch=batch)
        self.row = row
        self.column = column
