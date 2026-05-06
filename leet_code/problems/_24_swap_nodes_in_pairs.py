"""
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
"""


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
        #print("None")
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

# @print_list_after
def swapPairs(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Base case
    if not head or not head.next:
        return head

    # Store the nodes you'll need
    first = head
    second = head.next

    first.next = swapPairs(second.next)
    second.next = first

    return second

    
linked_list = LinkedList(1)
linked_list.append(5)
linked_list.append(100)
linked_list.append(200)
print('\n')
print(swapPairs(linked_list.head).value)
print(swapPairs(linked_list.head.next).value)
#print(swapPairs(linked_list.head).next.next.value)
# print(swapPairs(linked_list.head).next.next.next.value)



