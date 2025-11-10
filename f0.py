from __builtins__ import *


def till_if_not_till():
    if get_ground_type() != Grounds.Soil:
        till()

def goto_coord(x, y):
    if(x >= get_world_size()):
        quick_print("x will be reduced to ", x%get_world_size(), " bc it is out of bounds")
    if(y >= get_world_size()):
        quick_print("y will be reduced to ", y%get_world_size(), " bc it is out of bounds")

    x=x%get_world_size()


    if(x < get_pos_x()):
        if(x<get_world_size()/4 and get_pos_x() > get_world_size()/4):
            # print("case 1")
            for i in range(0, get_world_size()-get_pos_x()+x):
                move(East)
        else:
            for i in range(0, get_pos_x()-x):
                move(West)
    else:
        if(x>get_world_size()/4 and get_pos_x() < get_world_size()/4):
            # print("case 3")
            for i in range(0, get_pos_x()+(get_world_size()-x)):
                move(West)
        else:
            for i in range(0, x-get_pos_x()):
                move(East)



    if(y < get_pos_y()):
        if(y<get_world_size()/4 and get_pos_y() > get_world_size()/4):
            # print("case 1")
            for i in range(0, get_world_size()-get_pos_y()+y):
                move(North)
        else:
            for i in range(0, get_pos_y()-y):
                move(South)
    else:
        if(y>get_world_size()/4 and get_pos_y() < get_world_size()/4):
            # print("case 3")
            for i in range(0, get_pos_y()+(get_world_size()-y)):
                move(South)
        else:
            for i in range(0, y-get_pos_y()):
                move(North)



def get_z_pattern_list(start_x, start_y, size):
    list_pattern = []

    # z style patern to opti
    for i in range(start_y, start_y +size):
        # quick_print(i)
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
            # quick_print("    ", j)
            # quick_print((i,j))
            list_pattern.append((j, i))
    return list_pattern

def plant_safe(entity):
    if(entity == Entities.Grass):
        plant(Entities.Grass)
    elif(entity == Entities.Pumpkin):
        quick_print("please use dedicated function")
    elif(entity == Entities.Carrot):
        till_if_not_till()
        plant(Entities.Carrot)
    else:
        quick_print("not yet implemented")

def plant_in_list(list, entity):
    for item in list:
        goto_coord(item[0], item[1])
        plant_safe(entity)
def harvest_in_list(list):
    for item in list:
        goto_coord(item[0], item[1])
        harvest()

def harvest_if_ready_and_plant_back(list):
    for item in list:
        goto_coord(item[0], item[1])
        if(can_harvest()):
            entt = get_entity_type()
            harvest()
            plant(entt)