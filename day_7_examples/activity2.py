# Define a class for the nodes in the linked list
class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference


# Define a class for the linked list itself
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Method to add a new node to the end of the list
    def append(self, data):
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse the list to find the last node
        last_node = self.head
        while last_node.reference is not None:
            last_node = last_node.reference

        # Set the new node as the next node of the last node
        last_node.reference = new_node

    def add_item(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.reference:
                last_node = last_node.reference
            last_node.reference = new_node

    def add_item_after(self, value, target):
        new_node = Node(value)
        current_node = self.head
        while current_node:
            if current_node.data == target:
                new_node.reference = current_node.reference
                current_node.reference = new_node
                return
            current_node = current_node.reference
        raise ValueError(f"Value {target} not found in the list.")
    
    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

    def remove_item(self, value):
        current_node = self.head
        if current_node and current_node.data == value:
            self.head = current_node.reference
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != value:
            prev_node = current_node
            current_node = current_node.reference
        if current_node is None:
            raise ValueError(f"Value {value} not found in the list.")
        prev_node.reference = current_node.reference
        current_node = None

    # Method to print the contents of the list
    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.reference

if __name__ == "__main__":

    node1 = Node(5)
    print(node1)
    print(node1.data)
    node2 = Node(11)
    node1.reference = node2
    print(node2)
    print(node1.reference)
    node3 = Node("pumpkin")
    node2.reference = node3
    print(node3)
    print(node2.reference.data)


    #linked_list1 = LinkedList()
    #linked_list1.print_linked_list()
    #linked_list1.add_to_start(82)
    #linked_list1.add_to_start(15)
    #linked_list1.print_linked_list()
    #print("_"*40)
    #linked_list1.add_item_after(13,55)
    #linked_list1.add_item_after(55, 15)
    #linked_list1.print_linked_list()

