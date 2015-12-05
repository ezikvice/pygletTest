import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class Box(sprite.Sprite):

    id = 4

    def __init__(self, column, row, batch):
        super(Box, self).__init__(img=res.box, x=column*CELL_SIZE, y=WIN_HEIGHT - row*CELL_SIZE, batch=batch)
        self.column = column
        self.row = row
