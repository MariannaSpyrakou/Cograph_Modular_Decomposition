Modular Decomposition of co-graphs

example_1.py

  input: the below cotree 
  output: the updated cotree when adding node x, adjacent to a,d,e,f

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
      --full construction of the above cotree, given the initial cograph


create_cotree.py
      -- Function that given a cograph, computes its cotree by adding one-by-one its vertices


Trees.py

contains:
  -- Tree constructor
  
  -- Function: is_cograph() 
      recursive function that checks if the graph is a cograph. If so, it calls the function update_cotree 
      
      input parameters: -- tree: the existing cotree
                        -- x : inserting node
                        -- S : set of adjacent nodes of x
                        -- flag_mixed : initially 0 (there are no mixed nodes)
                                        1 (if there is at least one mixed node)
                                        2 (if it is not a co-graph)
                                        
  -- Function: update_cotree()
      adds node x to the existing co-tree 
      
      input parameters: -- tree: the existing cotree
                        -- x : inserting node
                        -- S : set of adjacent nodes of x
                        -- sum_adj : # of children of tree that are adjacent to x
                        -- sum_non_adj: # of children of tree that are non adjacent to x

-- Function: print_tree()
    prints tree nodes in postorder traversal
