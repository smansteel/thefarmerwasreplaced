import f0, f3
from __builtins__ import *


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
	Items.Gold: Entities.Treasure,
	Items.Weird_Substance: Entities.Pumpkin,
}


to_unlock = {
	Unlocks.Pumpkins: 10,
	Unlocks.Cactus: 6

}


def item_for_next_unlock():
	for unlock_item in to_unlock:
		lvl_to_unlock = to_unlock[unlock_item]
		if num_unlocked(unlock_item) != lvl_to_unlock:
			ucost = get_cost(unlock_item)
			for items in ucost:
				number = ucost[items]
				if num_items(items) < number:
					return items
			unlock(unlock_item)
	return None


def can_afford_full_farm_plant(entity):
	for item in get_cost(entity):
		number = get_cost(entity)[item]
		if num_items(item) <  world_used[2] ** 2 * number:
			quick_print("canno afford, missing ", item, " reeqruied : ", world_used[2] ** 2 * number  , "nb ",num_items(item) )
			return can_afford_full_farm_plant(map_items_entity[item])
	return entity


def get_next_farm(item):
	return can_afford_full_farm_plant(map_items_entity[item])


nd = 4
max_drone = 4
sqrt_max = 2
dronewsize = get_world_size()/(sqrt_max)

world_used = (0,0,get_world_size())
last_plant = None
current_plant = None
while True:
	rq_to_unlock = item_for_next_unlock()
	if rq_to_unlock == None:
		break
	current_plant = get_next_farm(rq_to_unlock)
	f3.optimized_harvest(world_used, last_plant, current_plant)
	last_plant = current_plant






