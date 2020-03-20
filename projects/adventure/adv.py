from room import Room
from player import Player
from world import World
from util import Stack, Queue


import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


'''
READ.ME Notes:

    You may find the commands useful:
        `player.current_room.id`, 
        `player.current_room.get_exits()`, 
        `player.travel(direction)` 

Plan:

    1: construct your own traversal graph
    2: use BFS for exploring / searching 
    3: Use DFT for creating map / maze ( what about recursion? )
        3a: how to connect / compare to test data (room_graph)
        3b: need a counter for keeping track of previous rooms?

   def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # Check is the node has been visited
        # If not...
        if visited is None:
            visited = set()
            # Mark it as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        // Instead of for each, 
            // pick one at random
            if sub_vertex with ? pick one
                # Call dft_recursive on each neighbor
                self.dft_recursive(sub_vertex, visited)
            else there are no ? to follow
                bfs to find a vertex with ?
                should return a vertex
                call dft on found vertex
                add the path of visited to dft

'''

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}

def find_shortest_path(starting_room_id): #search for shortest path (BFS)
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
            print('Traversal Graph Directions in BFS', traversal_graph[current_room])

            if traversal_graph[current_room][direction] == '?':
                print('path in conditional: ', path)
                # return available paths
                return path
                
            elif traversal_graph[current_room][direction] not in visited:
                # create new path to append/add direction/edge
                new_path = list(path)
                path.append(traversal_graph[current_room][direction])
                q.enqueue(new_path)
                print('Appending direction', new_path)

        

def search(starting_room):

    # Rooms visited counter
    visited_room = 0
    # opposing directions for back tracking
    back_track = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

    # What room we are currently in
    current_room = player.current_room
    print("Players current room: ", current_room)
    # The id we are currently in
    print("Players current room ID: ", player.current_room.id)
    room_id = player.current_room.id

    #prints out directions
    print("Exits", player.current_room.get_exits() ) 

    # build graph and make a dictionary of rooms 
    room_dict = {}      # 0: { n: '?', s: '?', e: '?', w: '?' }

    
    # while the length of taversal_graph does not equal the length of room_graph
    while len(traversal_graph) != len(room_graph):
        print("current room: ", current_room.id)
        # if room_id is not in traversal_graph:
        if room_id not in traversal_graph:
            # Iterate through current room exits to find the possible exits:
            for i in current_room.get_exits():
                # add the "?" to corresponding key in the room dictionary
                print("i: ", i) # prints n direction
                room_dict[i] = '?'
                print("room dictionary", room_dict) 
            # update room
            if traversal_path:
                prev_room = back_track[traversal_path[-1]]
                print('prev_room', prev_room)
                room_dict[prev_room] = prev_room
            #add the unexplored room to the room id
            traversal_graph[room_id] = room_dict
            

        else:
            break

        # Now I see the '?', need to check if there is a room connected

        possible_exits = list()

        # iterate through dictionary
        for direction in room_dict:
            # If '?' at the room dictionary index/value
            if room_dict[direction] == '?':
                # store them
                possible_exits.append(direction)
                print('Possible exit: ', possible_exits)

        # if there is an unknown direction
        if len(possible_exits) != 0:
            # randomly pick a possible exit
            random.shuffle(possible_exits)
            print('next possible exits: ', possible_exits)

            direction = possible_exits[0]
            print('You moved: ', direction)

            traversal_path.append(direction)
            print('traversal path in if possible_exists', traversal_path)

            for move in traversal_path:
                # move player in 'direction' of travel_path
                player.travel(move)
                print('move', move)
                
                move = player.current_room
                print('move = current room:', player.current_room.get_exits())

             
        


print("---------------")
print("Search", search(room_graph))
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
