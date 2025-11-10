from __builtins__ import *
import f0
def check_on_pumpkins(pumpkin_zone_x, pumpkin_zone_y, pumpkin_size):
    rq_stop = False

    #plant
    for i in range(0, pumpkin_size):
        dir = i % 2
        if (dir == 0):
            start = 0
            end = pumpkin_size
            step = 1
        else:
            start = pumpkin_size - 1
            end = -1
            step = -1
        for j in range(start, end, step):
            f0.goto_coord(pumpkin_zone_x + j, pumpkin_zone_x + i)
            f0.till_if_not_till()
            plant(Entities.Pumpkin)
    # check
    while(not rq_stop):
        all_pumpkin_ok = True
        uncked = init_unchecked_list(pumpkin_size)

        for item in uncked:
            f0.goto_coord(pumpkin_zone_x + item[0], pumpkin_zone_x + item[1])
            if (not can_harvest()):
                quick_print("not can_harvest", i, j)
                all_pumpkin_ok = False
                plant(Entities.Pumpkin)
            else:
                uncked.remove(item)
        if(all_pumpkin_ok):
            rq_stop = True
    f0.goto_coord(pumpkin_zone_x, pumpkin_zone_x)
    harvest()


def init_unchecked_list(size):
    unchecked_list = []

    # z style patern to opti
    for i in range(0, size):
        dir = i % 2
        if (dir == 0):
            start = 0
            end = size
            step = 1
        else:
            start = size - 1
            end = -1
            step = -1
        for j in range(start, end, step):
            unchecked_list.append((i,j))
    return unchecked_list
