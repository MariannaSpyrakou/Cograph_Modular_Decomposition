from Trees import Tree

# create_cotree: function that computes the cotree of a given graph

# two input options:
# --- sage graph / python dictionary, with the nodes and ALL their neighbors
# --- a list containing the names of the nodes and a nested list containing the "eliminated" neighbors of the nodes,
#     meaning that a node can have as neigbors only the nodes that precede in the given order.

def create_cotree(g):
	cotree=Tree('1')
	# the root of the tree is always '1'
	i=0
	for node in g:
		if i==0:
			first_node=node
			i=i+1
		elif i==1:
			if g[node].count(first_node):
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
			Tree.make_info_None(cotree)
	Tree.print_tree(cotree)
	return

def create_cotree(name,neighbors):
	cotree=Tree('1')
	# the root of the tree is always '1'
	for i in range(len(name)):
		if i==1:
			if neighbors[1].count(name[0]):
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
				Tree.make_info_None(cotree)
	Tree.print_tree(cotree)
	return
