class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
        new_node = BSTNode(value)
        if value < self.value:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass
        # BSTNode(target)
        value = self.value
        if target == value:
            return True
        if target < value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        pass
        if not self:
            return None
        current_max = self
        while current_max.right is not None:
            current_max = current_max.right
        return current_max.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass
        fn(self.value)
        if not self:
            return None
        if self.left or self.right:
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

