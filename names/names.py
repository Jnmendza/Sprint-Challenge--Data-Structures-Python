import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Base Case is when it creates a new node. No new node will end it
    def insert(self, value):
        node = BST(value)
        # if inserted value is > node
        if value >= self.value:
            # if no value right
            if self.right is None:
                # set right to node
                self.right = node
            else:
                # recurse to the right
                return self.right.insert(value)

        # if inserted value is < node
        elif value < self.value:
            # if no value left
            if self.left is None:
                # set left to node
                self.left = node
            else:
                # recurse to the left
                return self.left.insert(value)

    # Return True if the tree contains the value. False if it doesn't
    def contains(self, target):

        if self.value == target:
            return True

        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
