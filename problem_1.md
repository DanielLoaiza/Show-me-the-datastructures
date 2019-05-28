# LRU Cache
  Since its required O(1) for get and set operations this can be achieved mixing fast lookups of maps and quick access and  preserved order of  of queues.
  Storing nodes in the map we can retrieve easily previous and next values , so the time complexity for get and set operations is O(1)
  
  space complexity is a trade off here, since we are storing the values twice we have O(2n) which is finally O(n)
