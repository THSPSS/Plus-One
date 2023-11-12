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


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
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
        values = set()
        #two pointer for prev and current
        prev = None
        current = self.head
        #traverse the linked list
        while current is not None:
            if current.value in values:
                prev.next = current.next
                self.lenght -= 1
            else:
                values.add(current.value)
                prev = current
            current = current.next
        #Without using a Set - This approach will have a time complexity of O(n^2),
        # where n is the number of nodes in the linked list.
        # You are not allowed to use any additional data structures for this implementation.
        for i in range(self.length):
            prev = current
            after = current.next
            for j in range(i , self.length):
                if current.value == after.value:
                    prev.next = after.next
                    self.length -= 1
                else:
                    prev = after
                    after = after.next
            current = current.next

        #method remove_duplicates():

    # // Set the current pointer to the head of the list
    #
    # set current to head of the list






    #convert a binary number, represented as a linked list, to its decimal equivalent.
    def binary_to_decimal(self):
        result = 0
        temp = self.head
        for i in range(self.length-1 , -1, -1):
            print(f"temp.value {temp.value}")
            if temp.value == 1 :
               result += 2**int(i)
            print(f"result {result}")
            temp = temp.next
        # while temp is not None:
        #     if temp.value == 1 :
        #         result += 2**cnt
        #         print(2**cnt)
        #         print(f"cnt{cnt}")
        #     temp = temp.next
        #     cnt -= 1

        return result


    def reverse(self):
        if self.length == 0:
            return
        if self.length == 1:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



     #LL: Reverse Between ( ** Interview Question)
    def reverse_between(self, start, end):
        temp = self.head
        cnt = 0
        #get to the start using for loop
        while temp is not None and cnt < start:
            temp = temp.next
        #get start position and loop through end with prev and after to reverse positions
        # temp = self.head
        # self.head = self.tail
        # self.tail = temp
        before = None
        for _ in range(start , end):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


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
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(1)
my_linked_list.append(0)

k = 3
print(f"my_linked_list length {my_linked_list.length}")
print(my_linked_list.head.value)
print(find_kth_from_end(my_linked_list , k).value)
print( my_linked_list.find_middle_node().value )
print(my_linked_list.binary_to_decimal())





"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""