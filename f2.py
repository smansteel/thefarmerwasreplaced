from __builtins__ import *
import f0

def polyculture(start_point, start_entity):
    path_history = []
    f0.goto_coord(start_point[0], start_point[1])
    f0.plant_safe(start_entity)
    path_history.append((start_point[0], start_point[1]))
    comp = get_companion()
    f0.goto_coord(comp[1][0], comp[1][1])
    f0.plant_safe(comp[0])
    path_history.append((comp[1][0], comp[1][1]))
    comp = get_companion()
    while not comp[1] in path_history:
        f0.goto_coord(comp[1][0], comp[1][1])
        f0.plant_safe(comp[0])
        path_history.append((comp[1][0], comp[1][1]))
        comp = get_companion()

    while len(path_history) != 0:
        coord = path_history.pop(0)
        f0.goto_coord(coord[0], coord[1])
        while(not can_harvest()):
            do_a_flip()
        harvest()