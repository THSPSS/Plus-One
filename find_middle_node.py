class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        #the method should use a two-pointer approach, where one pointer (slow) moves one node
        #at a time and the other pointer (fast) moves two nodes at a time.
        #when the fast pointer reaches the end of the list or has no next node , the slow pointer
        #should be at the middle node of the list
        #The method should return the middle node or the first node of the second half of the list if the list has
        #an even number of nodes
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""