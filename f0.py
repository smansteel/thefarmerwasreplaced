from __builtins__ import *
from f2 import m_goto


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
		plantAndHarvestPumpkin()
	elif entity == Items.Gold:
		plantAndSolveMaze()
	elif entity == Entities.Cactus:
		plantAndHarvestCacti()

def m_plant(entity):
	if entity == Entities.Carrot:
		plantCarrot()
	elif entity == Entities.Bush:
		plantBush()
	elif entity == Entities.Grass:
		plantGrass()
	elif entity == Entities.Pumpkin:
		plantPumpkin()
	elif entity == Entities.Cactus:
		plantCactus()
	else:
		print("not implemented")

def plantCarrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)
def plantPumpkin():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Pumpkin)
def plantCactus():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)

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
			m_plant(Entities.Pumpkin)
			move(East)
		move(North)
	# control
	for i in range(0, get_world_size()):
		for j in range(0, get_world_size()):
			while (get_entity_type() != Entities.Pumpkin or not can_harvest()):
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
			move(East)
		move(North)
	m_goto(0,0)
	harvest()


def plantAndSolveMaze():
	m_goto(0,0)
	m_plant(Entities.Bush)
	use_item(Items.Weird_Substance)
	##solve
	harvest()

def plantAndHarvestCacti():
	#clean
	for i in range(0, get_world_size()):
		for j in range(0, get_world_size()):
			if can_harvest():
				harvest()
	# one map
	for i in range(0, get_world_size()):
		for j in range(0, get_world_size()):
			m_plant(Entities.Cactus)
			move(East)
		move(North)

	map={10: [],9: [],8: [],7: [],6: [], 5: [], 4: [], 3: [], 2: [], 1: [], 0: [] }
	for i in range(0, get_world_size()):
		for j in range(0, get_world_size()):
			map[measure()] = map[measure()].append([get_pos_x(), get_pos_y()])
			move(East)
		move(North)

	for levels in map:
		for points in map[levels]:
			m_goto(points[0], points[1])
			harvest()
