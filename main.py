import f0, f1
from __builtins__ import *

xsize = get_world_size()



plant_map = [
	[Entities.Grass, Entities.Tree, Entities.Carrot, Entities.Carrot, Entities.Tree, Entities.Carrot],
	[Entities.Grass, Entities.Carrot, Entities.Carrot, Entities.Carrot, Entities.Carrot, Entities.Carrot],
	[Entities.Grass, Entities.Tree, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin],
	[Entities.Grass, Entities.Carrot, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin],
	[Entities.Grass, Entities.Tree, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin],
	[Entities.Tree, Entities.Grass, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin, Entities.Pumpkin]
			 ]

def get_plant_type_for_coord(x, y):
	return plant_map[x][y]


def plant_prep(plant_to_plant):
	if(plant_to_plant == Entities.Grass):
		plant(Entities.Grass)
	if(plant_to_plant == Entities.Tree):
		plant(Entities.Tree)
	if(plant_to_plant == Entities.Carrot):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
	if(plant_to_plant == Entities.Pumpkin):
		f0.till_if_not_till()
		plant(Entities.Pumpkin)
def tile_process(plant):
	if(get_water() > 0.1):
		use_item(Items.Water)
	if can_harvest():
		harvest()
		plant_prep(plant)
	elif get_entity_type() == Entities.Dead_Pumpkin:
		harvest()
		plant_prep(plant)
	else:
		plant_prep(plant)

def row_type():
	tile_process(get_plant_type_for_coord(get_pos_x(), get_pos_y()))

# reset
clear()
quick_print("")
quick_print("")
quick_print("")
quick_print("")
quick_print("")
quick_print("")

quick_print("--- New Run ----")

pumpkin_zone_x, pumpkin_zone_y = 0,0
pumpkin_size = 5


# w
while True:
	f1.check_on_pumpkins(pumpkin_zone_x, pumpkin_zone_y, pumpkin_size)


