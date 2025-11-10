import f0
from __builtins__ import *

def harvest_sunfower(world_used, next_entity):
	height_check = sense_grow_sunfower(world_used)
	f0.goto_coord(world_used[0]+(world_used[2]/2), world_used[1]+(world_used[2]/2))

	for keys in height_check:
		for location in height_check[keys]:
			f0.wait_for_any_drone()
			f0.spawn_drone_with_args(f0.plan_safe_location, [next_entity, location])
		f0.wait_for_every_drone()

def sense_grow_sunfower(world_used):
	grow_index = f0.get_grow_index_sunflower()
	for location in f0.get_cross_pattern_list(world_used):
		f0.goto_coord_loc(location[0])
		if(get_entity_type() == Entities.Sunflower):
			grow_index[measure()].append(location[0])
		for direction in location[1]:
			grow_index[measure(direction)].append(f0.get_location_from_location_and_dir(location[0], direction))
	return grow_index


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


def none_safe(item):
	if item == None:
		return -1
	return item

def sense_grow_cactus(world_used):
	grow_index = f0.get_grow_index_cactus(world_used)
	for location in f0.get_cross_pattern_list(world_used):
		f0.goto_coord_loc(location[0])
		grow_index[location[0][0]][location[0][1]]= measure()

		for direction in location[1]:
			measured_location = f0.get_location_from_location_and_dir(location[0], direction)
			grow_index[measured_location[0]][measured_location[1]] = measure(direction)

	return grow_index

def is_vertically_sorted(list):
	isgood = True
	for i in range(len(list)):
		for j in range(len(list) - 1):
			if none_safe(list[j][i]) > none_safe(list[j+1][i]):
				isgood = False
	return isgood


def is_list_sorted(list):
	isgood = True
	for i in range(len(list)-1):
		if none_safe(list[i]) > none_safe(list[i+1]):
			isgood = False
	return isgood
def is_cactus_sorted(cac_list):
	isok = True
	for list in cac_list:
		if(not is_list_sorted(list)):
			isok = False
	return isok and is_vertically_sorted(cac_list)