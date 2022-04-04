from itertools import count


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head =None

    def get(self, index: int) -> int:
        temp = self.head 
        
        if index == 0:
            return temp.data 
        pos = 0
        while temp is not None:
            if pos == index:
                return temp.data
                break
            # return temp.data
            temp = temp.next
            pos+=1
            
        if temp == None:
            return -1
            

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        temp = self.head 
        if self.head is None:
            self.head = new_node
        while temp.next is not None:
            temp = temp.next
        temp.next =new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        temp = self.head 
        if index ==0:
            new_node.next=temp
            self.head = new_node
        pos = 0
        while temp is not None:
            if pos == index:
                break
            prev = temp
            temp = temp.next
            pos+=1
            prev.next =new_node
            new_node.next=temp
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return -1
        if index ==0:
            self.head = self.head.next
            return self.head
        pos =0
        curr = self.head
        prev=self.head 
        temp = self.head
        while curr is not None:
            if pos == index:
                temp = curr.next
                break
            prev = curr
            curr =curr.next
            pos+=1
        prev.next=temp
        return prev
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp =temp.next
    def count_nodes(self,head,count):
        
        if self.head is None:
            return count
        
        self.count_nodes(head.next,count+1) 
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.print_list()
print('#')
obj.addAtHead(1)
obj.print_list()
print('add at head')
obj.addAtTail(3)
obj.print_list()
print('add at tail')
obj.addAtIndex(1,2)
obj.print_list()
print('add at index')
param_1 = obj.get(1)
obj.print_list()
print('get')
obj.deleteAtIndex(1)
obj.print_list()
print('delete at index')
param_1 = obj.get(1)
obj.print_list()
obj.count_nodes()

# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]