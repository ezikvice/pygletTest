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


def save_file(filename):
    # lets create that config file for next time...
    cfgfile = open(filename, 'w')

    cfg = configparser.ConfigParser()
    # add the settings to the structure of the file, and lets write it out...
    cfg.add_section('GameObjects')
    cfg.set('GameObjects', 'trees', ', '.join(str(x) for x in trees))
    cfg.set('GameObjects', 'bricks', ', '.join(str(x) for x in bricks))
    cfg.set('GameObjects', 'boxes', ', '.join(str(x) for x in boxes))
    cfg.set('GameObjects', 'box_targets', ', '.join(str(x) for x in box_targets))
    cfg.write(cfgfile)
    cfgfile.close()

save_file("test.ini")

opencfg = configparser.ConfigParser()
opencfg.read("levels/1.ini")
print(opencfg.get("GameObjects", 'trees'))
print(opencfg.get("GameObjects", 'bricks'))

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
