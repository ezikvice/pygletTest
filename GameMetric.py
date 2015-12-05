__author__ = 'Dmitry'

#
# class GameMetric:

CELL_SIZE = 64
ROWS_NUM = 9
COLUMNS_NUM = 9
WIN_WIDTH = 640
WIN_HEIGHT = 640 - CELL_SIZE


def move(obj, column, row):
    obj.x = column * CELL_SIZE
    obj.y = row * CELL_SIZE
    obj.column = column
    obj.row = row


def can_move(arr, column, row):
    if 3 == arr[column][row]:
        return False
    return True
