import pyglet.resource as res

res.path = ["res"]
res.reindex()

brick = res.image("bricks3.png")
# brick = res.image("brick-wall.png")
tree = res.image("beech.png")
grass = res.image("pine-tree2.png")
box = res.image("wooden-crate.png")
player = res.image("gecko2.png")

