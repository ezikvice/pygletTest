import pyglet
import resources as res
from pyglet import clock
import configparser
import numpy as np

__author__ = 'Dmitry'

pyglet.resource.path = ["res"]
pyglet.resource.reindex()

tree = pyglet.sprite.Sprite(res.player, 110, 110)
# tree_down = pyglet.sprite.Sprite()


trees = []
bricks = []
boxes = []
box_targets = []

current_cell = 0, 0

arr = np.array([[3, 3, 3, 3, 3, 3, 3, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [3, 0, 1, 0, 0, 0, 0, 3, 2],
                [3, 0, 4, 0, 0, 10, 0, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [3, 0, 0, 14, 0, 0, 0, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [2, 3, 3, 3, 3, 3, 3, 2, 2],
                [0, 2, 2, 2, 2, 2, 2, 2, 0]])

for row in range(len(arr)):
    for column in range(len(arr[row])):
        current_cell = row, column
        cur_cell_val = arr[current_cell]
        if cur_cell_val >= 10:
            box_targets.append(current_cell)  # кидаем во второй слой
            cur_cell_val -= 10
        if cur_cell_val == 2:
            trees.append(current_cell)
        if cur_cell_val == 3:
            bricks.append(current_cell)
        if cur_cell_val == 4:
            boxes.append(current_cell)

# lets create that config file for next time...
cfgfile = open("test.ini", 'w')

cfg = configparser.ConfigParser()
# add the settings to the structure of the file, and lets write it out...
cfg.add_section('trees')
cfg.set('trees', trees)
cfg.add_section('bricks')
cfg.set('bricks', bricks)
cfg.add_section('boxes')
cfg.set('boxes', boxes)
cfg.add_section('box_targets')
cfg.set('box_targets', box_targets)
cfgfile.close()

window = pyglet.window.Window(width=640, height=640, caption="Gecko Soko")


def update(dt):
    tree.image = res.player_down
    # tree.rotation += 100*dt


clock.schedule(update)


@window.event
def on_draw():
    window.clear()
    tree.draw()


pyglet.app.run()
