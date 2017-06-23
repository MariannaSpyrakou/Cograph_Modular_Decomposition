from Trees import Tree
t = Tree('1', [Tree('0',[Tree('c'),Tree('1',[Tree('a'),Tree('b')])]),Tree('0',[Tree('d'),Tree('e'),Tree('f')])])
s=['a','f','d','e']
flag_mixed=[0]
Tree.is_cograph(t,'x',s,flag_mixed)
Tree.make_info_None(t)
if flag_mixed==0:
	Tree.update_cotree(t,'x',s,0,0)
Tree.print_tree(t)

