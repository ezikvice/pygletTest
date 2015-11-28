import pyglet

pyglet.resource.path = ["res"]
pyglet.resource.reindex()

brick = pyglet.resource.image("bricksx64.png")
player = pyglet.resource.image("gecko.png")

