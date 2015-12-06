import pyglet
from pyglet.window import key
import resources as res
import numpy as np
import GameObjects
from GameMetric import *

__author__ = 'Dmitry'

# TODO: сделать нормальный расчет координат. сейчас неправильно считаются

# shape = (9, 9)
# arr = np.ones((9, 9))
# TODO: загружать поле из файла
arr = np.array([[3, 3, 3, 3, 3, 3, 3, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [3, 0, 1, 0, 0, 0, 0, 3, 2],
                [3, 0, 0, 0, 0, 10, 0, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [3, 0, 0, 14, 0, 0, 0, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [2, 3, 3, 3, 3, 3, 3, 2, 2],
                [0, 2, 2, 2, 2, 2, 2, 2, 0]])

pyglet.resource.path = ["res"]
pyglet.resource.reindex()


# player = pyglet.sprite.Sprite(res.player, x=50, y=50)

batch = pyglet.graphics.Batch()
layer2 = pyglet.graphics.Batch()

trees = []  # TODO: сделать словарик с ресурсами (номер-имя), или лучше спрайты сделать объектами и в них хранить также номер
bricks = []
boxes = []
box_targets = []

current_cell = 0, 0

player = GameObjects.Player(None, current_cell)

arrsize = arr.size

for row in range(len(arr)):
    for column in range(len(arr[row])):
        current_cell = row, column
        cur_cell_val = arr[current_cell]
        if cur_cell_val >= 10:
            box_targets.append(GameObjects.BoxTarget(layer2, current_cell))  # кидаем во второй слой
            cur_cell_val -= 10
        if cur_cell_val == 2:
            trees.append(GameObjects.Tree(batch, current_cell))
        if cur_cell_val == 3:
            bricks.append(GameObjects.Brick(batch, current_cell))
        if cur_cell_val == 4:
            boxes.append(GameObjects.Box(batch, current_cell))
        elif arr[current_cell] == 1:
            # player = GameObjects.Player(row, column, None)
            player.move(current_cell)

window = pyglet.window.Window(width=(CELL_SIZE * 10), height=(CELL_SIZE * 10), caption="Gecko Soko")
fps_display = pyglet.window.FPSDisplay(window)
fps_display.label.y = 0

label = pyglet.text.Label('[{0}, {1}]'.format(player.row, player.column),
                          font_name='Times New Roman',
                          font_size=36,
                          x=410, y=10,
                          anchor_x='right', anchor_y='baseline')


def show_coords():
    label.text = '[{0}, {1}]'.format(player.row, player.column)


@window.event
def on_key_press(symbol, modifiers):
    c = player.column
    r = player.row
    if symbol == key.UP:  # координаты по y обращены для удобства
        next_pos = [player.row - 1, player.column]
        if arr[r - 1][c] != 3:  # TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            player.move(next_pos)
            show_coords()
    if symbol == key.DOWN:  # координаты по y обращены для удобства
        next_pos = [player.row + 1, player.column]
        if arr[r + 1][c] != 3:  # TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            player.move(next_pos)
            show_coords()
    if symbol == key.LEFT:
        next_pos = [player.row, player.column - 1]
        if arr[r][c - 1] != 3:  # TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            player.move(next_pos)
            show_coords()
    if symbol == key.RIGHT:
        next_pos = [player.row, player.column + 1]
        if arr[r][c + 1] != 3:  # TODO: сделать проверку возможности хода (кирпич, ящик, а за ним что-нибудь)
            player.move(next_pos)
            show_coords()


@window.event
def on_draw():
    window.clear()
    batch.draw()
    layer2.draw()
    player.draw()
    label.draw()
    fps_display.draw()


def update(dt):
    pass


pyglet.clock.set_fps_limit(60)
pyglet.clock.schedule_interval(update, 1 / 120)

pyglet.app.run()
