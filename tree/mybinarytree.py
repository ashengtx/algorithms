class BinaryTree(object):
    """自己写"""
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, data):
        t = BinaryTree(data)
        if self.left_child is None:
            self.left_child = t
        else:
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, data):
        t = BinaryTree(data)
        if self.right_child is None:
            self.right_child = t
        else:
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_value(self):
        return self.key

    def set_root_value(self, data):
        self.key = data


