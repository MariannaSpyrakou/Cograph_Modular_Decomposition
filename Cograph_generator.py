from Trees import Tree

" Cograph Generation with linear delay (A. Jones, F. Protti, R. Vecchio)"


def next_partition(a):
	"""
	given a partition a (of number n) find the partition immediately next to a
	all partitions of 4 are: [1,1,1,1], [1,1,2],[1,3],[2,2] (in increasing order)
	next_partition([1,1,2])  is [1,3]
	"""	
	k=len(a)
	n=sum(a)
	if a[0] != (n//2):
		if a[k-1]-a[k-2]<=1:
			return a[:k-2]+[a[k-2]+a[k-1]]
		else: 	
			a[k-2]+=1
			a[k-1]-=1
			q=a[k-1]//a[k-2]
			r=a[k-1]%a[k-2]
			if q>1:
				return a[:k-2]+[a[k-2]]*q+[a[k-2]+r]
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
	for i in range(k):
		# add the i-th child of u
		if i<len(u.children):
			u.children[i]=Tree(a[i])
		else:
			u.add_child(Tree(a[i]))
		u.children[i].parent=u
		if a[i]>1:   # if i is not a leaf, then its children should be leaves 
			this_child=u.children[i] 
			for j in range(a[i]):
				this_child.add_child(Tree(1))	
	for i in range(k, len(u.children)):
		# If there are more "existing" children than we need to delete them  
		u.children[k]=None
		u.children.remove(None)
	
def find_pivot(T,pivot):
	"""
 	find_pivot(T,pivot): given a tree T and a list pivot it finds the pivot i.e. the first node in reverse postorder traversal
	that does not induce a maximum partition. 
	"""
	for child in reversed(T.children):
		if pivot==[]:
        		find_pivot(child,pivot)
	""" (Definition 9: pivot node)
	 if a node T is not a leaf, it does not induce a maximum partition 
	 and it is the first such node in the inverse postorder traversal, 
	 then it is the  PIVOT.
	
	 the maximum partition of u is [floor(u/2),ceil(u/2)]
 	"""
	
	i=T.name
	if pivot==[] and T.name!=1 and ((i//2!=T.children[0].name) or ((i//2+i%2)!=T.children[1].name)): 
		pivot.append(T)
		T.info='p'
	 

def next_tree(T):
	"""
	Given the co-tree T, find the next cotree 
	"""
	pivot=[]
	find_pivot(T,pivot)
	if pivot!=[]: # If there is a pivot, then we can find the next tree
		"find the existing partition that is induced by pivot"
		partition=[]
		for i in pivot[0].children:
			partition.append(i.name) 
		b=next_partition(partition) # finds the next partition induced by the subtree pivot[0]
		rebuild_node(pivot[0],b) # changes the subtree "pivot[0]"
		x=pivot[0]
		while True:
			if x.parent!=None:
				ancestor=x.parent
				# modify the bigger siblings of node x
				is_bigger_sibling=False
				for y in range(len(ancestor.children)) : # y = all siblings of x
					this_child=ancestor.children[y]
					if this_child.info=='p':
						is_bigger_sibling=True
					if is_bigger_sibling==True and this_child.info!='p': # true only for bigger siblings of x
						if x.name==this_child.name: 
							temp=Tree(x.name)
							x.copy_tree(temp)
							ancestor.children[y]=temp  #copy subtree T(x) in T(y)
							temp.parent=ancestor
						else:
							c=[]
							for i in range(ancestor.children[y].name):
								c.append(1)
							rebuild_node(ancestor.children[y],c)
				# set x= parent of x 
				x.info=None # reset the pivot mark
				x=ancestor
				if x==None:
					break
				x.info='p' # parent gets the pivot mark	
			else: 
				break
		return True
	else:  # If there is no pivot, then there is no other tree
		return False



def cograph_generator(n):
	""" 
	Input integer n
 	Output, all cographs with n nodes
	"""
	if n>=2:
		# Construct the minimum tree
		T=Tree(n)
		for j in range(n):
			T.add_child(Tree(1))
		i=1
		flag=True
		while flag:
			## T corresponds to 2 cotrees: one with '0' root and one with '1' root
			tree1=Tree(T.name)
			T.copy_tree(tree1)
			tree0=Tree(T.name)
			T.copy_tree(tree0)
			# tree 1 has root '1'
			counter=[0]
			change_label(tree1,1,counter)
			# tree 0 has root '0'
			counter=[0]
			change_label(tree0,0,counter)
			tree00=Tree('1')
			tree00.add_child(tree0)
			yield tree1
			yield tree00
			flag=next_tree(T) # Find the next tree. return False if there is no other Tree
			if not flag:
				break
			#print(" ")
			i+=1
		print ("The number of cotrees is: ",2*i)
	else:
		print ("Number of vertices must be >=2")
	

def change_label(tree,status,counter):
	"""
	Given the the co-tree tree,that each node has aslabel the number of its children, 
	change the label into "0" for parallel nodes, "1" for series nodes and a "node-number" for the leaves/nodes
	
	counter: counts the total nodes of the tree, so that each one gets a unique label/name.
	status: counts the "level" of each node, so that the internal nodes get the label series/parallel.
	"""
	if tree.name!=1:
		tree.name=str(status%2)
	else:
		tree.name=counter[0]
		counter[0]+=1
	for child in tree.children:
		if child!=None: 
			change_label(child,status+1,counter)
