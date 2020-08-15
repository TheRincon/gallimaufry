class Node:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def insert(self, data):
        if self.root:
            if data < self.root:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.root = data

    def findval(self, lkpval):
        if lkpval < self.root:
            if self.left is None:
                return str(lkpval)+" NOT FOUND"
            return self.left.findval(lkpval)
        elif lkpval > self.root:
            if self.right is None:
                return str(lkpval)+" NOT FOUND"
            return self.right.findval(lkpval)
        else:
            print(str(self.root) + ' is found')

    def minValueNode(self, root):
        current = root

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current

    def deleteNode(self, root, key):
        # Base Case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's
        # key then it lies in left subtree
        if key < root.root:
            root.left = self.deleteNode(root.left, key)

        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif(key > root.root):
            root.right = self.deleteNode(root.right, key)

        else:
            # Node with only one child or no child
            if root.left is None :
                temp = root.right
                root = None
                return temp

            elif root.right is None :
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.root = temp.root

            # Delete the inorder successor
            root.right = self.deleteNode(root.right , temp.root)

        return root


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.root),
        if self.right:
            self.right.PrintTree()

def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root

def invertTree2(root):
    stack = [root]
    while stack:
        node = stack.pop(-1)
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root

if __name__ == '__main__':
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(5)
    root.insert(13)
    root.insert(15)
    root.insert(16)
    root.insert(3)
    root.insert(10)
    root.insert(1)
    root.insert(22)
    root = root.deleteNode(root, 14)
    root.insert(7)
    root.PrintTree()
    invertTree2(root)
    root.PrintTree()
    print('break')
    invertTree(root)
    root.PrintTree()
