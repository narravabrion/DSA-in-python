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
    def insert_after_node(self, prev_node, new_data):
        # check if node exists
        if prev_node is None:
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
    # delete at node
    def delete_node(self,key):
        temp = self.head
        # if the head contains the key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next #set head to the next node
                temp = None # free up space occupied by the node
                return
        # search for key in the list while keeping track of the previous node
        while(temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        #  if list if empty or key not in list
        if(temp is None):
            # return
            raise Exception('Key not in list')
            
        # unlink the node to be deleted from the list
        prev.next = temp.next
        temp = None
    
    # delete at given position
    def del_at_position(self,position):
        # check if the list is empty
        if self.head == None:
            return
        # check if the position is 0 then just delete the head 
        if position == 0:
            self.head = self.head.next
            return self.head
        # traverse the list looking for the position
        #  keep track of the list index, current node, previous node 
        index =0
        current = self.head
        prev = self.head 
        temp = self.head

        while current is not None:
            if index ==position:
                temp= current.next
                break
            prev = current
            current = current.next
            index +=1
        prev.next = temp
        return prev
    # sort list
    def sort_list(self):
        current = self.head
        index= Node(None)
        if current is None:
            return
        while current is not None:
            index = current.next
            while index is not None:
                if current.data>index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)



if __name__ == "__main__":
    l_list = LinkedList()  # initalize linked list
    l_list.head = Node(1)  # initialize first/head node
    # initialize subsequent nodes
    node2 = Node(2)
    node3 = Node(4)
    node4 = Node(3)
    # link the entire list together
    l_list.head.next = node2
    node2.next = node3
    node3.next = node4

    l_list.print_list()
    l_list.sort_list()
    print("after sort")
    l_list.print_list()
    l_list
