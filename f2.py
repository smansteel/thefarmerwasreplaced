from __builtins__ import *
import f0

# def polyculture(start_point, start_entity):
#     path_history = []
#     f0.goto_coord(start_point[0], start_point[1])
#     f0.plant_safe(start_entity)
#     path_history.append((start_point[0], start_point[1]))
#     comp = get_companion()
#     f0.goto_coord(comp[1][0], comp[1][1])
#     f0.plant_safe(comp[0])
#     path_history.append((comp[1][0], comp[1][1]))
#     comp = get_companion()
#     while not comp[1] in path_history:
#         f0.goto_coord(comp[1][0], comp[1][1])
#         f0.plant_safe(comp[0])
#         path_history.append((comp[1][0], comp[1][1]))
#         comp = get_companion()
#
#     while len(path_history) != 0:
#         coord = path_history.pop(0)
#         f0.goto_coord(coord[0], coord[1])
#         while(not can_harvest()):
#             do_a_flip()
#         harvest()

directions = [
	North,
	South,
	East,
	West
]

def get_available_directions():
	avdir = []
	for direction in directions:
		if(can_move(direction)):
			avdir.append(direction)
	return avdir

opp = {
	North: South,
	South: North,
	East: West,
	West: East
}

# class Choice():
#     def __init__(self, coords,  avdirection):
#         self.coords = coords
#         self.avdirection = avdirection
#
#     def explore(self, direction):
#         if(direction not in self.avdirection):
#             return
#         else:
#             self.avdirection.remove(direction)

def go_to_last_branch(moves_history, where_to_stop):
	while((get_pos_x(), get_pos_y()) != where_to_stop):
		move(opp[moves_history[where_to_stop].pop()])

	# for move_to_do in reversed(moves_history):
	#     if((get_pos_x(), get_pos_y()) == where_to_stop):
	#         break
	#     move(opp[move_to_do])


def solve_maze():
	choice_nb = 0
	moves = []
	moves_since_choice = {}
	available_dir_at_choice = {}

	choice_history = []

	last_move = None


	while(get_entity_type() != Entities.Treasure):
		avdir = get_available_directions()
		if last_move == None and 1 == len(avdir):
			last_move = avdir[0]
			move(avdir[0])
		elif(last_move != None and 1 == len(avdir)):
			go_to_last_branch(moves_since_choice, choice_history[len(choice_history)-1])
			last_move = None
		elif len(avdir) == 2 and last_move != None:
			if(last_move != None):
				avdir.remove(opp[last_move])
			if(len(choice_history) != 0 and moves_since_choice[choice_history[len(choice_history)-1]] != None):
				# case start game
				moves_since_choice[choice_history[len(choice_history)-1]].append(avdir[0])
			last_move = avdir[0]
			move(avdir[0])
		else:
			if(last_move != None):
				avdir.remove(opp[last_move])
			if(get_pos_x(), get_pos_y()) in available_dir_at_choice:
				# case nouvelle branche du choix deja existant
				avdir = available_dir_at_choice[(get_pos_x(), get_pos_y())]

			if(len(avdir) == 0):
				choice_history.remove(choice_history[len(choice_history) - 1])
				go_to_last_branch(moves_since_choice, choice_history[len(choice_history)-1])
				last_move = None
			else:
				go = avdir[0]
				avdir.remove(go)
				available_dir_at_choice[(get_pos_x(), get_pos_y())] = avdir

				choice_history.append((get_pos_x(), get_pos_y()))
				choice_nb += 1
				moves_since_choice[(get_pos_x(), get_pos_y())]= []
				moves_since_choice[(get_pos_x(), get_pos_y())].append(go)
				last_move = go
				move(go)
		# elif
	harvest()



