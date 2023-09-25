class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    def __init__(self, value):
        new_value = Node(value)
        self.head = new_value
        self.tail = new_value
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        # if there is no value on Linked list  (Empty) than make head and tail point to new_value
        # if self.head is None:
        if self.length == 0:
            # self.__init__(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            # self.length += 1
        self.length += 1
        return True

    # make pop last value of linked list
    # first find the before of last value which is next is none
    # and find last value before's next value to none
    # and make tail to point that one
    def pop(self):
        # Edge case 1#
        if self.length == 0:
            print("Empty linked list")
            return None
        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        # My code
        # temp = self.head
        # print(f"self.lenght {self.length}")
        # for i in range(self.length - 1):
        #     print(f"{i}{temp.value}")
        #     if i == self.length - 1 - 1:
        #         print("i is self.length - 1")
        #         self.tail = temp
        #         temp.next = None
        #         self.length -= 1
        #         break
        #     temp = temp.next
        return temp

    # add new value on the first of linked list
    def prepend(self, value):
        new_value = Node(value)
        # my code
        # temp = self.head
        # if temp is not None:
        #     self.head = new_value
        #     self.head.next = temp
        # else:
        #     self.head = new_value
        #     self.tail = new_value
        # self.length += 1

        # other solution
        if self.length == 0:
            self.head = new_value
            self.tail = new_value
        else:
            new_value.next = self.head
            self.head = new_value
        self.length += 1
        return True

    # Edge case when linked list is empty

    def pop_first(self):
        # pop first item of out of the linked list
        if self.length == 0:
            return None
        # if self.length == 1:
        #     self.head = None
        #     self.tail = None
        temp = self.head
        self.head = self.head.next
        # before plainly return temp value, make sure that temp.next is None
        # because after pop, it is not part of linked list
        temp.next = None
        self.length -= 1
        if self.length == 1:
            self.tail = None
        return temp

    def get(self, index):
        # The method should handle the cases where the index is out of bounds.

        # The method should start at the head of the list and traverse the list using the next attribute of the nodes.

        # The method should stop traversing the list when it reaches the specified index and return the node at that position.

        # If the index is out of bounds, the method should return None.
        if index >= self.length or index < 0:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self , index , value):
        #update the value of the node at the specified index in the linked list
        if index >= self.length or index < 0:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length :
            return False
        new_node = Node(value)
        #insert the new node with the given value at the specified index in the linked list
        #edge cases
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            before_new_node = self.get(index-1)
            after_new_node = self.get(index)
            new_node.next = after_new_node
            before_new_node.next = new_node
            self.length += 1
        return True

    ## WRITE REMOVE METHOD HERE ##
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length + 1:
            return self.pop()
        else:
            prev = self.get(index-1)
            temp = self.get(index)
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp


    ## WRITE REVERSE METHOD HERE ##
    #reverse the order of the nodes in the linked list
    #head becomes the tail and the tail becomes the head
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

        return


# my_linked_list = LinkedList(4)
#
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# print(my_linked_list.print_list())
# print(my_linked_list.append(2))
# print(my_linked_list.append(1))
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
# print(my_linked_list.print_list())

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
# my_linked_list.print_list()
# my_linked_list.pop()
# my_linked_list.print_list()
# my_linked_list.prepend(0)
# print("after prepend 0")
# my_linked_list.print_list()
# my_linked_list.pop_first()
# my_linked_list.print_list()
get_value = my_linked_list.get(2)
print(f"get value {get_value}")
get_value = my_linked_list.set_value(2,6)
get_value = my_linked_list.get(2)
print(f"get value after set method :{get_value}")
my_linked_list.insert(1,2)
my_linked_list.print_list()








"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1

"""
