from __builtins__ import *


def till_if_not_till():
	if get_ground_type() != Grounds.Soil:
		till()

def goto_coord(x, y):
	if(x > get_world_size()):
		quick_print("x will be reduced to ", x%get_world_size(), " bc it is out of bounds")
	if(y > get_world_size()):
		quick_print("y will be reduced to ", y%get_world_size(), " bc it is out of bounds")


	step = 1
	if(get_pos_x() > x):
		step = -1
	for i in range(get_pos_x(), x%get_world_size(), step):
		# quick_print(get_pos_x(), "wanted x :", x)
		if(step == 1):
			move(East)
		else:
			move(West)

	step = 1
	if(get_pos_y() > y):
		step = -1
	for i in range(get_pos_y(), y%get_world_size(), step):
		# quick_print(get_pos_y(), "wanted y :", y)

		if(step == 1):
			move(North)
		else:
			move(South)


