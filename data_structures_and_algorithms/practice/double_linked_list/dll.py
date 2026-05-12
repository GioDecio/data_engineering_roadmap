from functools import wraps

def print_list_after(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        print("\nList after", func.__name__ + ":")
        temp = self.head
        while temp is not None:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print("None")
        #print(f"Return value from {func.__name__}: {result}")  # Add this line to debug
        return result
    return wrapper

class Node:
    def __init__(self, value):
        self.value=value 
        self.next=None 
        self.previous=None
    

class DoublyLinkedList:
    @print_list_after
    def __init__(self, value):
        new_node = Node(value)
        self.head=new_node 
        self.tail=new_node
        self.length=1

    @print_list_after
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail=new_node
        self.length +=1
        return True
    
    @print_list_after
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail 
        if self.length ==1:
            self.head = None
            self.tail = None 
        else: 
            self.tail = self.tail.previous 
            self.tail.next=None 
            temp.previous=None
        self.length -=1
        return temp
    
    @print_list_after
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next=self.head 
            self.head.previous = new_node
            self.head = new_node
        self.length +=1
        return True
    
    @print_list_after
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head 
        if self.length ==1:
            self.head = None
            self.tail = None 
        else:   
            self.head = temp.next
            self.head.previous=None
            temp.next=None
        self.length -=1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2: 
            temp = self.head 
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.previous
        return temp

    @print_list_after
    def set_value(self, index, value):
        temp = self.get(index) 
        if temp:
            temp.value = value
            return True 
        return False

    @print_list_after
    def insert(self, index, value):
        if index < 0 or index >self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        before.next = new_node
        new_node.previous = before
        new_node.next = after 
        after.previous = new_node
        self.length +=1
        return True

    
    @print_list_after
    def remove(self, index):
        if index < 0 or index >=self.length:
            return None
        if index == self.length-1:
            return self.pop()
        if index ==0:
            return self.pop_first()
        before = self.get(index - 1)
        temp = before.next
        after = temp.next
        before.next = after 
        after.previous = before
        temp.previous = None
        temp.next = None 
        self.length -=1
        return temp


        

        
doubly_linked_list = DoublyLinkedList(7) 
doubly_linked_list.append(4)
doubly_linked_list.append(5)
doubly_linked_list.append(6)
doubly_linked_list.append(7)
doubly_linked_list.pop()
doubly_linked_list.prepend(10)
doubly_linked_list.pop_first()
print(doubly_linked_list.get(1).value)
print(doubly_linked_list.set_value(1,13))
doubly_linked_list.insert(2,17)
doubly_linked_list.remove(1)