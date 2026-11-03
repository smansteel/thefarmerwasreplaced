from __builtins__ import *


def m_lootMap(itemOrEntity):
	if itemOrEntity == Entities.Carrot:
		return Items.Carrot
	if itemOrEntity == Items.Carrot:
		return Items.Carrot
	if itemOrEntity == Items.Wood:
		return Entities.Bush

def m_goto(pos_x, pos_y):
	while get_pos_x() != pos_x:
		if pos_x - get_pos_x() > 0:
			move(East)
		else:
			move(West)
	while get_pos_y() != pos_y:
		if pos_y - get_pos_y() > 0:
			move(North)
		else:
			move(South)

	print("at requestes coords " + str(get_pos_x()) + " " + str(get_pos_y()))
	do_a_flip()
