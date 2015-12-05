import pyglet
from pyglet.window import key
import resources as res

__author__ = 'Dmitry'

pyglet.resource.path = ["res"]
pyglet.resource.reindex()

tree = pyglet.sprite.Sprite(res.grass, 0, 0)

window = pyglet.window.Window(width=640, height=640, caption="Gecko Soko")

@window.event
def on_draw():
    window.clear()
    tree.draw()

pyglet.app.run()
