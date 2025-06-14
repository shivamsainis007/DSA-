class node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class cll():
    def __init__(self,last=None):
        self.last=last
    def Is_empty(self):
        return self.last==None   
    def Insert_at_first(self,data):
        new_node=node(data)
        if self.Is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node 
    def Insert_at_last(self,data):
        new_node=node(data)
        if self.Is_empty():
            new_node.next=new_node
            self.last=new_node
        else:
            new_node.next=self.last.next
            self.last.next=new_node
            self.last=new_node  
    def search(self,finder):
        if self.Is_empty():
            print("list is empty")
            return
        temp=self.last.next
        while True:
            if temp.data==finder:
                return temp
            temp=temp.next
            if temp==self.last.next:
                break
        print("itme not found")    
        return None
    def Insert_at(self, finder, data):
        result = self.search(finder)
    
        if result is None:
            print(f"'{finder}' not found, cannot insert.")
            return

        if result == self.last:
            self.Insert_at_last(data)
        else:
            new_node = node(data)
            new_node.next = result.next
            result.next = new_node
    
    def delete_at_first(self):
        if self.Is_empty():
            return

        if self.last==self.last.next:
            self.last=None
        else:
            self.last.next=self.last.next.next    
    def delete_at_last(self):
        if self.Is_empty():
            return
        
        if self.last==self.last.next:
            self.last=None
        else:
            temp=self.last.next
            while temp.next is not self.last:
                temp=temp.next
            temp.next=self.last.next    
    
    def delete_at(self,finder):
        if self.last == self.last.next and self.last.data == finder:
            self.last = None
        curr=self.last.next
        if curr.data == finder:#delete only first node
            self.last.next = curr.next
            print(f"Deleted node with data {finder}.")
            return 
            
        
        prev=curr
        curr=curr.next
        while curr != self.last.next:
            if curr.data == finder:
                prev.next = curr.next
                print(curr.data,self.last.data)
                if curr == self.last:
                    prev.next=self.last.next
                    self.last = prev# Update last if we deleted the last node
                    
                print(f"Deleted node with data {finder}.")
                return
            prev = curr
            curr = curr.next

        print("Node not found.")
                                  
                    

                     
                       
            
    def print_list(self):
        if self.Is_empty():
            print("list is empty")
            return
        temp=self.last.next
        while True :
            print(temp.data,end=" ") 
            temp=temp.next 
            if temp==self.last.next:
                break
        print("\n") 
        
               
 
mylist=cll()
mylist.Insert_at_last(10)
mylist.Insert_at_last(20)
mylist.Insert_at_last(30)
mylist.print_list()
# mylist.Insert_at(20,40)
# mylist.delete_at_first()
# mylist.print_list()
# mylist.delete_at_last()
mylist.delete_at(30)
mylist.print_list()
            
                 