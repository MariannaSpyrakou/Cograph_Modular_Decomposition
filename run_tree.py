from Trees import Tree
#t1=Tree('0')
#t2=Tree('0')
#t3=Tree('1')
#t4=Tree('c')
#t=Tree('1',[t1,t2])
t = Tree('1', [Tree('0',[Tree('c'),Tree('1',[Tree('a'),Tree('b')])]),Tree('0',[Tree('d'),Tree('e'),Tree('f')])])
#Tree.add_child(t1,t4)
#Tree.add_child(t1,t3)
#Tree.add_child(t3,Tree('a'))
#Tree.add_child(t3,Tree('b'))
#Tree.add_child(t2,Tree('d'))
#Tree.add_child(t2,Tree('e'))
#Tree.add_child(t2,Tree('f'))

#Tree.add_child(t.children[2],Tree('e',[Tree('z'),Tree('w')]))
s=['a','f','d','e']
flag_mixed=[0]
Tree.is_cograph(t,'x',s,flag_mixed)
print flag_mixed[0]
print "Change a line"
Tree.make_info_None(t)
print t.info
print "Change a line"
Tree.print_tree(t)

