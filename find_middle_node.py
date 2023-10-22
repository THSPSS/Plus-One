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


    def has_loop(self):
        #The method should be able to detect if there is a cycle or loop present in the linked list.
        slow = self.head
        fast = self.head
        #while slow.next != self.head or slow.next != None:
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def partition_list(self, x):
        # check the list if empty or not
        if self.head is None:
            return None
        # making two linked list
        # one is for before x
        # other one is after x
        before_x = Node(0)
        after_x = Node(0)
        prev1 = before_x
        prev2 = after_x
        temp = self.head
        while temp is not None:
            if temp.value < x:
                prev1.next = temp
                prev1 = temp
            else:
                prev2.next = temp
                prev2 = temp
            temp = temp.next
        prev1.next = None
        prev2.next = None
        prev1.next = after_x.next
        self.head = before_x.next


        def remove_duplicates(self):
            #Using a Set - This approach will have a time complexity of O(n),
            # where n is the number of nodes in the linked list.
            # You are allowed to use the provided Set data structure in your implementation.
            #traverse the linked list
            #    // Initialize an empty set to store unique values
            #create an empty set called values
            values = []
            #two pointer for prev and current
            prev = None
            current = self.head
            #traverse the linked list
            while current is not None and current.next is not None:
            #Without using a Set - This approach will have a time complexity of O(n^2),
            # where n is the number of nodes in the linked list.
            # You are not allowed to use any additional data structures for this implementation.




# Implement the find_kth_from_end function,
# which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
def find_kth_from_end(linked_list , k):
    slow = linked_list.head
    fast = linked_list.head
    # The fast pointer should move k nodes ahead in the list.
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow







my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
print(find_kth_from_end(my_linked_list , k))
print( my_linked_list.find_middle_node().value )





"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""