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
map_file = "maps/test_cross.txt"
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
        # print("visited", visited)

        

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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
