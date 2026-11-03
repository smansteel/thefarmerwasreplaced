from __builtins__ import *

def m_plant_and_harvest(entity):
	if entity in [Entities.Carrot, Entities.Bush, Entities.Grass]:
		# one map
		for i in range(0, get_world_size()):
			for j in range(0, get_world_size()):
				if can_harvest():
					harvest()
					m_plant(entity)
				move(East)
			move(North)

	elif entity == Entities.Pumpkin:
		return plantAndHarvestPumpkin()

def m_plant(entity):
	if entity == Entities.Carrot:
		plantCarrot()
	elif entity == Entities.Bush:
		plantBush()
	elif entity == Entities.Grass:
		plantGrass()
	else:
		print("not implemented")

def plantCarrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def plantBush():
	if get_ground_type() == Grounds.Soil:
		till()
	if (get_pos_x() % 2 == 0 and get_pos_y() % 2) or ((get_pos_x()+1) % 2 == 0 and (get_pos_y()+1) % 2):
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def plantGrass():
	if get_ground_type() == Grounds.Soil:
		till()

def plantAndHarvestPumpkin():
	# plant
	for i in range(0, get_world_size()):
		for j in range(0, get_world_size()):
			if can_harvest():
				harvest()
				if get_ground_type() == Grounds.Soil:
					till()
				m_plant(Entities.Pumpkin)
			move(East)
		move(North)
	# control
	for i in range(0, get_world_size()):
		rowOk = False
		while not rowOk:
			if(not can_harvest()):
				rowOk = False
				plant(Entities.Pumpkin)
			move(East)
		move(North)
	harvest()
