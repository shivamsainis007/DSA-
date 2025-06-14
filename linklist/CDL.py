class node():
    def __init__(self,data=None,prev=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
class cdll():
    def __init__(self,start=None):
        self.start=start
        
    def is_empty(self):
        return self.start is None 
    
    
    def search(self,finder):
       
        temp=self.start
        while True:
            if temp.data==finder:
                return temp
            temp=temp.next
            if temp==self.start:
                break
            
        print(finder,":  is not found")    
        return     
            
       
    def insert_at_first(self,data):
        new_node=node(data)
        if self.is_empty():
            new_node.prev=new_node
            new_node.next=new_node
            self.start=new_node
        else:
            new_node.next=self.start 
            new_node.prev=self.start.prev
            self.start.prev.next=new_node
            self.start.prev=new_node
            self.start=new_node   
    
    def insert_at_last(self,data ):
        if self.is_empty():
            self.insert_at_first(data)
        else:
            new_node=node(data)
            new_node.prev=self.start.prev
            new_node.next=self.start
            self.start.prev.next=new_node
            self.start.prev=new_node           
     
    def insertAt(self,finder,item):
        
        if self.is_empty():
            return
        
        temp=self.search(finder)
        if temp==None:
            return
        if self.start.prev.data==temp.data:
            self.insert_at_last(item)
        
        
        else:
            new_node=node(item)
            new_node.prev=temp
            new_node.next=temp.next
            temp.next.prev=new_node
            temp.next=new_node
    
    
    def delete_at_first(self):
        if self.is_empty():
            print("list is empty")
            return    
        else:
            if self.start.next==self.start:
                self.start=None
            else:   
                self.start.next.prev=self.start.prev
                self.start.prev.next=self.start.next
                self.start=self.start.next
    
    
    def delete_at_last(self):
        if self.is_empty():
            print("list is empty")
            return        
        else: 
            if self.start.next==self.start:
                self.start=None
                return
        
            else:
                self.start.prev=self.start.prev.prev
                self.start.prev.next=self.start
    
    
    def deleteAt(self,finder):
        if self.is_empty():
            print("list is empty")
            return
        temp=self.search(finder)
        if temp==None:
            return
        if temp.data==self.start.data:
            self.delete_at_first()
        elif temp.data==finder:
            temp.next.prev=temp.prev
            temp.prev.next=temp.next
        elif temp.data==self.start.prev.data:
            self.delete_at_last()
            
                
                
          
    def print_list(self):
        temp=self.start
        if self.is_empty():
            print("list is empty")
            return
        while True:
            print(temp.data, end=" ")  
            temp=temp.next
            if temp==self.start:
                break
                
        print("\n") 
    def __iter__(self):
        return LinkedListIterator(self.start)
            
class LinkedListIterator:
    def __init__(self, start):
        self.start = start
        self.curr = start
        self.first_pass = True  # To handle the first node specially

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr:
            raise StopIteration
        if self.curr == self.start and not self.first_pass:
            raise StopIteration
        
        data = self.curr.data
        self.curr = self.curr.next
        self.first_pass = False
        return data

                
            
mylist=cdll()
mylist.insert_at_first(7) 
mylist.insert_at_first(6)
mylist.insert_at_first(5)
mylist.insert_at_first(4)
mylist.insert_at_first(4)
mylist.insert_at_first(3)  
mylist.insert_at_first(2)
mylist.insert_at_first(1)
mylist.print_list()
for i in mylist:
    print(i,end=" ")