'''

Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.


Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None

'''
from util import Stack, Queue 

# 2: Build the Graph
# Load words from dictionary
f = open('words.txt', 'r')
words = f.read().lower().split('\n')
f.close()


def get_neighbors(word):
    '''
    Get all words that are one letter 
    away from the given word
    '''
    # Get same length words first
    result = []
    pass


def words_are_neighbors(w1, w2):
    '''
    return True if words are one letter apart
    False otherwise
    '''
    list_word= list(w1)
    # Go through each letter in the word
    for i in range(len(list_word))
        # swap with each letter in the alphabet
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            # Check if that equals given word
            temp_word = list_word.copy()
            temp_word[i] = letter
            if ''.join(temp_word) == w2:
                return True
    return False

def words_are_neighbors(w1, w2):
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
            return True
    return False



words_are_neighbors('abc', 'abd')

neighbors = {}

# Go through each word
for word in words:
    neighbors[word] = set()
    # Go through each potential neighbor
    for potential_neighbor in neighbors:
        # Add the neighbors if the match
        if words_are_neighbors(word, potential_neighbor):
            neighbors[word].add(potential_neighbor)

# 3: Traverse the Graph (BFS)

def word_traverse(self, begin_word, end_word):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        q = Queue()
        # Enqueue a PATH TO the starting word
        q.enqueue([begin_word]) # initializing an array with starting_vertex
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE LAST WORD FROM THE END OF THE PATH
            last_w = path[-1]
            # Check if it's been visited
            # If it hasn't been visited...
            
                # Mark it as visited
                # CHECK IF IT'S THE TARGET WORD
                if last_w == end_word:
                    # IF SO, RETURN THE PATH
                    return path
                # Enqueue A PATH TO all it's neighbors
                if last_w not in visited:
                    visited.add(last_w)
                    # MAKE A COPY OF THE PATH
                    for neighbor in get_neighbors():
                        path_copy = path.copy()
                        path_copy.append(neighbor)
                        # ENQUEUE THE COPY
                        q.enqueue(path_copy) 
