Modular Decomposition of co-graphs

example.py

    --> Input option #1: a sage graph (co-graph)
    
        Output: Its modular decomposition tree (co-tree)

                           (1)
                          /   \
                       (0)     (0)
                       / \    / | \
                    (1)   c  d  e  f 
                   / \
                  a  (0)
                     / \
                    b   x
                                                           
          (1): series nodes 
          (0): parallel nodes
      
      --> Input option #2: a nested list with nodes and their adjacent nodes ([nodes, neighbors])
       
      --> Using cograph generator compute all cotrees with n nodes and check that the function cograph_modular_decomposition              computed it correctly



      


Cograph_modular_decomposition.py

      -- Function that given a co-graph, computes its co-tree by adding one-by-one its vertices
      -- Input options:
      
            1) A sage graph / python dictionary with nodes and ALL their neighbors
            2) A list with the nodes and a nested list with their "eliminated neighbors", meaning that a node can have as 
               neighbors only the nodes that are adjacent and precede in the given order (see main example)
               
       -- Cograph_recognition.py: Functions: is_cograph(), has_no_p4_path() and has_no_p4_path_2()
            check if in any subgraph of 4 vertices there is a path. If so, the graph is not a co-graph, otherwise it is a cograph.
            
     
       
       
Cograph_generator.py


       -- Creates all co-graphs with n nodes


Trees.py


  -- Tree constructor
  
  
  -- Function: is_cograph() 
  
      recursive function that checks if the graph is a cograph. If so, it calls the function update_cotree 
      
      input parameters: -- tree: the existing co-tree
                        -- x : inserting node
                        -- S : set of adjacent nodes of x
                        -- flag_mixed : initially 0 (there are no mixed nodes)
                                        1 (if there is at least one mixed node)
                                        2 (if it is not a co-graph)
                                        
  -- Function: update_cotree()
  
      adds node x to the existing co-tree 
      
      input parameters: -- tree: the existing co-tree
                        -- x : inserting node
                        -- S : set of adjacent nodes of x
                        -- sum_adj : # of children of tree that are adjacent to x
                        -- sum_non_adj: # of children of tree that are non adjacent to x

-- Function: print_tree()

    prints tree nodes. Prints '1' for series nodes and '0' for parallel nodes
