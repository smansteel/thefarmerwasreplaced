import f0
from __builtins__ import *
from f0 import goto_coord


def harvest_sunfower(world_used, next_entity):
	f0.wait_for_every_drone()

	for min_lvl in [15, 14, 13, 12, 11, 10, 9, 8, 7]:
		f0.goto_coord(world_used[0], world_used[1])
		for rows in range(0, world_used[2]):
			f0.wait_for_any_drone()
			f0.spawn_drone_with_args(f0.drone_start_row, [f0.harvest_min_lvl_plant_safe, [next_entity, min_lvl]])
			move(North)
		f0.wait_for_every_drone()

# def sense_grow_sunfower(world_used):
# 	grow_index = f0.get_grow_index_sunflower()
# 	for location in f0.get_z_pattern_list(world_used[0], world_used[1], world_used[2], 3):
# 		f0.goto_coord_loc(location)
# 		grow_index[measure()].append(location)
# 		if(not f0.get_location_from_location_and_dir(location, South)[1]< world_used[1]):
# 				grow_index[measure(South)].append(f0.get_location_from_location_and_dir(location, South))
# 		if (not f0.get_location_from_location_and_dir(location, North)[1] > world_used[0] + world_used[2]):
# 			grow_index[measure(North)].append(f0.get_location_from_location_and_dir(location, North))
#
# 	return grow_index


def row_or_line_sort_until_world(world_used, isrow):
	last_pos_x, last_pos_y = -1,-1
	while get_pos_x() > last_pos_x or get_pos_y() > last_pos_y:

		if measure(North) != None and measure() - measure(North) > 0 and world_used[2] - 1 != get_pos_y():
			swap(North)
		if measure(East) != None and measure() - measure(East) > 0 and world_used[2] - 1 != get_pos_x():
			swap(East)
		if measure(South) != None and measure() - measure(South) < 0 != get_pos_y():
			swap(South)
		if measure(West) != None and measure() - measure(West) < 0 != get_pos_x():
			swap(West)

		last_pos_x, last_pos_y = get_pos_x(), get_pos_y()


		if (isrow):
			move(East)
		else:
			move(North)



def gigasort(world_used, tries):
	f0.goto_coord(world_used[0], world_used[1])
	for sort in range(0, tries):
		if(sort%2 ==0 ):
			hz = True
		else:
			hz = False
		for row in range(0, world_used[2]):
			f0.wait_for_any_drone()
			if(not f0.spawn_drone_with_args(row_or_line_sort_until_world, [world_used, hz])):
				quick_print("drone not spawned", world_used)
			if(hz):
				move(North)
			else:
				move(East)
	f0.wait_for_every_drone()


def harvest_cactus(world_used):
	gigasort(world_used, world_used[2]*0.6)
	f0.goto_coord(world_used[0], world_used[1])
	harvest()

def row_check_pumpkins():
	last_pos_x, last_pos_y = -1,-1
	while get_pos_x() > last_pos_x or get_pos_y() > last_pos_y:

		if (get_entity_type() != Entities.Pumpkin):
			plant(Entities.Pumpkin)
		while (get_entity_type() == Entities.Dead_Pumpkin or not can_harvest()):
			plant(Entities.Pumpkin)
			use_item(Items.Fertilizer)

		last_pos_x, last_pos_y = get_pos_x(), get_pos_y()
		move(East)


def dispatch_pumpkins(world_used):
	f0.goto_coord(world_used[0], world_used[1])
	for sort in range(0, world_used[2]):
		f0.wait_for_any_drone()
		if(not f0.spawn_drone_with_args(row_check_pumpkins, [])):
			quick_print("drone not spawned", world_used)
		move(North)

	f0.wait_for_every_drone()

def harvest_pumpkin(world_used):
	dispatch_pumpkins(world_used)
	f0.goto_coord(world_used[0], world_used[1])
	harvest()