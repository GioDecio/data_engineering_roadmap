class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def insert_at_beginning(self, node):
        node.next = self.head
        self.head = node

    def insert_at_end(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def insert_after(self, target_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_data)

    def remove(self, target_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_data:
            self.head = self.head.next
            return

        previous_head = self.head
        for node in self:
            if node.data == target_data:
                previous_head.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_data)


sample = "Ciao a tutti belli e brutti".split(" ")

ll = LinkedList(sample)
ll.insert_at_beginning(Node("Udite!"))
ll.insert_at_end(Node("FINE"))
ll.insert_after("Ciao", Node(","))
ll.remove("Ciao")


for node in ll:
    print(node)
