class BSTree:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # def insert(self, node):


# Node-Left-Right
def tree_preorder(tree):
    if tree == None:
        return
    print(tree.value)
    tree_inorder(tree.left)
    tree_inorder(tree.right)


# Left-Node-Right
def tree_inorder(tree):
    if tree == None:
        return
    tree_inorder(tree.left)
    print(tree.value)
    tree_inorder(tree.right)


# Left-Right-Node
def tree_postorder(tree):
    if tree == None:
        return
    tree_inorder(tree.left)
    tree_inorder(tree.right)
    print(tree.value)


def bst_insert(root, ins_node):
    if root == None:
        return
    if ins_node.value < root.value:
        if root.left != None:
            bst_insert(root.left, ins_node)
        else:
            root.left = ins_node
            return
    elif ins_node.value > root.value:
        if root.right != None:
            bst_insert(root.right, ins_node)
        else:
            root.right = ins_node
            return


def bst_search(root, node):
    if root == None:
        print("Not Found")
        return

    if node.value == root.value:
        print("Found")
        return
    elif node.value < root.value:
        bst_search(root.left, node)
    elif node.value > root.value:
        bst_search(root.right, node)


if __name__ == "__main__":
    root = BSTree(10, BSTree(2), BSTree(12))
    tree_inorder(root)
    bst_insert(root, BSTree(4))
    bst_insert(root, BSTree(13))
    bst_insert(root, BSTree(11))
    tree_inorder(root)

    bst_search(root, BSTree(9))
