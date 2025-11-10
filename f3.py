from __builtins__ import *
import f0, f2, f4

need_global_harvest = [Entities.Pumpkin, Entities.Cactus, Entities.Treasure, Entities.Sunflower]

def classic_plant(world_used, next_resource):
	is_treasure = False
	if(next_resource == Entities.Treasure):
		is_treasure = True
		next_resource = Entities.Grass
	ongoing_drones = {}

	for row in range(0, world_used[2]):
		if (row in ongoing_drones and ongoing_drones[row] != None):
			wait_for(ongoing_drones[row])
		f0.wait_for_any_drone()
		drone = f0.spawn_drone_with_args(f0.plant_to_dir, [world_used[0] + world_used[2], East, next_resource])
		ongoing_drones[row] = (drone)
		move(North)

		f0.wait_for_every_drone()
	if(is_treasure):
		f0.goto_coord(world_used[0], world_used[1])
		f0.plant_safe(Entities.Bush)
		substance = world_used[2] * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
		use_item(Items.Weird_Substance, substance)



def optimized_harvest(world_used, resource, next_resource):
	# f0.goto_coord(world_used[0], world_used[1])
	if(resource == None or resource not in need_global_harvest):
		classic_plant(world_used, next_resource)

		return
	elif(resource == Entities.Sunflower):
		f4.harvest_sunfower(world_used, next_resource)
	elif(resource == Entities.Cactus):
		f4.harvest_cactus(world_used)
	elif(resource == Entities.Treasure):
		f2.solve_maze()
		classic_plant(world_used, next_resource)




