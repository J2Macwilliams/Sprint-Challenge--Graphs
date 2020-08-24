"""
 Understand:
    - Objective is to end up with a list of moves -> [n,s,e,n,s,w]
    - Use the power of traversal
    - Hints are Misleading
    - Tenets of Traversing
    ##Translate
    ##Build
    ##Traverse

    -Acquire graph from file and put it together
    -identify visited rooms with a set
    -identify moves from the traversal_graph[room].keys()
    -follow the unvisited rooms down the rabbit hole, then backtrack

"""
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Translate
# PLAN
# Abstract out info from room_graph to traversal graph
# use a DFT like traversal approach with recursion
# idea is to identify rooms not visited traverse thu them 
# back track out of rooms already visited
# Build Graph
# Traveling dictionary for opposites moves
# create a recursive function
    # pass visited set thru call stack
        # establish route for collecting moves
        # set current room to a variable
        # create loop with directions from create traversal graph
        # create variable for accessing nxt_room
        # check nxt_room if visited
        # add room to visited set
        # move player thru move_dir
        # add move to route
        # use recursion to increment route
        # thru unvisited rooms
        # backtrack out of rooms visited
        # add backtrack moves to route

# return route



# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# set traversal path to function response
traversal_path = []



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
