#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, root):
        self.root = root
        
def huffman_encoding(data):
    frequencies = charactersFrequencies(data)
    sortedFrequenciesList = sortFrequencies(frequencies)
    mappedSortedFrequencies =  list(map(lambda x: Node(x[0], x[1]), sortedFrequenciesList))
    tree = None
    
    while(len(mappedSortedFrequencies) > 1):
        firstElement = mappedSortedFrequencies.pop(0)
        secondElement = mappedSortedFrequencies.pop(0)
        rootNode = Node(firstElement.value + secondElement.value, firstElement.value + secondElement.value)
        rootNode.left = firstElement
        rootNode.right = secondElement
        insertElementIntoList(rootNode, mappedSortedFrequencies)
        if(len(mappedSortedFrequencies) == 0):
            tree = Tree(rootNode)
    
    if(tree is None):
        tree = Tree(Node(1, 1))
        tree.root.left = Node(data[0], 1)
        
    encodedChars = dict()
    encodeTree(tree.root, "", encodedChars)
    encodedString = ""
    for char in data :
        encodedString += encodedChars[char]
    return encodedString , tree
    pass

def insertElementIntoList(node, sortedFrequencies):
    for index, element in enumerate(sortedFrequencies):
        if node.value < element.value:
            sortedFrequencies.insert(index, node)
            break
        elif(index == len(sortedFrequencies) -1):
            sortedFrequencies.append(node)
            break
            
def encodeTree(root, string, hoffmanEncodes):
    if(root.right is None and root.left is None):
        hoffmanEncodes[root.key] = string
    else:
        if(root.left is not None):
            encodeTree(root.left, string + "0", hoffmanEncodes)
        if(root.right is not None):
            encodeTree(root.right, string + "1", hoffmanEncodes)
            
        

def huffman_decoding(data,root):
    def decode(data, root, index, decodedString):
        if(root.left is None and root.right is None):
            decodedString += root.key
            return index, decodedString
        elif data[index] == "0":
            return decode(data, root.left, index + 1, decodedString)
        else:
            return decode(data, root.right, index + 1, decodedString)
    index = 0
    decodedString = ""
    while(index <= len(data) -1):
        index, decodedString = decode(data, root, index, decodedString)
    return decodedString
    pass

def charactersFrequencies(data):
    frequencies = dict()
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies

def sortFrequencies(data):
    items =  list(data.items())
    items.sort(key=lambda x: x[1])
    return items

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is a word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree.root)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    

