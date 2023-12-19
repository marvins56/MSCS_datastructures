public list<object> DijkstrasAlgorithm(Grap graph, Node start) {
    
    Map<Node, int> totalCosts = new Map<>();
    Map<Node,Node>prevNodes = new Map<>();
    MinPQ<Node>minPQ = new MinPQ<>();
    Set<Node> visited = new Set<>();
    
    totalCosts.put(start, 0); // set start node cost to 0
    minPQ.add(start); // Add start node to minPQ
    
    
    for (Node node : graph.nodes()) {
            if (node !=start) {       // for all nodes other than start
             totalCosts.put(node, INFINITY);  // set all lengths to infinity  at first, since any path we find must have lenght <infinity
             }
            } 
    
    
    while (!minPQ.isEmpty()){           // main loop
          Node newSmallest = minPQ.deleteMin();  //Remove smallest item
          
          for (Node neigbor : newSmallest.neighbors()) {// check for neighbors
             
              if (!visted.contains(neighbors()) {    // check if visted
                                         
                 int altPath = totalCost.get(newSmallest)  + distance(newSmallest,neigbor);// make a path, contain new path distance
                 
                 if (altPath < totalCosts.get(neighbor)){       // check if new path is better
                                            
                                                         
                    totalCosts.put(neighbor,altPath); //update path lenght for neighbor
                    prevNodes.put(neighbor,newSmallest); // update previous node to node we just removed
                    
                    minPQ.decreasePriority(neighbor, altpath); // update priority in minPQ
                    }
                     
                 
                 
                 }
                  
           }
          
    }
      
                  
    list<object> results = new List<>();
    results.add(totalCosts): results.add(prevNodes);
    return results; // Results contains: totalCosts=map of each node to its shortest path lenght from start node;
                    // and prevNode=map of each node to node it came from
                  
     }
    
    