Modular Decomposition of co-graphs

example_1.py

    input: the below co-tree 
  
    output: the updated co-tree when adding node x, adjacent to a,d,e,f
    

                       (1)                                       (1)
                      /   \                                     /   \
                   (0)    (0)              -->               (0)     (0)
                   / \    / | \          output:             / \    / | \
                 (1)  c   d  e  f                         (1)   c  d  e  f 
                 / \                                      / \
                a   b                                    a  (0)
                                                            / \
                                                           b   x
                                                           

main_example.py

      --full construction of the above co-tree, given the initial cograph


create_cotree.py

      -- Function that given a co-graph, computes its co-tree by adding one-by-one its vertices
      -- Input options:
      
            1) A sage graph / python dictionary with nodes and ALL their neighbors
            2) A list with the nodes and a nested list with their "eliminated neighbors", meaning that a node can have as 
               neighbors only the nodes that are adjacent and precede in the given order (see main example)


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

    prints tree nodes in postorder traversal
