import pyglet.resource as res

res.path = ["res"]
res.reindex()

brick = res.image("bricks3.png")
# brick = res.image("brick-wall.png")
tree = res.image("beech.png")
pinetree = res.image("pine-tree2.png")
box = res.image("wooden-crate3.png")
player = res.image("gecko2.png")
target = res.image("boxtarget.png")
