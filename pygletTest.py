import pyglet
from pyglet.window import key
import numpy as np
import GameObjects
import configparser
from GameMetric import *

__author__ = 'Dmitry'

# TODO: сделать нормальный расчет координат. сейчас неправильно считаются

# TODO: загружать поле из файла
# TODO: сделать загрузку из нескольких массивов на каждый объект свой массив
arr = np.array([[3, 3, 3, 3, 3, 3, 3, 3, 2],
                [3, 0, 0, 0, 0, 0, 0, 3, 2],
                [3, 0, 1, 0, 0, 0, 0, 3, 2],
                [3, 0, 4, 0, 0, 10, 0, 3, 2],
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

trees = []
bricks = []
boxes = []
box_targets = []

current_cell = 0, 0

player = GameObjects.Player(None, current_cell)
# player.image.anchor_x = 0
# player.image.anchor_y = 0

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
            player.move(current_cell)  # работает только потому, что изначально у игрока позиция 0,0

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


def can_move(obj, direction):
    # проверяем не кирпич ли это
    next_cell = n.add([obj.row, obj.column], direction)
    next_cell.tolist()
    r, c = next_cell
    if get_obj_by_coords(bricks, r, c):
        return False
    else:
        # проверяем, если это ящик, то что за ним
        old_r = r
        old_c = c
        if get_obj_by_coords(boxes, r, c):
            next_cell = n.add(next_cell, direction)
            next_cell.tolist()
            r, c = next_cell
            if get_obj_by_coords(boxes, r, c) or get_obj_by_coords(bricks, r, c):
                return False
            else:
                box = get_obj_by_coords(boxes, old_r, old_c)
                box.move(direction)
    return True


def get_obj_by_coords(objects, r, c):
    for obj in objects:
        if obj.row == r and obj.column == c:
            return obj


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:  # координаты по y обращены для удобства
        direction = [-1, 0]
        if can_move(player, direction):
            player.image = player.views['up']
            player.move(direction)
        show_coords()
    if symbol == key.DOWN:  # координаты по y обращены для удобства
        direction = [1, 0]
        if can_move(player, direction):
            player.image = player.views['down']
            player.move(direction)
        show_coords()
    if symbol == key.LEFT:
        direction = [0, -1]
        if can_move(player, direction):
            player.image = player.views['left']
            player.move(direction)
        show_coords()
    if symbol == key.RIGHT:
        direction = [0, 1]
        if can_move(player, direction):
            player.image = player.views['right']
            player.move(direction)
        show_coords()
    if symbol == key.M:
        player.music.pause()
    if symbol == key.P:
        player.music.play()


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
