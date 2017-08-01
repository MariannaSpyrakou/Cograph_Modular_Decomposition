from Trees import Tree
from sage.all import Graph
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


" Cograph Generation with linear delay (A. Jones, F. Protti, R. Vecchio)"


def next_partition(a):
	"""
	given a partition a (of number n) find the partition immediately next to a
	all partitions of 4 are: [1,1,1,1], [1,1,2],[1,3],[2,2] (in increasing order)
	next_partition([1,1,2])  is [1,3]
	"""	
	k=len(a)
	n=0
	for i in range(k):
		n=n+a[i]
	if a[0] != (n//2):
		if a[k-1]-a[k-2]<=1:
			b=[]
			for i in range(0,k-2):
				b.append(a[i])
				#print b
			b.append(a[k-2]+a[k-1])
			return b
		else: 	
			a[k-2]=a[k-2]+1
			a[k-1]=a[k-1]-1
			q=a[k-1]//a[k-2]
			r=a[k-1]%a[k-2]
			if q>1:
				b=[]
				for i in range(0,k-2):
					b.append(a[i])
				for i in range(0,q):
					b.append(a[k-2])
				b.append(a[k-2]+r)
				return b
			else:
				return a
	else:
		if n!=3:
			return None
		else:
			if a[1]==n//2+n%2:
				return None
			else:
				return [1,2]


def rebuild_node(u,a):
	"""
 	rebuild_node(u,a): given a node u of the ordered tree T and a partition a, 
	the subtree T(u) is replaced by the partition a, that is induced by u.
	"""
	k=len(a)
	# replace the children of u with the partition a
	# if k < number of existing children of the node, then we don't have to add children, just replace the 'existing' children.
	if k<=len(u.children): # General case, when function cograph_generator is used
		for i in range(len(u.children)):
			# add the i-th child of u
			if i<k:
				u.children[i]=Tree(a[i])
				u.children[i].parent=u
				if a[i]>1: # if i not a leaf, its children should be leaves 
					this_child=u.children[i] 
					for j in range(a[i]):
						this_child.add_child(Tree(1))	
			else: # If there are more "existing" children than we need set  
				u.children[i]=None
	else: # used only when transforming trees seperately from cograph_generator 
		for i in range(k):
			# add the i-th child of u
			if i<len(u.children):
				u.children[i]=Tree(a[i])
				u.children[i].parent=u
				if a[i]>1: # if i not a leaf, its children should be leaves 
					this_child=u.children[i] 
					for j in range(a[i]):
						this_child.add_child(Tree(1))	
			else:
				u.add_child(Tree(a[i]))
				u.children[i].parent=u
				if a[i]>1: # if i not a leaf, its children should be leaves 
					this_child=u.children[i] 
					for j in range(a[i]):
						this_child.add_child(Tree(1))
	# return the tree
	return 

def find_pivot(T,pivot):
	"""
 	find_pivot(T,pivot): given a tree T and a list pivot it finds the pivot i.e. the first node in reverse postorder traversal
	that does not induce a maximum partition. 
	"""
	for child in reversed(T.children):
		if pivot==[] and child!=None:
        		find_pivot(child,pivot)
	""" (Definition 9: pivot node)
	 if node T is not a leaf, it does not induce a maximum partition 
	 and it is the first such node in the inverse postorder traversal, 
	 then it is the  PIVOT.
	
	 the maximum partition of u is [floor(u/2),ceil(u/2)]
 	"""
	
	#partition=[]
	#for i in T.children:
		#if i!=None:
			#partition.append(i.name)
	i=T.name
	if pivot==[] and T.name!=1 and ((i//2!=T.children[0].name) or ((i//2+i%2)!=T.children[1].name)): #and next_partition(partition)!=None: 
		pivot.append(T)
		T.info='p'
		#print ("pivot is:",T.name)
	return 

def next_tree(T):
	pivot=[]
	find_pivot(T,pivot)
	if pivot!=[]: # If there is a pivot, then we can find the next tree
		#print pivot[0]
		"find the existing partition that is induced by pivot"
		partition=[]
		for i in pivot[0].children:
			if i!=None:
				partition.append(i.name)
		b=next_partition(partition) # finds the next partition induced by the subtree pivot[0]
		rebuild_node(pivot[0],b) # changes the subtree "pivot[0]"
		x=pivot[0]
		while True:
			if x.parent!=None:
				ancestor=x.parent
				#print ancestor.name
				# modify the bigger siblings of node x
				is_bigger_sibling=False
				for y in range(len(ancestor.children)) : # y = all siblings of x
					if ancestor.children[y]!=None:
						this_child=ancestor.children[y]
						if this_child.info=='p':
							is_bigger_sibling=True
						if is_bigger_sibling==True and this_child.info!='p': # true only for bigger siblings of x
							if x.name==this_child.name: 
								#print ("case 1")
								temp=Tree(x.name)
								x.copy_tree(temp)
								ancestor.children[y]=temp  #copy subtree T(x) in T(y)  #copy subtree T(x) in T(y)
							else:
								#print ("case 2")
								c=[]
								for i in range(ancestor.children[y].name):
									c.append(1)
								rebuild_node(ancestor.children[y],c)
				# set x= parent of x 
				x.info=None # reset the pivot mark
				x=ancestor
				if x==None:
					break
				x.info='p' # the parent gets the pivot mark	
			else: 
				break
		return True
	else:  # If there is no pivot, then there isn't any other tree
		return False
		
	



def cograph_generator(n):
	""" 
	Input integer n
 	Output, all cographs with n nodes
	"""
	if n>=2:
		#print n
		# Construct the minimum tree
		T=Tree(n)
		for j in range(n):
			T.add_child(Tree(1))
		i=1
		flag=True
		cograph_gen=[]
		while flag:
			## T corresponds to 2 cotrees: one with '0' root and one with '1' root
			#T.print_tree() 
			tree1=Tree(T.name)
			T.copy_tree(tree1)
			tree0=Tree(T.name)
			T.copy_tree(tree0)
			# tree 1 has root '1'
			counter=[0]
			change_names(tree1,1,counter)
			# tree 0 has root '0'
			counter=[0]
			change_names(tree0,0,counter)
			tree00=Tree('1')
			tree00.add_child(tree0)
			cograph_gen.append(tree1)
			cograph_gen.append(tree00)
			flag=next_tree(T) # Find the next tree. return False if there is no other Tree
			if not flag:
				break
			#print(" ")
			i=i+1
		print ("The number of cotrees is: ",2*i)
		return cograph_gen
	else:
		print ("Number of vertices must be >=2")
	return

def change_names(tree,status,counter):
	if tree.name!=1:
		#print tree.name
		tree.name=str(status%2)
	else:
		tree.name=counter[0]
		counter[0]+=1
	for child in tree.children:
		if child!=None: 
			change_names(child,status+1,counter)
	return

def tree_to_graph(tree,g):
	for child in tree.children:
            if child != None:
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
				if sibling!=tree and sibling!=None and sibling.info!='v':
					add_sibling(tree,sibling,g)
		elif ancestor.name=='0':
			ancestor.info='v'
		ancestor=ancestor.parent
		
			

def add_sibling(tree,sibling,g):
	if sibling.name!='0' and sibling.name!='1':
		g.add_edge(tree.name,sibling.name)
	else:
		for child in sibling.children:
			if child!=None:
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


	print (" ")

	# input option 2:
	names =['a','b','c','d','e','f','x']
	neighbors = [[],['a'] ,[],  ['a','b','c'], ['a','b','c'], ['a','b','c'] , ['f','a','d','e']]

	#create_cotree_2(names,neighbors)
	print (" ")

	
	#k=next_partition([1,1,1,1,1,1,1])
	#print k
	#i=1
	#while k!=None:
		#k=next_partition(k)
		#print k
		#i=i+1
	#print i
	print (" ")
	# n= number of vertices of the graph
	n=10
	co_gen=cograph_generator(n)
	false_counter=0;
	for tree in co_gen:
		#tree.print_tree()
		g=Graph(n)
		tree_to_graph(tree,g)
		cotreee=create_cotree_1(g)
		false_flag=tree.tree_equality(cotreee)
		if false_flag!=None:
			false_counter+=1
		#print " "
	print "false counter"
	print false_counter	
