import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from linklist.SLL import sll
class stack(sll):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.count = 0 
    def isEmpty(self):
        self.is_empty()
        
    def push(self,data):
        self.insert_at_start(data)
        self.count+=1
        
    def pop(self):
        self.delete_at_first()
        self.count-=1
        
    def peek(self):
        print(self.start.item)
        
    def size(self):
        print(self.count)   
        
s=stack()
s.push(13)
s.push(14)
s.push(15)
s.pop()
s.peek()
s.size()

  