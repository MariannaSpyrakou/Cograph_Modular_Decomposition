from sage.all import Graph
from create_cotree import create_cotree

# input option 1:
d = {'a': ['b','d','e','f','x'],
         'b': ['a','f','e','d'], 'c': ['f','e','d'],
         'd': ['a','b','c','x'], 'e': ['a','b','c','x'],
         'f': ['a','b','c','x'] , 'x': ['f','a','d','e']
         }
g=graph(d)
create_cotree(g)


# input option 2:
names =['a','b','c','d','e','f','x'] 
neighbors = [[],['a'] ,[],  ['a','b','c'], ['a','b','c'], ['a','b','c'] , ['f','a','d','e']]

create_cotree(names,neighbors)
