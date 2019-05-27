#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, key,value):
        node = Node(key, value)
        if(self.head is None):
            self.head = node
            self.tail = self.head
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        return node
            
    def dequeue(self):
        dequeuedNode = self.head
        if(self.head == self.tail):
            self.head = None
            self.tail = None
        if(self.head is not None):
            self.head = self.head.next
            self.head.previous = None
        return dequeuedNode
        
    def remove_node(self, node):
        if(node.previous is None and node.next is None):
            self.head = None
            self.tail = None
        elif(node.previous is None):
            self.head = node.next
            self.head.previous = None
        elif(node.next is None):
            self.tail = node.previous
            self.tail.next = None
        else:
            node.previous.next = node.next 
            node.next.previous = node.previous
            node = None
            
        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.queue = Queue()
        pass

    def get(self, key):
        if(key in self.cache):
            self.queue.remove_node(self.cache[key])
            self.queue.enqueue(key, self.cache[key].value)
            return self.cache[key].value
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) == self.capacity:
            node = self.queue.dequeue()
            self.cache.pop(node.key, None)
            self.cache[key] = self.queue.enqueue(key, value)
        else:
            if key in self.cache:
                self.queue.remove_node(self.cache[key])
            node = self.queue.enqueue(key, value)
            self.cache[key] = node
        pass


def test1():
    print("test 1 init")
    checks = []
    single_value_cache = LRU_Cache(1)
    # value 1 with key 2 is on cache now
    single_value_cache.set(2, 1)

    #check if value is on cache
    checks.append(single_value_cache.get(2) == 1)

    # value should be removed from cache
    single_value_cache.set(3,4)

    #check if value is on cache
    checks.append(single_value_cache.get(2) == -1)

    #check if value is on cache
    checks.append(single_value_cache.get(3) == 4)
    
    if(all(checks[:sum(checks)]) == True):
        print("Passed")
    else:
        print("Failed")

def test2():
    print("test 2 init")
    checks = []
    cache = LRU_Cache(3)
    # value 1 with key 2 is on cache now
    cache.set(2, 1)

    #check if value is on cache
    checks.append(cache.get(2) == 1)

    # value should be removed from cache
    cache.set(3,4)

    #check if value is on cache
    checks.append(cache.get(2) == 1)

    #check if value is on cache
    checks.append(cache.get(3) == 4)
    
    cache.set(4, 6)
    
    #check if value is on cache
    checks.append(cache.get(2) == 1)

    #check if value is on cache
    checks.append(cache.get(3) == 4)
    
    #check if value is on cache
    checks.append(cache.get(4) == 6)
    
    #remove oldest element which should be 2
    cache.set(5, 9)
    
    #check if value is on cache
    cache.get((2) == -1)

    #check if value is on cache
    checks.append(cache.get(3) == 4)
    
    #check if value is on cache
    checks.append(cache.get(4) == 6)
    
    #check if value is on cache
    checks.append(cache.get(5) == 9)
    
    if(all(checks[:sum(checks)]) == True):
        print("Passed")
    else:
        print("Failed")
        
def test3():
    print("test 3 init")
    checks = []
    single_value_cache = LRU_Cache(2)
    # value 1 with key 2 is on cache now
    single_value_cache.set(2, 1)

    #check if value is on cache
    checks.append(single_value_cache.get(2) == 1)

    # handle collision
    single_value_cache.set(2,4)

    #1 value should be overriden
    checks.append(single_value_cache.get(2) == 4)

    single_value_cache.set(3,1)
    
    #check if value is on cache
    checks.append(single_value_cache.get(3) == 1)
    
    #check if value is on cache
    checks.append(single_value_cache.get(2) == 4)
    
    if(all(checks[:sum(checks)]) == True):
        print("Passed")
    else:
        print("Failed")

test1()
test2()
test3()

