#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    elements = set()
    node = llist_1.head
    new_list = LinkedList()
    while node:
        if node.value not in elements:
            elements.add(node.value)
            new_list.append(node)
            
        node = node.next
    
    node = llist_2.head
    while node:
        if node.value not in elements:
            elements.add(node.value)
            new_list.append(node)
            
        node = node.next
    return new_list 
    pass

def intersection(llist_1, llist_2):
    elements = set()
    node = llist_1.head
    new_list = LinkedList()
    while node:
        if node.value not in elements:
            elements.add(node.value)
        node = node.next
    
    node = llist_2.head
    while node:
        if node.value in elements:
            elements.remove(node.value)
            new_list.append(node)
        node = node.next
            
    return new_list
    pass

def test1():
    print("test 1")
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print ("union",union(linked_list_1,linked_list_2))
    print ("intersection",intersection(linked_list_1,linked_list_2))
    
def test2():
    print("test 2")
    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print ("union", union(linked_list_3,linked_list_4))
    print ("intersection",intersection(linked_list_3,linked_list_4))
    
def test3():
    print("test 3")
    # Test case 3
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print ("union", union(linked_list_3,linked_list_4))
    print ("intersection",intersection(linked_list_3,linked_list_4))
    
def test4():
    print("test 4")
    # Test case 4
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print ("union", union(linked_list_3,linked_list_4))
    print ("intersection",intersection(linked_list_3,linked_list_4))
    
test1()
test2()
test3()
test4()

