import f0
from __builtins__ import *
from f0 import goto_coord, goto_coord_loc


def harvest_sunfower(world_used, next_entity):
	height_check = sense_grow(world_used)
	goto_coord(world_used[0]+(world_used[2]/2), world_used[1]+(world_used[2]/2))

	for keys in height_check:
		for location in height_check[keys]:
			f0.wait_for_any_drone()
			f0.spawn_drone_with_args(f0.plan_safe_location, [next_entity, location])
			f0.wait_for_every_drone()

def sense_grow(world_used):
	grow_index = f0.get_grow_index()
	for location in f0.get_z_pattern_list_wu(world_used):
		f0.goto_coord_loc(location)
		if(get_entity_type() == Entities.Sunflower):
			grow_index[measure()].append(location)
	return grow_index