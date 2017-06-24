from Trees import Tree

def create_cotree(g):
	cotree=Tree('1')
	i=0
	for node in g:
		if i==0:
			first_node=node
		elif i==1:
			if g[node].count(first_node):
				Tree.add_child(cotree,Tree(first_node))
				Tree.add_child(cotree,Tree(node))
			else:
				tree0=Tree('0',[Tree(first_node),Tree(node)])
				Tree.add_child(cotree,tree0)
		else:
			flag_mixed=[0]
			Tree.is_cograph(cotree,node,g[node],flag_mixed)
			if flag_mixed[0]==0:
				Tree.update_cotree(cotree,node,g[node],0,0)
			elif flag_mixed[0]==2:
				print "The input graph is not a co-graph"
				return
			Tree.make_info_None(cotree)
		i=i+1
	
	Tree.print_tree(cotree)
	return


d = {'a': ['b','d','e','f','x'],
         'b': ['a','f','e','d'], 'c': ['f','e','d'],
         'd': ['a','b','c','x'], 'e': ['a','b','c','x'],
         'f': ['a','b','c','x'] , 'x': ['f','a','d','e']
         }
create_cotree(d)
