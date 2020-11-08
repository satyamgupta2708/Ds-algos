# this is inorder binary where the order of printing the element is left, root, right
class Node:
    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.data is not None:
            
            if self.left : 
                self.left.print_tree()
            print(self.data)
            if self.right:
                self.right.print_tree()


root = Node(12)
root.insert(17)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(27)
root.insert(6)
root.insert(2)
root.insert(10)
root.insert(0)
root.insert(8)

root.print_tree()