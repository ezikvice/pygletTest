import pyglet
from pyglet.window import key
import resources as res
from pyglet import clock

__author__ = 'Dmitry'

pyglet.resource.path = ["res"]
pyglet.resource.reindex()

tree = pyglet.sprite.Sprite(res.player, 110, 110)
# tree_down = pyglet.sprite.Sprite()

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
