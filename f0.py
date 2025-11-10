from __builtins__ import *


def till_if_not_till():
    if get_ground_type() != Grounds.Soil:
        till()

def goto_coord(x, y):
    if(x > get_world_size()):
        quick_print("x will be reduced to ", x%get_world_size(), " bc it is out of bounds")
    if(y > get_world_size()):
        quick_print("y will be reduced to ", y%get_world_size(), " bc it is out of bounds")

    # quick_print("goto", x, y)
    step = 1
    if(get_pos_x() > x):
        step = -1
    for i in range(get_pos_x(), x%get_world_size(), step):
        # quick_print(get_pos_x(), "wanted x :", x)
        if(step == 1):
            move(East)
        else:
            move(West)

    step = 1
    if(get_pos_y() > y):
        step = -1
    for i in range(get_pos_y(), y%get_world_size(), step):
        # quick_print(get_pos_y(), "wanted y :", y)

        if(step == 1):
            move(North)
        else:
            move(South)

def get_z_pattern_list(start_x, start_y, size):
    unchecked_list = []

    # z style patern to opti
    for i in range(start_y, start_y +size):
        dir = i % 2
        if (dir == 0):
            start = 0
            end = size
            step = 1
        else:
            start = size - 1
            end = -1
            step = -1
        for j in range(start_x+start, start_x+end, step):
            # quick_print((i,j))
            unchecked_list.append((j, i))
    return unchecked_list