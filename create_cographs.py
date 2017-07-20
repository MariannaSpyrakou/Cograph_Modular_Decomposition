from create_cotree import *
from sage.all import Graph,graphs

"""
Create all graphs with n nodes, check which of them are cographs and output their cotree.
generate all graphs with the command gen = graphs.nauty_geng("n -c"). Replace n with the number of vertices of the graph
(Works for n=3,...,9)
"""
gen = graphs.nauty_geng("9 -c")
number_cographs=0
number_non_cographs=0
for g in list(gen):
	if has_no_p4_path(g): # it is cograph
		number_cographs+=1
		# print the co_graph
		#for vert in g:
			#print (vert,g[vert])
		# count the co_graphs
		#print number_cographs
		tree=create_cotree_1(g)
	else:
		number_non_cographs+=1
print(" ")
#print("# total nodes: 9")
print ("# of cographs is: ", 2*number_cographs)
print ("# of non cographs is: ", number_non_cographs)
