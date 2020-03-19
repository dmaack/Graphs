
'''
       10
     /
    1   2   4  11
     \ /   / \ /
      3   5   8
       \ / \   \
        6   7   9
'''

'''
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
'''
from util import Stack
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    print(ancestors)
    # initialize a graph
    g = Graph()

    # strip duplicates
    s = set()
    for pair in ancestors:
        for ancestor in pair:
            s.add(ancestor)
    l = list(s)

    # add to graph
    for num in l:
        g.add_vertex(num)
    
    # add ancestors
    for i in ancestors:
        g.add_edge(i[1], i[0])

    # last in first out
    s = Stack()
    s.push(starting_node)
    
    path = []
    outer = []
        
    while s.size() > 0:
        x = s.pop()
        path.append(x)

        if g.vertices[x]:
            for vert in g.vertices[x]:
                s.push(vert)
        # no ancestors to starting_node
        elif x == starting_node:
           return -1
        # reached the oldest ancestor for a path
        else:
            outer.append(path)
            path = path[:len(outer)]

    # create a counter
    longest = []
    # for each path in list
    for i in range(len(outer)):
        if len(outer[i]) > len(longest):
            longest = outer[i]
        elif len(outer[i]) == len(longest):
            x = outer[i]
            if x[-1] < longest[-1]:
                longest = x
    
    return longest[-1]
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 10))