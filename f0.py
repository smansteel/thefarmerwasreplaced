from __builtins__ import *

def plant(entity):
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
	plant(Entities.Bush)

def plantGrass():
	if get_ground_type() == Grounds.Soil:
		till()
