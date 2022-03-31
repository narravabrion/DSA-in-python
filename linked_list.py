# Node class
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # print linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # insert at the beiginning
    def insert_at_beginning(self, new_data):
        # create new node
        new_node = Node(new_data)
        # point the next of new_node to current head
        new_node.next = self.head
        # point head of list to new_node
        self.head = new_node

    # insert after node
    def insert_after(self, prev_node, new_data):
        # check if node exists
        if prev_node is Node:
            raise Exception("Previous node does not exist")
        # create new node
        new_node = Node(new_data)
        # point next of the new node to prev_node next
        new_node.next = prev_node.next
        # point next of prev_node to the new_node
        prev_node.next = new_node

    # insert at the end of the list
    def insert_at_end(self, new_data):
        # create new node
        new_node = Node(new_data)
        # check if list is empty
        if self.head is None:
            self.head = new_node
            return
        # traverse list and add to last item on list
        last = self.head
        while last.next:
            last = last.next
        # append to end of list
        last.next = new_node


if __name__ == "__main__":
    l_list = LinkedList()  # initalize linked list
    l_list.head = Node(1)  # initialize first/head node
    # initialize subsequent nodes
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    # link the entire list together
    l_list.head.next = node2
    node2.next = node3
    node3.next = node4

    l_list.print_list()
    l_list.insert_at_end( 5)
    print("after adding")
    l_list.print_list()
