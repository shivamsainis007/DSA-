class stack():
    def __init__(self  ):
        self.list=[]
    
    def push(self, data):
        self.list.append(data)
        
    
    def is_empty(self):
        if len(self.list)==0:
            print("stack is empty")
            return
    
    
    def pop(self):
        if  self.is_empty():
           return
            
        deleteItem=self.list[-1]
        print("deleted item is : ",deleteItem)
        return self.list.pop()
    
    
    def peek(self):
        if self.is_empty():
            return 
        print("peek item is : ",self.list[-1])
        
    def size(self):
        if self.is_empty():
            return
        print("size of stack",len(self.list))    
    
    def printstack(self):
        if self.is_empty():
            print("stack is empty")
            return
        
        print("stack item:",end=" ")
        for i in range(len(self.list) - 1, -1, -1):
            print(self.list[i],end=" ")
            
            
        print('\n')
s=stack()          
s.push(15)
s.push(16)
s.push(17)
s.push(18)
s.push(19)
s.printstack()
s.pop()
s.peek()
s.size()
# s.pop()
# s.pop()
s.printstack()
          
    