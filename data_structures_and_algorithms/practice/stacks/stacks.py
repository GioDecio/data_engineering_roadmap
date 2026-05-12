from functools import wraps

def print_stack(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print("\nstack after", func.__name__ + ":")
        temp = self.top
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
        return result
    return wrapper

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None


class Stack:
    @print_stack
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node 
        self.height=1

    @print_stack
    def push(self, value):
        if self.height == 0:
            self.top = new_node        
        else: 
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        self.height +=1
        
    @print_stack
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -=1
        return temp
        



stack = Stack(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()