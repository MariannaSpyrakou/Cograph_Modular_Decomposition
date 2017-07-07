from Trees import Tree
import itertools

# create_cotree: function that computes the cotree of a given graph

# two input options:
# --- 1. sage graph / python dictionary, with the nodes and ALL their neighbors
# --- 2. a list containing the names of the nodes and a nested list containing the "eliminated" neighbors of the nodes,
#     meaning that a node can have as neigbors only the nodes that precede in the given order.

def create_cotree_1(g):
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
			Tree.make_info_None(cotree)
	Tree.print_tree(cotree)
	return

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
				Tree.make_info_None(cotree)
	Tree.print_tree(cotree)
	return

# function that checks by definition if the given graph is a co-graph
# if there is an induced path on any subgraph with 4 vertices, then it is not a co-graph 
def has_no_p4_path(g):
	# find all the subgraphs of g with 4 vertices
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
		# In that case we have a path on 4 edges
		if count_edges==3 and len(vertex_cover)==4:
			# unless all edges are adjacent to one vertex
			if not (3 in vertex_counter.values()):
				print ("The input graph is not a co-graph. Execution terminated!")
				return False
	print (" ")
	return True

# An easier function to check if the graph is a cograph
# A little bit more time consuming
def has_no_p4_path_2(g):
	comb = list(itertools.combinations(g, 4)) # Find all subgraphs with 4 vertices
	for i in comb:
		#print i
		perm=list(itertools.permutations(i)) # Find all the permutations of the 4 nodes
		for j in perm:
			if g.has_edge(j[0],j[1]) and g.has_edge(j[1],j[2]) and g.has_edge(j[2],j[3]):
				if (g.has_edge(j[0],j[2]) or g.has_edge(j[0],j[3]) or g.has_edge(j[1],j[3])):
					break
				else:   # case that there is a path on 4 edges
					print ("The input graph is not a co-graph. Execution terminated!")
					return False
	print (" ")
	return True
