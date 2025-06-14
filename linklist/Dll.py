class node():
    def __init__(self ,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class dll():
    def __init__(self,start=None):
        self.start=start     
    
    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self, data):
          
        if self.is_empty():
            n=node(None,data,self.start)
            self.start=n
        else:
            n=node(None,data,self.start)
            self.start.prev=n
            self.start=n
    def insert_at_last(self,data):
        if self.is_empty():
            n=node(None,data,self.start)
        else:
            temp=self.start
            while temp.next:
                temp=temp.next            
            n=node(temp,data,None)
            temp.next=n
    def search(self,finder):
        if self.is_empty():
            print("list is empty")
            
            
        else:
            
            temp=self.start 
            while temp:
                if temp.item==finder:
                    return temp
                
                temp=temp.next
            print("item not found")    
            return None
    
    
    def insert_before(self, finder, data):
        temp = self.search(finder)
        if self.is_empty():
            print("list is empty")
        
        if temp.prev is None:
            self.insert_at_first(data)
        else:
            prevnode=temp.prev
            n=node(prevnode,data,temp)
            temp.prev.next=n
            
            
        
    def insert_after(self,finder,data):
        temp=self.search(finder)
        if temp is None:
            print("Item not found")
            return    
        if temp.next is None: 
            n=node(temp,data,None)
            temp.next=n 
        else:
            n=node(temp,data,temp.next)
            temp.next=n
            temp.next.prev=n
    def delete_at_first(self):
        if self.is_empty():
            print("list is empty")
        else:
            self.start=self.start.next    
    def delete_at_last(self):
        if self.is_empty():
            print("List is empty      111")   
            return
        if self.start.next is None:
            self.start=None
        
        temp=self.start
        while temp.next.next is not None:
            
            temp=temp.next
            
        temp.next=None   
    
    
    def delete_before(self,finder):
        temp=self.start
        if  not temp or not temp.next:
            return
        if temp.next.item==finder:
            self.start = temp.next
            temp.prev=None
        else:
            if temp:    
                while temp.next:
                    if temp.next.item==finder:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                        break
                    temp=temp.next
            else:
                print("item not found") 
    def delete_after(self,finder):
        temp=self.start
        if not  temp or  not temp.next:
            print("not enuf node to delete")
        else:
            if temp:
                while temp.next.next is not None:
                    if temp.item==finder:
                        print(temp.item)
                        temp.next.next.prev=temp
                        temp.next=temp.next.next
                        break
                    temp=temp.next
            else:
                print("item not found")
                
        
    
    def printlist(self):
        temp=self.start
        if self. is_empty():
            print('list is empty')
            
        while temp:
            print(temp.item,end=' ')
            temp=temp.next
        print("\n")  
mylist=dll()
mylist.insert_at_first(20)
mylist.insert_at_first(10)
mylist.insert_at_first(5)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_at_last(80)
mylist.insert_before(5,11)
mylist.insert_before(80,66)
mylist.insert_after(30,35)
mylist.printlist()
mylist.delete_at_first()
mylist.printlist() 
mylist.delete_at_last()
mylist.printlist()
mylist.delete_before(35)
mylist.delete_before(5)
mylist.delete_before(40)
mylist.printlist()
mylist.delete_after(111)
mylist.printlist()



         
           