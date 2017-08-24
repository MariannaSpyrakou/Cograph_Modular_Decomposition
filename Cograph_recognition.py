from sage.all import Graph,graphs
import itertools

def is_cograph(g):
	P4 = graphs.PathGraph(4)
	return not g.subgraph_search(P4, induced=True)

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
		if count_edges==3 and len(vertex_cover)==4:
			# at most 2 adjacent vertices = no vertex with 3 adjacent vertices
			if not (3 in vertex_counter.values()):
				#print ("The input graph is not a co-graph. ")
				return False
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
		perm=list(itertools.permutations(i)) # Find all the permutations of the 4 nodes
		for j in perm:
			if g.has_edge(j[0],j[1]) and g.has_edge(j[1],j[2]) and g.has_edge(j[2],j[3]):
				if (g.has_edge(j[0],j[2]) or g.has_edge(j[0],j[3]) or g.has_edge(j[1],j[3])):
					break
				else:   # case that there is a path on 4 edges
					#print ("The input graph is not a co-graph.")
					return False
	return True
