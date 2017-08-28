# Modular Decomposition of graphs and digraphs

### GSoC 2017,  SageMath

### Mentors: Dima Pasechnik, David Coudert

<br>

My name is Maria Ioanna Spyrakou and I have been working on modular decomposition of cographs and digraphs for SageMath in Google summer of code 2017. 

As part of the project, I implemented in python code for:
<ul> 
  <li> modular decomposition of cographs, according to [1],[2],  </li>
  <li> a cograph generator, according to [3], and </li>
  <li>modular decomposition of digraphs according to [4],[5]. </li>
</ul>  
     
<br>     
     
## About Modular Decomposition
Modular decomposition of a graph is a decomposition into subsets of vertices, called modules, such that every vertex of the module has uniform relationship with every other vertex outside the module. Modular decomposition of a graph can be represented as a rooted tree, where the leaves correspond to vertices and the internal nodes (more precisely: the subgraph defined by the children of each internal node) correspond to the strong modules (i.e. the modules that do not overlap any other module). The importance of modular decomposition is that it represents all possible ways to decompose a graph into quotients and factors and some of its applications include: transitive orientation, weighted maximum clique, coloring, graph drawing and in many combinatorial optimization problems. 

In this project we introduce the first open-source implementation of modular decomposition of co-graphs as well as the first open-source Python implementation of modular decomposition of digraphs. 

<br>

## Modular Decomposition of Cographs:

Cographs (or totally decomposable graphs) are defined as the class of graphs formed from a single vertex under the closure of the operations of union and complement [1]. Equivalently cographs are the P4-free graphs, that is the graphs that have no induced path on 4 vertices. 
Every cograph has unique modular decomposition and  is defined by the properties of its modular decomposition. As a result, each internal node of the cotree (i.e. modular decomposition tree of a cograph) corresponds either to union or join of subgraphs defined by the children of that node. Those nodes will be called series (node label: '1') or parallel (node label '0') respectively. 

<br>

### Python implementation:

Given a graph in sage structure or an adjacency list of the graph, returns the modular decomposition tree (cotree), if the input graph is cograph. 

#### Functions included:
<ul>
    <li> Cograph_recognition: Contains 3 functions that test if the input graph is a cograph, by searching if there is a P4 path on any induced subgraph on 4 vertices.  </li>
    <li> Cograph_modular_decomposition: if the input graph is a cograph, then construct its cotree by adding incrementally one by one its nodes. When all nodes are added the modular decomposition tree is returned. </li>
</ul>

For the correctness of the code, the code was tested on all cographs with n=3,....,16 nodes as follows.

<br>

### Cograph generator:
Given the number of nodes n, generates all cotrees that correspond to all cographs with n nodes. 
<ul>
The example includes the testing of the modular decomposition code: 
<li>Generate all cotrees with n=3,..,16 nodes, using the cograph_generator.</li>
<li>Find their corresponding cographs.</li>
<li>Run the modular decomposition code for each cograph and test if the output matches the initial cotree. </li>
</ul>

<br>

## Modular Decomposition of Digraphs: 

Python implementation:
Github: https://github.com/MariannaSpyrakou/Digraphs_modular_decomposition

Given a digraph in sage structure, returns the modular decomposition tree. 

<br>

## References:

[1] D. G. Corneil, Y. Perl, L. K. Stewart, A linear recognition algorithm for cographs, SIAM Journal on Computing, Vol. 14, No. 4 : pp. 926-934, 1985

[2] M. Habib, C. Paul, A Survey on Algorithmic Aspects of
Modular Decomposition, Computer Science Review Volume 4, Issue 1, Pages 41-59, February 2010

[3] Á. A. Jones, F. Protti, R. R. Del-Vecchio, Cograph generation with linear delay, arXiv:1612.05827v1, 2016

[4] R. M. McConnell, F. de Montgolfier. Linear-time modular decomposition of directed graphs, Discrete Applied Mathematics, Volume 145, Issue 2, 2005

[5] C. Capelle, M. Habib, F. de Montgolfier. Graph Decompositions and Factorizing Permutations. Discrete Mathematics and Theoretical Computer Sciences 5, 2002


<br>


## Appendix: Modules Description


#### example.py

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




#### Cograph_modular_decomposition.py

      -- Function that given a co-graph, computes its co-tree by adding one-by-one its vertices
      -- Input options:
      
            1) A sage graph / python dictionary with nodes and ALL their neighbors
            2) A list with the nodes and a nested list with their "eliminated neighbors", meaning that a node can have as 
               neighbors only the nodes that are adjacent and precede in the given order (see example)
               
#### Cograph_recognition.py: 

    -- Functions: is_cograph(), has_no_p4_path() and has_no_p4_path_2()
            check if in any subgraph of 4 vertices there is a path. If so, the graph is not a co-graph, otherwise it is a cograph.
            
      
#### Cograph_generator.py


       -- Creates all co-graphs with n nodes


#### Trees.py


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
