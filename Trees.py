class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
	self.info = None
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


    def __str__(self):
        return str(self.name)

    def make_info_None(tree):
	if tree==None: return
	for child in tree.children:
		Tree.make_info_None(child)
	tree.info=None

    # is_cograph: function that ckecks if (G+x) is a cograph
    # input: tree, x: inserting node, S: set of adjacent nodes of x, flag_mixed: 
    # flag_mixed= 0: no mixed nodes, 
    #             1: at least one mixed node 
    #             2: not a co-graph 

    # node.info = None: non adjancent, 
    #             1: adjancent, 
    #             2: adjancent, 
    #             3: mixed, 
    #             4: empty, 
    #             5: insertion node

    # node.name: '1': series
    #            '0':parallel
    #            nodes name if it is leaf 

    def is_cograph(tree,x,S,flag_mixed):
    	if tree == None: return
	for child in tree.children:
    		Tree.is_cograph(child,x,S,flag_mixed)
	if S.count(tree.name)>0:
		tree.info = 1
	sum_adj=0
	sum_non_adj=0
	for child in tree.children:
		if child.info == 3 or child.info==5:
			tree.info = 3
		elif child.info == 1 or child.info == 2:
			if sum_non_adj>0:
				if flag_mixed[0]==0:
					tree.info = 5
					flag_mixed[0]=1
					sum_adj=sum_adj+1
				elif flag_mixed[0]==1:
					tree.info =3
					flag_mixed[0]=2
					return
			else:
				sum_adj=sum_adj+1
		elif child.info == None or child.info == 4:
			if sum_adj>0:
				if flag_mixed[0]==0:
					tree.info=5
					flag_mixed[0]=1
					sum_non_adj=sum_non_adj+1
				elif flag_mixed[0]==1:
					flag_mixed[0]=2
					return
			else:
				sum_non_adj=sum_non_adj+1
	if tree.info == None:
		if sum_adj>0:
			tree.info = 2
		elif sum_non_adj>0:
			tree.info = 4	
	if tree.name=='1' and tree.info==3 and sum_non_adj>0:
		flag_mixed[0]=2
		return
	if tree.name=='0' and tree.info==3 and sum_adj>0:
		flag_mixed[0]=2
		return
	if tree.info==5:
		Tree.update_cotree(tree,x,S,sum_adj,sum_non_adj)
    	


# function that updates the cotree and inserts node x

# input: tree: existing cotree
#	 x : node to add in the cotree
#	 S : set of adjacent nodes of x
# 	 sum_adj : # of children of tree adjacent to x
#	 sum_non_adj : # of children of tree non adjacent to x
    def update_cotree(tree,x,S,sum_adj,sum_non_adj):
	if tree.info==5:
		if tree.name=='0':
			# parallel node
			if sum_adj==1:
				# one adjacent node 
				i=0
				for child in tree.children:
					if child.info==1:
						this_child=child
						tree.children[i]=Tree('1',[this_child,Tree(x)])
						break
					if child.info==2:
						Tree.add_child(child,Tree(x))
						break
					i=i+1

			else:
				#more than one adjacent node
				t1=Tree('0')
				Tree.add_child(tree,Tree('1',[t1,Tree(x)]))
				i=0
				for child in tree.children:
					if child.info==1 or child.info==2:
						tree.children[i]=None
						Tree.add_child(t1,child)
					i=i+1			
		else:
			# tree.name=='1'			
			# series node check the cases
			if sum_non_adj==1:
				#one non adjacent node
				i=0
				for child in tree.children:
					if child.info==None:
						this_child=child
						tree.children[i] = Tree('0',[this_child,Tree(x)])
						break
					if child.info==4:
						Tree.add_child(child,Tree(x))
						break
					i=i+1
			else:
				#more than one non adjacent node
				t1=Tree('1')
				Tree.add_child(tree,Tree('0',[t1,Tree(x)]))
				i=0
				for child in tree.children:
					if child.info== None or child.info==4:
						tree.children[i]=None
						Tree.add_child(t1,child)
	elif tree.info==2:
		# x is connected to all vertices of G
		Tree.add_child(tree,Tree(x))
	elif tree.info==4: 
		# tree has empty label
		if tree.children[1]==None:
			# G is disconnected
			Tree.add_child(tree.children[0],Tree(x))
		else:
			# G is connected but G is disconnected
			i=0
			t2=Tree('1')
			t1=Tree('0',[t2,Tree(x)])
			Tree.add_child(tree,t1)
			for child in tree.children:
				tree.children[i]=None
				Tree.add_child(t2,child)
				i=i+1
	return	

# print_tree: function that traverses the tree in postorder and prints it

    def print_tree(tree):			
	if tree == None: return
	for child in tree.children:
    		Tree.print_tree(child)				
	print tree.name


