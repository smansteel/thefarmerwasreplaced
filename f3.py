from __builtins__ import *
import f0
import f4
from f0 import goto_coord

need_global_harvest = [Entities.Pumpkin, Entities.Cactus, Entities.Treasure, Entities.Sunflower]


def optimized_harvest(world_used, resource, next_resource):
	goto_coord(world_used[0], world_used[1])
	ongoing_drones = {}
	if(resource == None or resource not in need_global_harvest):
		for row in range(0,world_used[2]):
			if(row in ongoing_drones and ongoing_drones[row] != None):
				wait_for(ongoing_drones[row])
			f0.wait_for_any_drone()
			drone = f0.spawn_drone_with_args(f0.plant_to_dir,[world_used[0]+world_used[2], East, next_resource])
			ongoing_drones[row]=(drone)
			move(North)

		f0.wait_for_every_drone()
		return
	elif(resource == Entities.Sunflower):
		f4.harvest_sunfower(world_used, next_resource)




