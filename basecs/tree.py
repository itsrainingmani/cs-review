class BSTree:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def find_parent(root, value):
    if value == root.value:
        return None
    if value < root.value:
        if root.left == None:
            return None
        elif root.left.value == value:
            return root
        else:
            return findParent(root.left, value)
    else:
        if root.right == None:
            return None
        elif root.right.value == value:
            return root
        else:
            return findParent(root.right, value)


def find_node(root, value):
    if root == None:
        return None
    if root.value == value:
        return root
    elif value < root.value:
        return findNode(root.left, value)
    else:
        return findNode(root.right, value)


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


def bst_contains(root, value):
    if root == None:
        print("Not Found")
        return

    if value == root.value:
        print("Found")
        return
    elif value < root.value:
        bst_search(root.left, value)
    elif value > root.value:
        bst_search(root.right, value)

def bst_remove(root, value):
    node_to_remove = find_node(root, value)
    if node_to_remove == None:
        return False
    parent = find_parent(root, value)
    


if __name__ == "__main__":
    root = BSTree(10, BSTree(2), BSTree(12))
    tree_inorder(root)
    bst_insert(root, BSTree(4))
    bst_insert(root, BSTree(13))
    bst_insert(root, BSTree(11))
    tree_inorder(root)

    print("\n")

    print(findParent(root, findParent(root, 13).value).value)

    # bst_contains(root, BSTree(11))
