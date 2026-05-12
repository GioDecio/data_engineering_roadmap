# A node is a pointer and a value, you can think of it as a dictionary
# So you can think of a LL as a nested dict
from functools import wraps

def print_list_after(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print("\nList after", func.__name__ + ":")
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
        # print(f"Return value from {func.__name__}: {result}")  # Add this line to debug
        return result
    return wrapper

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    @print_list_after
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    @print_list_after
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    @print_list_after
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    @print_list_after
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head= new_node
        self.length += 1
        return True
    

    @print_list_after
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -=1
        if self.length == 0:
            self.tail = None
        temp.next = None
        return temp

    @print_list_after
    def get(self, index):
        if index >= self.length or index < 0 :
            return None
        temp = self.head  
        for _ in range(index):
            temp = temp.next
        return temp
            
    @print_list_after
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return value
        return None
    
    @print_list_after
    def insert(self, index, value):
        if index > self.length or index < 0 :
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.get(index-1)
        post = self.get(index)
        prev.next = new_node
        new_node.next = post
        self.length +=1 
        return True
    
    @print_list_after
    def remove(self, index):
        if index > self.length or index < 0 :
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index-1)
        temp.next = temp.next.next
        self.length -=1
        return True

        
    @print_list_after
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail =temp
        before = None 
        after = temp.next
        for _ in range(self.length):
            after=temp.next
            temp.next = before # this is what reverses the arrow         
            before = temp
            temp = after
        return True
    
    







    
linked_list = LinkedList(1)
# linked_list.append(5)
# linked_list.append(100)
# linked_list.append(200)
# linked_list.append([1,2,3,4,6])
# linked_list.prepend(40)
# linked_list.pop()
# linked_list.pop_first()
# linked_list.get(20)
# linked_list.set_value(0,'A')
# linked_list.insert(1,23)
# linked_list.remove(1)
# linked_list.reverse()