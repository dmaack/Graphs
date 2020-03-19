import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0 # initalize    
        self.users = {} # users
        self.friendships = {} # friendships

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id) # connect the two friends, i follow you, you follow me
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"User {i + 1}")

        # Create friendships
        # To create N friendships,
        # you should create a lust with all possible friendship combinations,
        # shuffle list, then grab the first N elements from the list
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1): # we want to include the last id but it's not given to us
                possible_friendships.append((user_id, friend_id))
        #print(possible_friendships)     
        # O(n^2) -- or n * ( n / 2 ) -- or 1/2 * n^2
        random.shuffle(possible_friendships)

        # Create n friendships where 
        # N = avg_friendships * num_users // 2
        # average friendships = total friendships / num_users
        # total friendships = avg_friendships * num_users

        # Shuffle List
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])     


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # create empty queue
        q = Queue() 
        # add a path to the starting node to the queue
        q.enqueue([user_id])

        # While the queue is not empty...
        while q.size() > 0: 
            # Dequeue the first path from the queue
            path = q.dequeue()
            last_v = path[-1]
            # Check if it's been visited
            if last_v not in visited:
                # When we reach an unvisited node, add the path to visited dictionary
                visited[last_v] = path

            # Add a path to each neighbor to the back of the queue
            for v in self.friendships[last_v]:
                if v not in visited:
                    path_copy = list(path)
                    path_copy.append(v)
                    q.enqueue(path_copy)
        # Return visited dictionary
        return visited

       


if __name__ == '__main__':


    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # sg.populate_graph(num_users, avg_friendships)
    print(f'Friendships: {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f'Connections: {connections}')



# N = avg_friendships * num_users // 2
# average friendships = total friendships / num_users
# total friendships = avg_friendships * num_users


'''
 Q1: 

 N = 10 * 100 // 2 
 N = 




'''