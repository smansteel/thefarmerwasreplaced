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

def compute_swaps():
	print('not implemented')

def harvest_cactus(world_used):
	height_check = sense_grow_cactus(world_used)

	f0.goto_coord(world_used[0]+(world_used[2]/2), world_used[1]+(world_used[2]/2))
	# compute_swaps()

	print("sorted ?", is_cactus_sorted(height_check))

	for linees in height_check:
		quick_print(linees)

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