import pyglet.resource as res

res.path = ["res"]
res.reindex()

brick = res.image("bricks3.png")
# brick = res.image("brick-wall.png")
tree = res.image("beech.png")
pinetree = res.image("pine-tree2.png")
box = res.image("wooden-crate3.png")
player = res.image("gecko4.png")
player_down = res.image("gecko4.png", rotate=180)
player_left = res.image("gecko4.png", rotate=270)
player_right = res.image("gecko4.png", rotate=90)
target = res.image("boxtarget.png")
