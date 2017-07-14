from __future__ import print_function
class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
	self.name = name
	self.children = []
	self.info = None
	self.parent = None
        if children is not None:
		for child in children:
			self.add_child(child)
			child.parent=self
    def __repr__(self):
	return self.name
    def add_child(self, node):
	assert isinstance(node, Tree)
	self.children.append(node)
	node.parent=self

    def __str__(self):
	return str(self.name)

    def reset_info(self):
	for child in self.children:
		if child!=None:
			child.reset_info()
	self.info = None
	return
   
	
    def is_cograph(self,x,S,flag_mixed):
	"""
    	is_cograph: function that ckecks if (G+x) is a cograph
     	input: tree, x: inserting node, S: set of adjacent nodes of x, flag_mixed: 
     	flag_mixed= 0: no mixed nodes, 
        	    1: at least one mixed node 
               	    2: not a co-graph 

     	node.info = None: non adjancent, 
                    1: adjancent, 
                    2: adjancent, 
                    3: mixed, 
                    4: empty, 
                    5: insertion node

     	node.name: 1: series
                   0:parallel
                   nodes name if it is leaf 
    	"""
	for child in self.children:
		if child!=None:
    			child.is_cograph(x,S,flag_mixed)
	if self.name in S:
		self.info = 1
	sum_adj=0
	sum_non_adj=0
	for child in self.children:
		if child != None:
			if child.info == 3 or child.info==5:
				# tree has a mixed child
				self.info = 3
			elif child.info == 1 or child.info == 2:
				# tree has an adjacent child
				if sum_non_adj>0:
					# tree has non adjacent child/children too
					if flag_mixed[0]==0:
						# the first mixed node
						self.info = 5
						flag_mixed[0]=1
						sum_adj=sum_adj+1
					elif flag_mixed[0]==1:
						#not possible to be the second node that has both adjacent and non adjacent children
						if self.info==5:
							sum_adj=sum_adj+1
						else:
							self.info =3
							flag_mixed[0]=2
							return
				else:
					# count the number of adjacent nodes
					sum_adj=sum_adj+1
			elif child.info == None or child.info == 4:
				# tree has a non adjacent child
				if sum_adj>0:
					# tree has adjacent child/children too
					if flag_mixed[0]==0:
						# the first mixed node
						self.info=5
						flag_mixed[0]=1
						sum_non_adj=sum_non_adj+1
					elif flag_mixed[0]==1:
						if self.info==5:
							sum_non_adj=sum_non_adj+1
						else:
							#not possible to be the second node that has both adjacent and non adjacent children
							flag_mixed[0]=2
							return
				else:
					# count the number of non-adjacent nodes
					sum_non_adj=sum_non_adj+1
	if self.info == None:
		if sum_adj>0:
			# no mixed nodes, only adjacent nodes
			# tree --> adjacent node
			self.info = 2
		elif sum_non_adj>0:
			# no mixed nodes, only non-adjacent nodes
			# tree --> empty node
			self.info = 4	
	if self.name=='1' and self.info==3 and sum_non_adj>0:
		#not a co-tree case
		flag_mixed[0]=2
		return
	if self.name=='0' and self.info==3 and sum_adj>0:
		# not a co-tree case
		flag_mixed[0]=2
		return
	if self.info==5:
		self.update_cotree(x,S,sum_adj,sum_non_adj)
		# If tree it is the first mixed node, then update that part of the co-tree by adding x
    	


    def update_cotree(self,x,S,sum_adj,sum_non_adj):
	"""
 	function that updates the cotree and inserts node x

 	input: tree: existing cotree
	 	x : node to add in the cotree
	 	S : set of adjacent nodes of x
	 	sum_adj : # of children of tree adjacent to x
	 	sum_non_adj : # of children of tree non adjacent to x
	"""	
		
	if self.info==5:
		if self.name=='0':
			# parallel node
			if sum_adj==1:
				# one adjacent node 
				i=0
				for child in self.children:
					if child.info==1:
						this_child=child
						self.children[i]=Tree('1',[this_child,Tree(x)])
						break
					if child.info==2:
						child.add_child(Tree(x))
						break
					i=i+1

			else:
				#more than one adjacent node
				t1=Tree('0')
				self.add_child(Tree('1',[t1,Tree(x)]))
				i=0
				for child in self.children:
					if child.info==1 or child.info==2:
						self.children[i]=None
						t1.add_child(child)
					i=i+1			
		else:
			# tree.name=='1'			
			# series node
			if sum_non_adj==1:
				# one non adjacent node
				i=0
				for child in self.children:
					if child!=None:
						if child.info==None:
							this_child=child
							self.children[i] = Tree('0',[this_child,Tree(x)])
							break
						if child.info==4:
							child.add_child(Tree(x))
							break
					i=i+1
			else:
				# more than one non adjacent node
				t1=Tree('1')
				i=0
				for child in self.children:
					if child!=None:
						if child.info== None or child.info==4:
							self.children[i]=None
							t1.add_child(child)
					i=i+1
				self.add_child(Tree('0',[t1,Tree(x)]))
	elif self.info==2:
		# x is connected to all vertices of G
		self.add_child(Tree(x))
	elif self.info==4: 
		# tree has empty label
		if self.children[1]==None:
			# G is disconnected
			Tree.add_child(self.children[0],Tree(x))
		else:
			# G is connected but G+x is disconnected
			i=0
			t2=Tree('1')
			t1=Tree('0',[t2,Tree(x)])
			for child in self.children:
				self.children[i]=None
				t2.add_child(child)
				i=i+1
			self.add_child(t1)
	return	


    def print_tree(self):
	" print_tree: for every node its subtree is inside brackets [ ]"
	if self.name=='1' or self.name=='0':
		print ('[',self.name,' ',sep='', end='')
	else:
		print ('(',self.name,sep='', end='')		
	for child in self.children:
		if child!=None:
    			child.print_tree()	
	if self.name=='1' or self.name=='0':
		print ('],',end=' ')
	else:	
		print (')',end=' ')			
	return



    def print_tree_postorder(self):
	" print_tree_postorder: function that traverses the tree in postorder and prints it"
	for child in self.children:
		if child!=None:
    			child.print_tree()				
	print (self.name)
	return
