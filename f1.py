from __builtins__ import *
from f2 import m_toPlantForRes


def myCost(entity, number=1):
	if entity == Entities.Grass or entity == Entities.Bush or entity == None:
		return True
	elif entity == Entities.Carrot:
		return num_items(Items.Hay) > number and num_items(Items.Wood) > number
	elif entity == Entities.Pumpkin:
		return num_items(Items.Carrot) > number
	return True


def m_getEntityFromGoal(objectives):
	for objective_key in objectives:
		if num_items(objective_key) < objectives[objective_key]:
			return m_toPlantForRes(objective_key)
	return Items.Gold



def m_isTargetFarmable(target, number=1):
	return myCost(target, number)

def m_getNextFarmableTarget(entity):
	nextFarmableTarget = None
	if entity == Entities.Grass or entity == Entities.Bush:
		return None
	elif entity == Entities.Carrot:
		if(num_items(Items.Hay) > num_items(Items.Wood)):
			nextFarmableTarget = Entities.Bush
		else:
			nextFarmableTarget  = Entities.Grass
	elif entity == Entities.Pumpkin:
		nextFarmableTarget = Entities.Carrot
	elif entity == Entities.Cactus:
		nextFarmableTarget = Entities.Pumpkin

	else:
		print("not implemented")
	if(not m_isTargetFarmable(nextFarmableTarget), get_world_size()*get_world_size()):
		return m_getNextFarmableTarget(nextFarmableTarget)
	else:
		return nextFarmableTarget
