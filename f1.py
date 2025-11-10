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
    uncked = f0.get_z_pattern_list(0,0,pumpkin_size)
    # quick_print(uncked)
    # check
    while(not rq_stop):
        all_pumpkin_ok = True


        for item in uncked:

            f0.goto_coord(pumpkin_zone_x + item[0], pumpkin_zone_y + item[1])
            if (get_entity_type() == Entities.Dead_Pumpkin or not can_harvest()):
                all_pumpkin_ok = False
                plant(Entities.Pumpkin)
                use_item(Items.Fertilizer)
            else:
                quick_print(get_entity_type() == Entities.Dead_Pumpkin, can_harvest())
                quick_print("removing ", item, "when being at ", get_pos_x(), get_pos_y())
                uncked.remove(item)
        if(all_pumpkin_ok):
            rq_stop = True
    f0.goto_coord(pumpkin_zone_x, pumpkin_zone_x)
    harvest()

