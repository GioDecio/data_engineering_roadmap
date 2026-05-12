from functools import wraps

def print_queue(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print("\n queue after", func.__name__ + ":")
        temp = self.first
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

class Queue:
    @print_queue
    def __init__(self, value):
        new_node = Node(value)
        self.first=new_node
        self.last=new_node 
        self.length=1

    @print_queue
    def enque(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first=new_node
            self.last=new_node 
        else:
            self.last.next = new_node 
            self.last = new_node
        self.length +=1

    @print_queue 
    def dequeue(self):
        if self.first is None:
            return None 
        temp = self.first
        if self.length == 1:
            self.first = None 
            self.last = None
        else: 
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp
    
    




queue = Queue(6)
queue.enque(7)
queue.enque(8)
queue.enque(9)
queue.dequeue()
