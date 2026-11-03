from __builtins__ import clear, move, North, East, harvest, Entities, can_harvest, get_world_size
from f0 import m_plant_and_harvest
from f1 import m_isTargetFarmable, m_getNextFarmableTarget, m_getEntityFromGoal
from f2 import m_goto




m_goto(0,0)
m_goto(1,1)
m_goto(5,5)


clear()

objectives = [5000, 7500, 2000]

worldSize = get_world_size() * get_world_size()



while True:
	# decision once per map
	target = m_getEntityFromGoal(objectives)
	if m_isTargetFarmable(target, worldSize):
		runTarget = target
	else:
		runTarget = m_getNextFarmableTarget(target)
	m_plant_and_harvest(runTarget)

