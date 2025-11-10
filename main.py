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
	Items.Gold: Entities.Treasure
}


nd = 4
max_drone = 4
sqrt_max = 2
dronewsize = get_world_size()/(sqrt_max)

world_used = (0,0,get_world_size())
while True:
	f3.optimized_harvest(world_used, Entities.Bush, Entities.Cactus)
	f3.optimized_harvest(world_used, Entities.Cactus, Entities.Pumpkin)
	f3.optimized_harvest(world_used, Entities.Pumpkin, Entities.Bush)

