from __builtins__ import clear, move, Grounds, North, East, harvest, Entities, can_harvest
from f0 import plant

clear()
while True:
	move(North)
	for i in range (0,3):
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		move(East)
