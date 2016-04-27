import pyglet
import resources as res
from pyglet import clock
import configparser
import numpy as np
import GameObjects
import ast

__author__ = 'Dmitry'

pyglet.resource.path = ["res"]
pyglet.resource.reindex()

# tree = pyglet.sprite.Sprite(res.player, 600, 40)
# tree.image = res.tree
# tree.image.anchor_x = tree.width // 2
# tree.image.anchor_y = tree.height // 2

batch = pyglet.graphics.Batch()


def save_level(filename, game_object):
    # lets create that config file for next time...
    cfgfile = open(filename, 'w')

    cfg = configparser.ConfigParser()
    # add the settings to the structure of the file, and lets write it out...
    cfg.add_section('GameObjects')
    cfg.set('GameObjects', 'trees', ', '.join(str(x.get_position()) for x in game_object.trees))
    cfg.set('GameObjects', 'bricks', ', '.join(str(x.get_position()) for x in game_object.bricks))
    cfg.set('GameObjects', 'boxes', ', '.join(str(x.get_position()) for x in game_object.boxes))
    cfg.set('GameObjects', 'box_targets', ', '.join(str(x.get_position()) for x in game_object.box_targets))
    cfg.set('GameObjects', 'player', str(game_object.player))
    cfg.write(cfgfile)
    cfgfile.close()


def load_level(levelnumber, game_objects):
    opencfg = configparser.ConfigParser()
    opencfg.read("levels/" + levelnumber + ".ini")

    # ast.literal_eval приводит строку к простым типам питона
    # (в данном случае в список позиций - туплу, в которой тупла)
    trees_list = ast.literal_eval(opencfg.get("GameObjects", 'trees'))
    # заполняем массив деревьев с помощью генераторного выражения
    game_objects.trees = [GameObjects.Tree(batch, current_cell) for current_cell in trees_list]

    game_objects.bricks = [GameObjects.Brick(batch, current_cell) for current_cell in
                           ast.literal_eval(opencfg.get("GameObjects", 'bricks'))]
    game_objects.boxes = [GameObjects.Box(batch, current_cell) for current_cell in
                          ast.literal_eval(opencfg.get("GameObjects", 'boxes'))]
    game_objects.box_targets = [GameObjects.BoxTarget(batch, current_cell) for current_cell in
                                ast.literal_eval(opencfg.get("GameObjects", 'box_targets'))]

    return game_objects


class GameObject:
    trees = []
    bricks = []
    boxes = []
    box_targets = []
    player = (1, 2)


ob = GameObject()

load_level("1", ob)
save_level("test.ini", ob)

window = pyglet.window.Window(width=640, height=640, caption="Gecko Soko")


def update(dt):
    # tree.rotation += 100*dt
    pass


clock.schedule(update)


@window.event
def on_draw():
    window.clear()
    # tree.draw()
    batch.draw()


pyglet.app.run()
