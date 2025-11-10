import f0, f1
import f2
from __builtins__ import *
from f0 import goto_coord

xsize = get_world_size()

# reset
clear()
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
	Items.Wood: Entities.Bush
}

def farm_missing_or_farm_missing(resource):

	any_needed = False
	for needed in f0.check_resources_to_plant(resource):
		print("i need ", needed)
		farm_missing_or_farm_missing(map_items_entity[needed])
		any_needed = True
	if(any_needed):
		farm_missing_or_farm_missing(resource)
		return
	if(num_items(Items.Power) < 500 and resource != Entities.Sunflower):
		farm_missing_or_farm_missing(Entities.Sunflower)

	if(resource == Entities.Pumpkin):
		f1.check_on_pumpkins(zone_x, zone_y, size)
	else:
		f0.plant_in_list(f0.get_z_pattern_list(zone_x, zone_y, size), resource)


next_unlocks = [
	Unlocks.Pumpkins,
	Unlocks.Carrots,
	Unlocks.Trees,
	Unlocks.Cactus

]


while True:
	if(xsize != get_world_size()):
		break
	for unlock_upgrade in next_unlocks:
		cost = get_cost(unlock_upgrade)
		for item in cost:
			if(num_items(item) > cost[item]):
				unlock(unlock_upgrade)
				break
			else:
				farm_missing_or_farm_missing(map_items_entity[item])
	# 	print("cost", cost)
	#     if(cost < )
	# farm_missing_or_farm_missing(Entities.Pumpkin)
    # print("new poly cycle")
    # f2.polyculture((0,0), Entities.Bush)