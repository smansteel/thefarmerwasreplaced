from __builtins__ import *

def myCost(entity, number=1):
	if entity == Entities.Grass or entity == Entities.Bush:
		return True
	elif entity == Entities.Carrot:
		return num_items(Items.Hay) > number and num_items(Items.Wood) > number


def m_getEntityFromGoal(objectives):
	if objectives[0] > num_items(Items.Hay):
		return Entities.Grass
	elif objectives[1] > num_items(Items.Wood):
		return Entities.Bush
	elif objectives[2] > num_items(Items.Carrot):
		return Entities.Carrot
	else:
		return Entities.Carrot



def m_isTargetFarmable(target, number=1):
	return myCost(target, number)

def m_getNextFarmableTarget(entity):
	if entity == Entities.Grass or entity == Entities.Bush:
		return None
	elif entity == Entities.Carrot:
		if(num_items(Items.Hay) > num_items(Items.Wood)):
			return Entities.Bush
		else:
			return Entities.Grass
