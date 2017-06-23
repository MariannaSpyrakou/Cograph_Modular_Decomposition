Modular Decomposition of co-graphs

run_file.py
contains test case of the modular decomposition for co-graphs

Test case: co-tree

                      (1)
                      /   \
                   (0)    (0)
                   / \    / | \
                 (1)  c   d  e  f
                 / \
                a   b
 
 inserted node: x,
 x neigbors: a,d,e,f
       
       
       
Trees.py
contains:
  -- Tree constructor
  -- Function: is_cograph() 
      recursive function that checks if the graph is a cograph and if yes it calls the function update_cotree 
  -- Function: update_cotree()
      adds node x to the co-tree.
