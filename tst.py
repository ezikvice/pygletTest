import numpy as n


class Obj:
    row = 0
    column = 2


arr = [[1, 2, 0], [1, 1, 1]]
direction = [0, -1]
obj = Obj()


def can_move():
    next_cell = n.add([obj.row, obj.column], direction)
    next_cell.tolist()
    r, c = next_cell
    if arr[r][c] == 3:
        return False
    else:
        next_cell = n.add(next_cell, direction)
        next_cell.tolist()
        r, c = next_cell
        if arr[r][c] == 2 or arr[r][c] == 3:
            return False
    return True


a = can_move()
print(a)
