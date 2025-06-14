import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from linklist.SLL import sll

class Stack:
    def __init__(self):
        self.mylist = sll()
        self.count = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self, data):
        self.mylist.insert_at_start(data)
        self.count += 1

    def pop(self):
        if not self.is_empty():
            self.mylist.delete_at_first()
            self.count -= 1
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
        return None

    def print_stack(self):
        self.mylist.print_list()
        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())  # 30
stack.print_stack()  # 30 20 10

stack.pop()
print("Top after pop:", stack.peek())  # 20
stack.print_stack()  # 20 10
