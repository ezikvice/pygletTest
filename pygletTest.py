import pyglet
from pyglet.window import key
import resources as res
import numpy as np

__author__ = 'Dmitry'

# shape = (9, 9)
# arr = np.ones((9, 9))
arr = np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 0, 0, 0, 0, 0, 0, 0, 2],
               [2, 0, 0, 0, 0, 0, 0, 0, 2],
               [2, 0, 0, 0, 0, 0, 0, 0, 2],
               [2, 0, 0, 0, 0, 0, 0, 0, 2],
               [2, 0, 0, 0, 0, 0, 0, 0, 2],
               [2, 0, 0, 0, 0, 0, 0, 0, 2],
               [2, 1, 0, 0, 0, 0, 0, 0, 2],
               [2, 2, 2, 2, 2, 2, 2, 2, 2]])

pyglet.resource.path = ["res"]
pyglet.resource.reindex()


# player = pyglet.sprite.Sprite(res.player, x=50, y=50)

batch = pyglet.graphics.Batch()
bricks = []
cell = 64
winwidth = cell*10
winheight = cell*10
arrsize = arr.size
for i in range(len(arr)):
    for k in range(len(arr[i])):
        x, y = (k % arrsize) * cell, i * 64
        if arr[i, k] == 2:
            bricks.append(pyglet.sprite.Sprite(res.brick, x, winwidth - cell - y, batch=batch))
        elif arr[i, k] == 1:
            player = pyglet.sprite.Sprite(res.player, x, winheight - cell - y)


window = pyglet.window.Window(width=(cell*10), height=(cell*10))
fps_display = pyglet.window.FPSDisplay(window)

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=100, y=36,
                          anchor_x='left', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()
    player.draw()
    fps_display.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:

        player.set_position(player.x, player.y + cell)
    if symbol == key.DOWN:
        player.set_position(player.x, player.y - cell)
    if symbol == key.LEFT:
        player.set_position(player.x - cell, player.y)
    if symbol == key.RIGHT:
        player.set_position(player.x + cell, player.y)


def update(dt):
    pass

pyglet.clock.set_fps_limit(60)
pyglet.clock.schedule_interval(update, 1/120)

pyglet.app.run()
