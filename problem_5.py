#!/usr/bin/env python
# coding: utf-8

# In[88]:


from datetime import datetime
import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def get_utc_time(self):
        return datetime.utcfromtimestamp(float(self.timestamp))
        
    def calc_hash(self):
        encodedData = hashlib.sha256(self.data.encode('utf-8'))
        encodedTimestamp = hashlib.sha256(self.timestamp.encode('utf-8'))
        encodedData.hexdigest()
        encodedTimestamp.update(encodedData.digest())
        if(self.previous_hash is not None):
            encodedTimestamp.update(self.previous_hash.hash.encode("utf-8"))
        return encodedTimestamp.hexdigest()
    
class BlockChain:
    
    def __init__(self):
        self.tail = None
        
    def add_block(self, data):
        if self.tail is None:
            self.tail = Block(str(datetime.now().timestamp()), data, None)
        else:
            tail = self.tail
            block = Block(str(datetime.now().timestamp()), data, tail)
            self.tail = block
    
    def print_blockchain(self):
        tail = self.tail
        while tail is not None:
            print("<-",tail.data, tail.hash, tail.get_utc_time())
            tail = tail.previous_hash
            
def test_blockchain():
    blockchain = BlockChain()
    blockchain.add_block("hey")
    blockchain.add_block("ho")
    blockchain.add_block("lets")
    blockchain.add_block("go")
    blockchain.print_blockchain()
    
test_blockchain()


# In[ ]:




