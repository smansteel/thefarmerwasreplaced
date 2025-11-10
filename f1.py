from __builtins__ import *
import f0
def check_on_pumpkins(pumpkin_zone_x, pumpkin_zone_y, pumpkin_size):
	rq_stop = False
	plant_locations = f0.get_z_pattern_list(0, 0, pumpkin_size)
	#plant

	for location in plant_locations:
		f0.goto_coord(pumpkin_zone_x + location[0], pumpkin_zone_x + location[1])
		harvest()
		f0.till_if_not_till()
		plant(Entities.Pumpkin)


	# quick_print(uncked)
	# check
	to_come_back = []

	for location in plant_locations:
		f0.goto_coord(pumpkin_zone_x + location[0], pumpkin_zone_y + location[1])

		if (get_entity_type() != Entities.Pumpkin):
			plant(Entities.Pumpkin)
		while (get_entity_type() == Entities.Dead_Pumpkin or not can_harvest()):
			plant(Entities.Pumpkin)
			if (num_items(Items.Fertilizer) == 0):
				to_come_back.append((pumpkin_zone_x + location[0], pumpkin_zone_y + location[1]))
			else:
				use_item(Items.Fertilizer)

	while len(to_come_back) != 0 :
		for item in to_come_back:
			f0.goto_coord(item[0], item[1])
			if (get_entity_type() != Entities.Pumpkin):
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
				to_come_back.remove(item)

	f0.goto_coord(pumpkin_zone_x, pumpkin_zone_x)
	harvest()
