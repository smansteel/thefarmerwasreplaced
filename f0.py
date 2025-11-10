from __builtins__ import *

directions = [
	North,
	South,
	East,
	West
]

opp = {
	North: South,
	South: North,
	East: West,
	West: East
}

def till_if_not_till():
	if get_ground_type() != Grounds.Soil:
		till()
def force_till():
	if get_ground_type() != Grounds.Soil:
		till()
	else:
		till()
		till()
def untill_if_till():
	if get_ground_type() == Grounds.Soil:
		till()

def no_oob(coord):
	return coord % get_world_size()

# 1, 18         0, 0, 22
def is_oob(location, wu):
	return location[0]< wu[0] or location[0]>= wu[0]+wu[2] or location[1]< wu[1] or location[1]>= wu[1]+wu[2]

def goto_coord_loc(lcoation):
	return goto_coord(lcoation[0], lcoation[1])

def goto_coord(x, y):
	if(x >= get_world_size()):
		quick_print("x will be reduced to ", x%get_world_size(), " bc it is out of bounds")
	if(y >= get_world_size()):
		quick_print("y will be reduced to ", y%get_world_size(), " bc it is out of bounds")



	x=x%get_world_size()
	y = y % get_world_size()

	if(x < get_pos_x()):
		if(x < (get_world_size()/4) and get_pos_x() > (3*get_world_size()/4)):
			# print("case 1")
			for i in range(0, get_world_size()-get_pos_x()+x):
				move(East)
		else:
			for i in range(0, get_pos_x()-x):
				move(West)
	else:
		if(x > (3*get_world_size()/4) and get_pos_x() < (get_world_size()/4)):
			# print("case 3")
			for i in range(0, get_pos_x()+(get_world_size()-x)):
				move(West)
		else:
			for i in range(0, x-get_pos_x()):
				move(East)



	if(y < get_pos_y()):
		if(y < get_world_size()/4 and get_pos_y() > 3*get_world_size()/4):
			# print("case 1")
			for i in range(0, get_world_size()-get_pos_y()+y):
				move(North)
		else:
			for i in range(0, get_pos_y()-y):
				move(South)
	else:
		if(y > 3*get_world_size()/4 and get_pos_y() < get_world_size()/4):
			# print("case 3")
			for i in range(0, get_pos_y()+(get_world_size()-y)):
				move(South)
		else:
			for i in range(0, y-get_pos_y()):
				move(North)

def get_z_pattern_list_wu(world_used):
	return get_z_pattern_list(world_used[0], world_used[1], world_used[2])

def is_direction_oob(location, direction, wu):
	return is_oob(get_location_from_location_and_dir(location, direction), wu)

cross_pattern_cache = {

}

def get_cross_pattern_list(wu):
	if(wu in cross_pattern_cache):
		return cross_pattern_cache[wu]
	list_pattern = []
	quick_print("generating map")
	for i in range(-1, wu[2]+1):
		for j in range(-1, wu[2]+1):
			center_oob = is_oob((i,j), wu)

			if not (j + i*3)%5 == 0:
				continue
			valid_dir = []
			for direction in directions:
				if(not is_direction_oob((i,j), direction, wu)):
					valid_dir.append(direction)
			if(center_oob and len(valid_dir)>0):
				list_pattern.append((get_location_from_location_and_dir((i,j), valid_dir[0]), [])) # cannot have center oob and mpre than one direction
			elif(not center_oob):
				list_pattern.append(((i,j), valid_dir))
	quick_print("finish generating map")
	cross_pattern_cache[wu] = list_pattern
	return list_pattern



def get_z_pattern_list(start_x, start_y, size, every_lines=1):
	list_pattern = []

	# z style patern to opti
	for i in range(start_y, start_y +size, every_lines):
		# quick_print(i)
		dir = i % 2
		if (dir == 0):
			start = 0
			end = size
			step = 1
		else:
			start = size - 1
			end = -1
			step = -1
		for j in range(start_x+start, start_x+end, step):
			# quick_print("    ", j)
			# quick_print((i,j))
			list_pattern.append((j, i))
	return list_pattern
def plant_safe_harvest(entity):
	while(not can_harvest() and get_entity_type() not in (None, Entities.Dead_Pumpkin)):
		do_a_flip()
	plant_safe(entity)

def plan_safe_location(entity, location):
	goto_coord_loc(location)
	plant_safe(entity)

def harvest_min_lvl_plant_safe(entity, min_lvl):
	if(measure() != None and measure()>=min_lvl):
		plant_safe(entity)


def drone_start_row(func, args):
	last_pos_x, last_pos_y = -1,-1
	while get_pos_x() > last_pos_x or get_pos_y() > last_pos_y:
		call_func_with_args_as_list(func, args)

		last_pos_x, last_pos_y = get_pos_x(), get_pos_y()
		move(East)


def plant_safe(entity):
	harvest()
	while(get_water() < .3 and not num_items(Items.Water) ==0):
		use_item(Items.Water)

	if(entity == Entities.Grass):
		untill_if_till()
		# plant(entity)
	elif(entity == Entities.Pumpkin):
		till_if_not_till()
		plant(entity)
	elif(entity == Entities.Carrot):
		till_if_not_till()
		plant(entity)
	elif(entity == Entities.Sunflower):
		till_if_not_till()
		plant(entity)
	elif(entity == Entities.Bush):
		untill_if_till()
		plant(entity)
	elif(entity == Entities.Cactus):
		till_if_not_till()
		plant(entity)
	elif(entity == Entities.Tree):
		untill_if_till()
		if(get_pos_x()%2 == 0 and get_pos_y()%2 == 0):
			plant(Entities.Tree)
		elif(get_pos_x()%2 == 1 and get_pos_y()%2 == 1):
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
	else:
		quick_print("seed cannot be planted, not implemented")


def plant_safe_in_list_random(entity_list):
	plant_safe(entity_list[(random()*len(entity_list))])



def plant_in_list(list, entity):
	for item in list:
		goto_coord(item[0], item[1])
		plant_safe(entity)

def plant_to_dir(max_x, direction,  entity):
	while get_pos_x() < max_x-1:
		plant_safe_harvest(entity)
		move(direction)
	plant_safe_harvest(entity)
	move(direction)

def plant_in_list_in_list_random(list, entity_list):
	for item in list:
		goto_coord(item[0], item[1])
		plant_safe_in_list_random(entity_list)


def harvest_in_list(list):
	for item in list:
		goto_coord(item[0], item[1])
		harvest()

def harvest_if_ready_and_plant_back(list):
	for item in list:
		goto_coord(item[0], item[1])
		if(can_harvest()):
			entt = get_entity_type()
			harvest()
			plant(entt)


def check_resources_to_plant(to_plant):
	all_ok = []
	for item in get_cost(to_plant):
		if(num_items(item)< get_world_size()**2*get_cost(to_plant)[item]*1.3):
			all_ok.append(item)
	return all_ok

def call_func_with_args_as_list(function, args):
	if (len(args) == 0):
		function()
	elif (len(args) == 1):
		function(args[0])
	elif (len(args) == 2):
		function(args[0], args[1])
	elif (len(args) == 3):
		function(args[0], args[1], args[2])
	elif (len(args) == 4):
		function(args[0], args[1], args[2], args[3])
	elif (len(args) == 5):
		function(args[0], args[1], args[2], args[3], args[4])
	elif (len(args) == 6):
		function(args[0], args[1], args[2], args[3], args[4], args[5])
	elif (len(args) == 7):
		function(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
	elif (len(args) == 8):
		function(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
	else:
		print("Atrocité tellement atroce qu'elle fait exploser ton programme")
		return

def spawn_drone_with_args(function, args):
	def rt_func():
		return call_func_with_args_as_list(function, args)
	return spawn_drone(rt_func)


def wait_for_any_drone():
	while(num_drones() == max_drones()):
		random()

def wait_for_every_drone():
	while(num_drones() != 1):
		random()


def get_grow_index_sunflower():
	grow_index = {}
	for i in [15, 14, 13, 12, 11, 10, 9, 8, 7]:
		grow_index[i] = []
	return grow_index
def get_grow_index_cactus(world_used):
	rlist = []
	for col in range(0, world_used[2]):
		lllist = []
		for row in range(0, world_used[2]):
			lllist.append(" ")
		rlist.append(lllist)
	return rlist

def get_location_from_location_and_dir(location, direction):
	mv = (0,0)
	if(direction == North):
		mv = (0,1)
	elif(direction == South):
		mv = (0,-1)
	elif(direction == East):
		mv = (1,0)
	elif(direction == West):
		mv = (-1,0)
	return location[0] + mv[0], location[1] + mv[1]