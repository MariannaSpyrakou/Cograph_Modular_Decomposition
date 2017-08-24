from Trees import Tree
from sage.all import Graph,graphs
from Cograph_modular_decomposition import *
from Cograph_generator import *

# input option 1:
d = {'a': ['b','d','e','f','x'],
     'b': ['a','f','e','d'],
     'c': ['f','e','d'],
     'd': ['a','b','c','x'],
     'e': ['a','b','c','x'],
     'f': ['a','b','c','x'] ,
     'x': ['f','a','d','e']}
g=Graph(d)
cotree_1=cograph_modular_decomposition(g)
cotree_1.print_tree()

print (" ")

# input option 2:
names =['a','b','c','d','e','f','x']
neighbors = [[],['a'] ,[],  ['a','b','c'], ['a','b','c'], ['a','b','c'] , ['f','a','d','e']]
inp=[names,neighbors]
cotree_2=cograph_modular_decomposition(inp)
cotree_2.print_tree()

print (" ")

"""
Generate all co-trees of the cographs with n nodes and check if cograph_modular_decomposition functions computes it correctly
"""
# n= number of vertices of the graph
n=5
co_gen=cograph_generator(n)
false_counter=0;
for tree in co_gen:
	g=Graph(n)
	tree_to_graph(tree,g)
	cotreee=cograph_modular_decomposition(g)
	false_flag=tree.tree_equality(cotreee)
	if false_flag!=None:
		false_counter+=1
print ("The number of wrongly computed cotrees is: ", false_counter)	
	
