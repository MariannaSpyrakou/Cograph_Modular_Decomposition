from create_cotree import *
from sage.all import Graph,graphs

number_cographs=0
number_non_cographs=0
gen = graphs.nauty_geng("9 -c")
for g in list(gen):
	if has_no_p4_path(g):
		number_cographs+=1
		#for vert in g:
			#print (vert,g[vert])
		print number_cographs
		tree=create_cotree_1(g)
		#is_in_the_list(tree,co_gen)
	else:
		number_non_cographs+=1
print(" ")
print("# total nodes: 9")
print ("# of cographs is: ", 2*number_cographs)
print ("# of non cographs is: ", number_non_cographs)
