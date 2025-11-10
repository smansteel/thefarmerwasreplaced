import f0, f1
import f2
from __builtins__ import *
from f0 import goto_coord

xsize = get_world_size()

# reset
# clear()
harvest()
f0.goto_coord(0,0)
quick_print("")
quick_print("")
quick_print("")
quick_print("")
quick_print("")
quick_print("")

quick_print("--- New Run ----")

zone_x, zone_y = 0,0
size = get_world_size()


map_items_entity = {
	Items.Carrot: Entities.Carrot,
	Items.Pumpkin: Entities.Pumpkin,
	Items.Hay: Entities.Grass,
	Items.Wood: Entities.Bush,
	Items.Cactus: Entities.Cactus,
	Items.Gold: Entities.Treasure
}

def farm_missing_or_farm_missing(resource, x_start, y_start,zone):
	goto_coord(x_start, y_start)

	any_needed = False
	for needed in f0.check_resources_to_plant(resource):
		# print("i need ", needed)
		farm_missing_or_farm_missing(map_items_entity[needed], x_start, y_start, zone)
		any_needed = True
	if(any_needed):
		farm_missing_or_farm_missing(resource, x_start, y_start, zone)
		return
	if(num_items(Items.Power) < 500 and resource != Entities.Sunflower):
		farm_missing_or_farm_missing(Entities.Sunflower, x_start, y_start, zone)

	if(resource == Entities.Pumpkin):
		f1.check_on_pumpkins(x_start, y_start, zone)
	elif(resource == Entities.Cactus):
		f1.check_on_cactus(y_start, y_start, zone)
	# elif(resource == Entities.Treasure):
	#     harvest()
	#     plant(Entities.Bush)
	#     substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	#     use_item(Items.Weird_Substance, substance)
	#
	#     f2.solve_maze()
	else:
		f0.plant_in_list(f0.get_z_pattern_list(x_start, y_start, zone), resource)


next_unlocks = [
	Unlocks.Pumpkins,
	Unlocks.Cactus,
	Unlocks.Carrots

]

# harvest()
# while True:
#     plant(Entities.Bush)
#     substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
#     use_item(Items.Weird_Substance, substance)
#
#     f2.solve_maze()

nd = 4
max_drone = 4
sqrt_max = 2
dronewsize = get_world_size()/(sqrt_max)
quick_print(dronewsize)


def init():
	x_start, y_start = get_pos_x(), get_pos_y()

	for unlock_upgrade in next_unlocks:
		cost = get_cost(unlock_upgrade)
		for item in cost:
			if (num_items(item) > cost[item]):
				unlock(unlock_upgrade)
				break
			else:
				farm_missing_or_farm_missing(map_items_entity[item],x_start, y_start, dronewsize)
active_drones = []
while True:
	quick_print(f0.get_z_pattern_list(0,0, sqrt_max))
	for coords in f0.get_z_pattern_list(0,0, sqrt_max):
		coords = (coords[0]*dronewsize, coords[1]*dronewsize)
		print(coords, dronewsize)
		f0.goto_coord(coords[0], coords[1])
		created = spawn_drone(init)
		active_drones.append(created)
		if not created:
			print("not spawned")
	for drones in active_drones:
		wait_for(drones)
