from __builtins__ import clear, move, North, East, harvest, Entities, can_harvest
from f0 import plant




clear()

target = Entities.Carrot
while True:
	move(North)
	for i in range (0,3):
		if can_harvest():
			harvest()
			plant()
		move(East)
