from Trees import Tree
from sage.all import Graph,graphs
from Cograph_recognition import is_cograph
import itertools

def cograph_modular_decomposition(inp):
	"""
 	function that computes the cotree of a given graph

 	two input options:
 	--- 1. sage graph / python dictionary, with the nodes and ALL their neighbors
	--- 2. a list containing the names of the nodes and a nested list containing the "eliminated" neighbors of the nodes,
  	       meaning that a node can have as neigbors only the nodes that precede in the given order.
	"""
	if type(inp)==type([]): 
		return create_cotree_2(inp)
	else: 
		return create_cotree_1(inp)

def create_cotree_1(g):
	if is_cograph(g)==False:
		return
	cotree=Tree('1')
	# the root of the tree is always '1'
	i=0
	for node in g:
		if i==0:
			first_node=node
			i+=1
		elif i==1:
			if g.has_edge(node,first_node):
				# first and second node are adjacent
				Tree.add_child(cotree,Tree(first_node))
				Tree.add_child(cotree,Tree(node))
			else:
				# first and second node are not adjacent
				tree0=Tree('0',[Tree(first_node),Tree(node)])
				Tree.add_child(cotree,tree0)
			i+=1
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
	return cotree

def create_cotree_2(inp):
	name=inp[0]
	neighbors=inp[1]
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
	return cotree
