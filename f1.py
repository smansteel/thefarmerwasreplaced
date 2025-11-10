from __builtins__ import *
import f0
from f0 import untill_if_till


def check_on_pumpkins(pumpkin_zone_x, pumpkin_zone_y, pumpkin_size):
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

def check_on_cactus(zone_x, zone_y, size):
    plant_locations = f0.get_z_pattern_list(0, 0, size)
    # plant

    for location in plant_locations:
        f0.goto_coord(zone_x + location[0], zone_x + location[1])
        harvest()
        f0.till_if_not_till()
        plant(Entities.Cactus)

    # quick_print(uncked)
    # check
    to_come_back = []
    req_stop = False
    # ok_cactus = []

    count = 0
    while not req_stop:
        count +=1
        # if(count > 5):
        #     plant_locations
        no_issue = True

        for location in plant_locations:
            # if(location not in ok_cactus):

                f0.goto_coord(zone_x + location[0], zone_y + location[1])
                if(measure(North) != None and measure() - measure(North) > 0 and size-1 != get_pos_y()):
                    no_issue = False
                    swap(North)
                if (measure(East) != None and measure() - measure(East) > 0  and size-1 != get_pos_x()):
                    no_issue = False
                    swap(East)
                if (measure(South) != None and measure() - measure(South) < 0  and 0 != get_pos_y()):
                    no_issue = False
                    swap(South)
                if (measure(West) != None and measure() - measure(West) < 0  and 0 != get_pos_x()):
                    no_issue = False
                    swap(West)

        if(no_issue):
            req_stop = True

    f0.goto_coord(zone_x, zone_y)
    harvest()