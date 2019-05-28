# Blockchain
a linked list is used for this problem since is easier to keep track of previous item on the blockchain, retrieval for the last block is O(1) and the first one O(n)

hash_function: the hash function is calculated ciphering the data with sha256 using utf-8 encode, then with the encoded data as hex string we add another encode that is the timestamp ciphering the data twice

hash function and inserting a block are O(1), printing the whole blockchain is O(n) 
