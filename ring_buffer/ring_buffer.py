from doubly_linked_list import DoublyLinkedList

# when the ring buffer is full and a new element is added,
# the oldest element in the ring is overwritten with the new element

# buffer size is 4 and you insert ten numbers
# insert one at a time, at the end of the buffer
# each iteration, the first element is removed from the front of the buffer
'''
[None, None, None, 0]
[None, None, 0, 1]
[None, 0, 1, 2]
[0, 1, 2, 3]
[1, 2, 3, 4]
[2, 3, 4, 5]
[3, 4, 5, 6]
[4, 5, 6, 7]
[5, 6, 7, 8]
[6, 7, 8, 9]
'''


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # Append method will add elements to the buffer
    def append(self, item):
        # check to see if capacity is full
        if self.capacity > self.storage.length:
            # if capacity isn't full then add the item to the tail
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        # if capacity is full
        elif self.capacity == self.storage.length:
            self.current.value = item
            # add new item where the old item was at
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    # returns all the elements in the buffer but not None
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.current
        list_buffer_contents.append(current_node.value)

        if current_node:
            next_node = current_node.next
        else:
            next_node = self.storage.head

        while next_node is not current_node:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        return list_buffer_contents


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass
#
#     def append(self, item):
#         pass
#
#     def get(self):
#         pass
