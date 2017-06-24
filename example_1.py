from Trees import Tree

# add node x that is adjacent to a,f,d,e to the cotree t 
# output: the updated cotree in postorder tree traversal

t = Tree('1', [Tree('0',[Tree('c'),Tree('1',[Tree('a'),Tree('b')])]),Tree('0',[Tree('d'),Tree('e'),Tree('f')])])
s=['a','f','d','e']
flag_mixed=[0]
Tree.is_cograph(t,'x',s,flag_mixed)
Tree.make_info_None(t)
if flag_mixed==0:
	Tree.update_cotree(t,'x',s,0,0)
Tree.print_tree(t)

