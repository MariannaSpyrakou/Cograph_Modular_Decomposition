from Trees import Tree
from sage.all import Graph
from Cograph_generator import *
import itertools

def create_cotree_1(g):
	"""
 	create_cotree: function that computes the cotree of a given graph

 	two input options:
 	--- 1. sage graph / python dictionary, with the nodes and ALL their neighbors
	--- 2. a list containing the names of the nodes and a nested list containing the "eliminated" neighbors of the nodes,
  	       meaning that a node can have as neigbors only the nodes that precede in the given order.
	"""
	if has_no_p4_path(g)==False:
		return
	cotree=Tree('1')
	# the root of the tree is always '1'
	i=0
	for node in g:
		if i==0:
			first_node=node
			i=i+1
		elif i==1:
			if g.has_edge(node,first_node):
				# first and second node are adjacent
				Tree.add_child(cotree,Tree(first_node))
				Tree.add_child(cotree,Tree(node))
			else:
				# first and second node are not adjacent
				tree0=Tree('0',[Tree(first_node),Tree(node)])
				Tree.add_child(cotree,tree0)
			i=i+1
		else:
			# add incrementally nodes 3,...,end to the cotree
			flag_mixed=[0]
			Tree.is_cograph(cotree,node,g[node],flag_mixed)
			if flag_mixed[0]==0:
				Tree.update_cotree(cotree,node,g[node],0,0)
			elif flag_mixed[0]==2:
				print ("The input graph is not a co-graph. Execution terminated!")
				return
			# initialize tree info for the next iteration
			cotree.reset_info()
	#cotree.print_tree()
	return cotree

def create_cotree_2(name,neighbors):
	cotree=Tree('1')
	# the root of the tree is always '1'
	for i in range(len(name)):
		if i==1:
			if name[0] in neighbors[1]:
				# first and second node are adjacent
				Tree.add_child(cotree,Tree(name[0]))
				Tree.add_child(cotree,Tree(name[1]))
			else:
				# first and second node are not adjacent
				tree0=Tree('0',[Tree(name[0]),Tree(name[1])])
				Tree.add_child(cotree,tree0)
		elif i!=0:
			# add incrementally nodes 3,...,end to the cotree
			flag_mixed=[0]
			Tree.is_cograph(cotree,name[i],neighbors[i],flag_mixed)
			if flag_mixed[0]==0:
				Tree.update_cotree(cotree,name[i],neighbors[i],0,0)
			elif flag_mixed[0]==2:
				print ("The input graph is not a co-graph. Execution terminated!")
				return
			if i<len(name)-1:
				# initialize tree info for the next iteration
				cotree.reset_info()
	#cotree.print_tree()
	return cotree

def has_no_p4_path(g):
	"""
 	function that checks by definition if the given graph g is a co-graph
 	if there is an induced path on any subgraph with 4 vertices, then it is not a co-graph,
 	otherwise it is a co-graph
	
	There is a path on 4 vertices if:
		 1) there are exactly 3 edges in the subgraph 
		 2) there is at least one edge adjacent to each node (the "vertex cover" of the edges includes all 4 vertices)
		 3) each vertex has at most 2 adjacent vertices
	"""
	
	# find all the subgraphs of g on 4 vertices
	comb = list(itertools.combinations(g, 4))
	for i in comb:
		#print i
		# find all possible edges of the subgraph / all possible combinations of the 4 vertices
		pos_edges=list(itertools.combinations(i,2))
		count_edges=0  # number of edges in the subgraph
		vertex_cover=[] # list of all vertices that have adjacent nodes in the subgraph
		vertex_counter={i[0]:0,i[1]:0,i[2]:0,i[3]:0} # count how many edges are adjacent to each node
		for j in pos_edges:
			if g.has_edge(j):
				count_edges=count_edges+1
				if not (j[0] in vertex_cover):
					vertex_cover.append(j[0])
				vertex_counter[j[0]]=vertex_counter[j[0]]+1
				if not (j[1] in vertex_cover):
					vertex_cover.append(j[1])
				vertex_counter[j[1]]=vertex_counter[j[1]]+1
			if count_edges>=4: # there is at least one cycle in the subgraph
				break
		#print count_edges
		if count_edges==3 and len(vertex_cover)==4:
			# at most 2 adjacent vertices = no vertex with 3 adjacent vertices
			if not (3 in vertex_counter.values()):
				#print ("The input graph is not a co-graph. Execution terminated!")
				return False
	#print (" ")
	return True


def has_no_p4_path_2(g):
	"""
	An easier function to check if the graph is a cograph
	A little bit more time consuming
	Finds all subgraphs of g on 4 vertices and
	checks all possible paths on the subgraph to see if there exists one  
	"""	
	comb = list(itertools.combinations(g, 4)) # Find all subgraphs with 4 vertices
	for i in comb:
		#print i
		perm=list(itertools.permutations(i)) # Find all the permutations of the 4 nodes
		for j in perm:
			if g.has_edge(j[0],j[1]) and g.has_edge(j[1],j[2]) and g.has_edge(j[2],j[3]):
				if (g.has_edge(j[0],j[2]) or g.has_edge(j[0],j[3]) or g.has_edge(j[1],j[3])):
					break
				else:   # case that there is a path on 4 edges
					#print ("The input graph is not a co-graph. Execution terminated!")
					return False
	#print (" ")
	return True



def tree_to_graph(tree,g):
	for child in tree.children:
            tree_to_graph(child,g)
        if tree.name!='1' and tree.name!='0':
		tree.info='v'
		find_neighbors(tree,g)
		tree.reset_info()
        return	

	
def find_neighbors(tree,g):
	ancestor=tree.parent
	ancestor.info='v'
	while ancestor!=None:
		if ancestor.name=='1':
			for sibling in ancestor.children:
				if sibling!=tree and sibling.info!='v':
					add_sibling(tree,sibling,g)
		elif ancestor.name=='0':
			ancestor.info='v'
		ancestor=ancestor.parent
		
			

def add_sibling(tree,sibling,g):
	if sibling.name!='0' and sibling.name!='1':
		g.add_edge(tree.name,sibling.name)
	else:
		for child in sibling.children:
			add_sibling(tree,child,g)
	


if __name__ == "__main__":
	# input option 1:
	d = {'a': ['b','d','e','f','x'],
     'b': ['a','f','e','d'],
     'c': ['f','e','d'],
     'd': ['a','b','c','x'],
     'e': ['a','b','c','x'],
     'f': ['a','b','c','x'] ,
     'x': ['f','a','d','e']}
	g=Graph(d)
	#create_cotree_1(g)

	#print (" ")

	# input option 2:
	names =['a','b','c','d','e','f','x']
	neighbors = [[],['a'] ,[],  ['a','b','c'], ['a','b','c'], ['a','b','c'] , ['f','a','d','e']]
	#create_cotree_2(names,neighbors)
	
	print (" ")
	# n= number of vertices of the graph
	n=8
	co_gen=cograph_generator(n)
	false_counter=0;
	for tree in co_gen:
		g=Graph(n)
		tree_to_graph(tree,g)
		cotreee=create_cotree_1(g)
		false_flag=tree.tree_equality(cotreee)
		if false_flag!=None:
			false_counter+=1
	print ("The number of wrongly computed cotrees is: ", false_counter)	
