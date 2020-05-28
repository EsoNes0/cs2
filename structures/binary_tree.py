'''
Description: Binary Search Tree implementation
Author: Larsen Close
Version: Completed through A work, revisited to work on remove()
Outline and initial tests provided in class by Professor Dr. Beaty at
MSU Denver
'''


class BinaryTree():
    """Binary tree class"""
    _empty = {}

    def __init__(self, value=None, parent=None):
        self.left = self.right = None
        self.value = self._empty
        self.parent = parent

        if value:
            try:
                for i in value:
                    self.insert(i)
            except TypeError:
                self.insert(value)

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node
        yield self.value
        if self.right:
            for node in self.right:
                yield node

    def __str__(self):
        return ','.join(str(node) for node in self)

    def empty(self):
        """Returns true if empty"""
        return self.value == self._empty

    def insert(self, value):
        """Binary tree insert function"""

        if self.empty():
            self.value = value
            return
        if value < self.value:
            if not self.left:
                self.left = BinaryTree(value, self)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinaryTree(value, self)
            else:
                self.right.insert(value)

    def next_highest(self):
        next_highest = self.left
        while next_highest.right:
            next_highest = next_highest.right
        return next_highest

    def remove_both_references(self):

        next_highest = self.next_highest()

        self.remove(next_highest.value)

        next_highest.left = self.left
        next_highest.right = self.right
        self.reference_replacement(next_highest)

    def remove(self, value):
        # Base case we've found the value
        if self.value == value:

            # If no children we just have to delete the reference to self
            if not self.left and not self.right:
                self.reference_replacement(None)

            # If only right child then
            # replace the reference to self with right child
            elif not self.left:
                self.reference_replacement(self.right)

            # Same but left
            elif not self.right:
                self.reference_replacement(self.left)

            # If two children, move the next highest node to our spot
            # Remove it
            # Give it our children
            # Change the reference to us to be to it
            else:
                self.remove_both_references()

        # Recursive calls depending on value until we find the value
        elif self.value > value:
            self.left.remove(value)
        else:
            self.right.remove(value)

    def reference_replacement(self, new):
        # Checks which parent has a reference to self
        # replaces reference with argument

        if self.parent.left == self:
            self.parent.left = new
        elif self.parent.right == self:
            self.parent.right = new
