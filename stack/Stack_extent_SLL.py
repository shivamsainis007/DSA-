class node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class stack(node):
    def __init__(self, ):
        self.top=None
        self.count=0
    
    def isempty(self):
        if self.top==None:
            print("stcak is empty")
            return
    
        
    def push(self,data):
        new_node=node(data,self.top)
        # new_node.next=self.start
        self.top=new_node
        self.count+=1
    def pop(self):
        if self.isempty():
            return
        else:
            print("delete item is : ",self.top.data)
            self.top=self.top.next
            return
    
    def peek(self):
        if self.isempty():
            return
        else:
            print("peek item is :", self.top.data)
    def size(self):
        if self.isempty():
            return
        else:
            print("size of stack is : ",self.count)    
    def printStack(self):
        if self.isempty():
            return
        else:
            temp=self.top
            print("stack item is : " ,end=" ")
            while temp :
                print(temp.data,end=" ") 
                temp=temp.next
                
            print("\n")  
            
s1=stack()
s1.push(10)
s1.push(20) 
s1.push(30)
s1.size() 
s1.peek() 
s1.pop()
s1.peek() 
s1.printStack()   
                    
        