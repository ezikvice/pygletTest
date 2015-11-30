import pyglet
from pyglet.window import key
import resources as res
import numpy as np
import Brick

__author__ = 'Dmitry'

# shape = (9, 9)
# arr = np.ones((9, 9))
#TODO: загружать поле из файла
arr = np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2],
               [2, 3, 3, 3, 3, 3, 3, 3, 2],
               [2, 3, 0, 0, 0, 0, 0, 3, 2],
               [2, 3, 0, 0, 0, 0, 0, 3, 2],
               [2, 3, 0, 0, 0, 0, 0, 3, 2],
               [2, 3, 0, 4, 1, 0, 0, 3, 2],
               [2, 3, 0, 0, 0, 0, 0, 3, 2],
               [2, 3, 3, 3, 3, 3, 3, 3, 2],
               [2, 2, 2, 2, 2, 2, 2, 2, 2]])

pyglet.resource.path = ["res"]
pyglet.resource.reindex()


# player = pyglet.sprite.Sprite(res.player, x=50, y=50)

batch = pyglet.graphics.Batch()
trees = []  #TODO: сделать словарик с ресурсами (номер-имя), или лучше спрайты сделать объектами и в них хранить также номер
bricks = []
boxes = []
cell = 64
winwidth = cell*10
winheight = cell*10
arrsize = arr.size
for i in range(len(arr)):
    for k in range(len(arr[i])):
        x, y = (k % arrsize) * cell, i * 64
        if arr[i, k] == 2:
            trees.append(pyglet.sprite.Sprite(res.grass, x, winwidth - cell - y, batch=batch))
        if arr[i, k] == 3:
            # bricks.append(pyglet.sprite.Sprite(res.brick, x, winwidth - cell - y, batch=batch))
            bricks.append(Brick.Brick(i, k, batch))
        if arr[i, k] == 4:
            boxes.append(pyglet.sprite.Sprite(res.box, x, winwidth - cell - y, batch=batch))
        elif arr[i, k] == 1:
            player = pyglet.sprite.Sprite(res.player, x, winwidth - cell - y)


window = pyglet.window.Window(width=(cell*10), height=(cell*10))
fps_display = pyglet.window.FPSDisplay(window)

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=100, y=36,
                          anchor_x='left', anchor_y='center')



@window.event
def on_key_press(symbol, modifiers):
    r = player.x // cell
    c = player.y // cell - 1
    if symbol == key.UP:
        if arr[r][c+1] != 3: #TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            label.text = '[{0}, {1}]'.format(r, c+1)
            player.set_position(player.x, player.y + cell)
    if symbol == key.DOWN:
        if arr[r][c-1] != 3: #TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            label.text = '[{0}, {1}]'.format(r, c-1)
            player.set_position(player.x, player.y - cell)
    if symbol == key.LEFT:
        if arr[r-1][c] != 3: #TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            label.text = '[{0}, {1}]'.format(r-1, c)
            player.set_position(player.x - cell, player.y)
    if symbol == key.RIGHT:
        if arr[r+1][c] != 3: #TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            label.text = '[{0}, {1}]'.format(r+1, c)
            player.set_position(player.x + cell, player.y)


@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()
    player.draw()
    fps_display.draw()


def update(dt):
    pass

pyglet.clock.set_fps_limit(60)
pyglet.clock.schedule_interval(update, 1/120)

pyglet.app.run()
