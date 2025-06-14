class stack(list):
    
    def is_empty(self):
        if len(self)==0:
            print("stsck is empty")
            return
        
    def push(self,data): 
        self.append(data) 
        
        
    def pop(self):
        if self.is_empty():
            return
        else:
            delete=super().pop()
            print("delete item is :",delete)
            
    
    
    def peek(self):
        if self.is_empty():
            return
        print("peek item is :", self[-1])
    
    def size(self):
        if self.is_empty():
            return
        else:
            print("size of stcak is :",len(self))    
      
    def printlist(self):
        if self.is_empty():
            return
        
        
        print("stack item is : " ,end=" ")
        for i in range(len(self)-1,-1,-1):
            print(self[i],end=" ") 
        print("\n")  
s=stack()
s.push(1)
s.push(2)
s.push(3)  

s.printlist()
s.size()  
s.pop()
s.printlist()
s.size()
s.peek()