import BinaryTreeClass

def treeTraversal(root): #root being a binary tree node
    if root:
        print(f'Preorder: {root.data}')
        treeTraversal(root.left)
        print(f'Inorder: {root.data')
        treeTraversal(root.right)
        print(f'Postorder: {root.data}')
