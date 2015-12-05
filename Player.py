import pyglet.sprite as sprite
import resources as res
from GameMetric import *

__author__ = 'Dmitry'


class Player(sprite.Sprite):
    id = 1

    def __init__(self):
        super(Player, self).__init__(res.player)
        self.column = 0
        self.row = 0

    def move(self, row, column):
        self.column = column
        self.row = row
        self.set_position(column * CELL_SIZE, WIN_HEIGHT - row * CELL_SIZE)

