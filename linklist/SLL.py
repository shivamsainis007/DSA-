# class node():
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next
# class sll():
#     def __init__(self,start=None):
#         self.start=start
#     def is_empty(self):
#         return self.start==None    
#     def insert_at_start(self ,data):
#         n=node(data,self.start) 
#         self.start=n
#     def insert_at_last(self,data):
#         n=node(data)
#         if self.is_empty():
#             self.start=n
#         else:
#             temp=self.start 
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=n              
            
#     def search(self,data):
#         temp=self.start
#         while temp is not None:
#             if temp.item == data:
#                 return temp
#             temp=temp.next
#         return None
            
#     def insert_after(self,finder,newdata):
#         temp=self.search(finder)
#         if temp is None:
#             print("item is not found")
#             return
#         else:
#             n=node(newdata,temp.next)
#             temp.next=n    
#     def printlist(self):
#         temp=self.start
#         while temp is not None:
#             print(temp.item ,end =" " )
        
#             temp=temp.next
#         print("\n")     
#     def delete_at_last(self):
#         if self.is_empty():
#             print(" list is empty")
#         elif self.start.next is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next.next is not  None:
#                 temp=temp.next
#             temp.next=None
#     def delete_at_first(self):
#         if self.is_empty():
#             print("list is empty")
#         else:
#             self.start=self.start.next    
#     def delete_item(self,data):
#         if self.is_empty():
#             print("list is empty")
#             return
#         elif(self.start.next is None):
#             if self.start.item==data:
#                 self.start=None
#             return    
#         else:
#             temp=self.start
#             while temp.next is not None:
#                 if temp.next.item==data:
#                     temp.next=temp.next.next
#                     break
#                 temp=temp.next
#                 print("data not found") 
#     def __iter__(self):
#         return sllitreator(self.start)                   
# class sllitreator():
#     def __init__(self,start): 
#         self.current=start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data=self.current.item
#         self.current=self.current.next
#         return data
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class sll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            return
        temp = self.start
        while temp.next:
            temp = temp.next
        temp.next = n

    def search(self, item):
        prev = None
        temp = self.start
        while temp:
            if temp.item == item:
                return prev, temp
            prev = temp
            temp = temp.next
        return None, None

    def insert_after(self, finder, data):
        _, temp = self.search(finder)
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
        else:
            print("Item not found")

    def insert_before(self, finder, data):
        prev, temp = self.search(finder)
        if self.is_empty():
            print("List is empty")
            return
        n = Node(data, temp)
        if prev is None:
            self.start = n
        else:
            prev.next = n

    def delete_at_first(self):
        if self.is_empty():
            print("List is empty")
        else:
            self.start = self.start.next

    def print_list(self):
        temp = self.start
        if self.is_empty():
            print("List is empty", end=" ")
            return
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()
  
                
                                              
                
            
# mylist=sll()
# mylist.insert_at_start(20)  
# mylist.insert_at_start(10) 
# mylist.insert_at_last(30)
# mylist.insert_at_last(40)
# mylist.insert_at_last(50)
# mylist.insert_before(10,12)
# mylist.insert_before(12,11)

# mylist.insert_after(30,40)
# mylist.insert_after(40,45)
# mylist.insert_after(68,45)
# mylist.print_list()
# mylist.delete_at_first()
# mylist.print_list() 
# mylist.delete_item(30)
# mylist.printlist()
# for x in mylist:
#     print(x,end=' ')
                             
        
        