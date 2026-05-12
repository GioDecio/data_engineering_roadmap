class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    def merge(self, other_ll):
        dummy = Node(0)
        current=dummy
        self.length += other_ll.length
        self_head = self.head
        other_head = other_ll.head
        while self_head and other_head:
            if self_head.value <= other_head.value:
                current.next = self_head
                self_head = self_head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
        
        if self_head:
            current.next = self_head 
            #self_head = self_head.next

        if other_head:
            current.next = other_head 
            #other_head = other_head.next


        #self.head = dummy.next 
        #self.tail = current

        

            


    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""