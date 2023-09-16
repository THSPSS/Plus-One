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
        #if there is no value on Linked list  (Empty) than make head and tail point to new_value
        #if self.head is None:
        if self.length == 0:
            #self.__init__(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            #self.length += 1
        self.length += 1
        return True

    #make pop last value of linked list
    #first find the before of last value which is next is none
    #and find last value before's next value to none
    #and make tail to point that one
    def pop(self):
        #Edge case 1#
        if self.length == 0:
            print("Empty linked list")
            return None
        temp = self.head
        prev = self.head
        while temp.next :
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        #My code
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

    #add new value on the first of linked list
    def prepend(self,value):
        new_value = Node(value)
        #my code
        # temp = self.head
        # if temp is not None:
        #     self.head = new_value
        #     self.head.next = temp
        # else:
        #     self.head = new_value
        #     self.tail = new_value
        # self.length += 1

        #other solution
        if self.length == 0:
            self.head = new_value
            self.tail = new_value
        else:
            new_value.next = self.head
            self.head = new_value
        self.length += 1

        return True
    #Edge case when linked list is empty

    def pop_first(self):
        #pop first item of linked list
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def get(self,value):
        return True




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
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.prepend(0)
print("after prepend 0")
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.print_list()
"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1

"""
