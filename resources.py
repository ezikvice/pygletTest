import pyglet.resource as res

res.path = ["res"]
res.reindex()

brick = res.image("bricksx64.png")
# brick = res.image("brick-wall.png")
tree = res.image("beech.png")
grass = res.image("wheat.png")
player = res.image("gecko.png")

