from room import Room
from player import Player
from world import World
from util import Stack, Queue


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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}


# BFS: search for shortest path
def find_shortest_path(starting_room_id): 
    # Create a queue
    q = Queue()
    # Enqueue a PATH TO the starting vertex (starting_room_id)
    q.enqueue([starting_room_id])
    # Create a set to store visited room_id's
    visited = set() 

    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first available PATH
        path = q.dequeue()
        print("path", path, "\n\n")
        # current_room = Grab the last room_id from the end of the PATH
        current_room = path[-1]
        print("current room", current_room, "\n\n")
        visited.add(current_room)
        print("visited", visited)


        # for each connection in current room
        for direction in traversal_graph[current_room]:
            print('Traversal Graph Directions in BFS', traversal_graph[current_room]) # not printing

            if traversal_graph[current_room][direction] == '?':
                print('path in conditional: ', path)
                # return to available paths
                return path
                
            elif traversal_graph[current_room][direction] not in visited:
                # create new path to append/add direction/edge
                new_path = list(path)
                new_path.append(traversal_graph[current_room][direction])
                q.enqueue(new_path)
                print('Appending direction', new_path)

        
# DFT: Searching all possible paths of graph/maze until exit is path found
def search(starting_room):

    # Rooms visited counter
    visited_room = 0
    # opposing directions for back tracking
    back_track = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    
    # while the length of taversal_graph does not equal the length of room_graph
    while len(traversal_graph) != len(room_graph):

         # What room we are currently in
        current_room = player.current_room
        print("Players current room: ", current_room)
        # The id we are currently in
        print("Players current room ID: ", player.current_room.id)
        room_id = current_room.id

        #prints out directions
        #print("Exits", player.current_room.get_exits() ) 

        # build graph and make a dictionary of rooms 
        room_dict = {}      # 0: { n: '?', s: '?', e: '?', w: '?' }



        # if room_id is not in traversal_graph:
        if room_id not in traversal_graph:
            # Iterate through current room exits to find the possible exits:
            for i in current_room.get_exits():
                # add the "?" to corresponding key in the room dictionary
                print("i: ", i) # prints n direction
                room_dict[i] = '?'
                print("building room dictionary", room_dict) 
            # updating the room  
            if traversal_path:
                # store the direction of the last traveled path
                prev_room = back_track[traversal_path[-1]]
                print('prev_room', prev_room) 
                # add the last traveled path to the counter
                room_dict[prev_room] = visited_room
                print('visited_room counter', visited_room)
            #add the unexplored room '?' to the corresponding room_id
            traversal_graph[room_id] = room_dict
            print('room dict after while', room_dict)
            

        else:
            # add room_id from traversal_graph to room_dict
            room_dict = traversal_graph[room_id]
            print('else: room dict: ', room_dict)

        # Now I see the '?', need to check if there is a room connected
        # store '?'

        possible_exits = list()

        # iterate through dictionary
        for direction in room_dict:
            # If there is '?' at the room dictionary index/value
            if room_dict[direction] == '?':
                # store them so I can use them to travel
                possible_exits.append(direction)
                print('Possible exit: ', possible_exits)

        # if there is an unknown direction
        if len(possible_exits) != 0: # len(possible_exits) gives me 1
            # randomly pick a possible exit
            random.shuffle(possible_exits)
            print('next possible exits: ', possible_exits)

            direction = possible_exits[0]
            print('You moved the randomly picked direction: ', direction)

            # append the random picked direction to traversal path
            traversal_path.append(direction)
            print('traversal path in conditional (186)', traversal_path)

            # move player in 'direction' of travel_path
            player.travel(direction)
            print('move', direction)
            print('exits in current room', player.current_room.get_exits())

            # grab the player current room 
            move_rooms = player.current_room
            print('move_rooms = current room:', move_rooms)
            print('move_rooms = current room ID:', move_rooms)
            print('dictionary after move: ', traversal_graph[current_room.id][direction])

            # replace '?' with room_ids
            traversal_graph[current_room.id][direction] = move_rooms.id
            visited_room = current_room.id

        else: 
            # BFS to search for next possible exit using room_id

            next_room = find_shortest_path(room_id)
            print('BFS path to next room: ', next_room)

            # if path from next_room has results from bfs 
            if next_room is not None and len(next_room) > 0: 
                print('this code ran')

                # iterate the length of the room to access room_ids
                for i in range(len(next_room) - 1):
                    print('else i: ', i)
                    print('traversal graph at [i]', traversal_graph[next_room[i]])
                    
                    # iterate the traversal_graphs next_room value to acces it's direction
                    for direction in traversal_graph[next_room[i]]:
                        print('direction in double for loop', direction)
                        
                        # if the traversal_graphs next room value and direction matches the bfs found next room value
                        if traversal_graph[next_room[i]][direction] == next_room[i + 1]:
                            # append the direction to travel_path
                            traversal_path.append(direction)
                            # move th player to that room
                            player.travel(direction)
            else:
                break


        

search(room_graph)

# print("---------------")
# print("Search", search(room_graph))
# # search(room_graph)
print("---------------")
print("Traversal Graph", traversal_graph) 
print("---------------")
print("Traversal path", traversal_path)
print("---------------")





# ---------------------------------- My Code Above ---------------------


# TRAVERSAL TEST
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
