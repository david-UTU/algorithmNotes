import BinaryTreeClass
import collections

def isBalanced(tree): #tree being a treenode data structure
    BalancedStatus = collections.namedtuple('BalancedStatus', ('balanced', 'height'))
    def checkBalanced(tree):
        if not tree:
            return BalancedStatus(balanced=True, height=-1)

        leftResult = checkBalanced(tree.left)
        if not leftResult.balanced:
            return leftResult

        rightResult = checkBalanced(tree.right)
        if not rightResult.balanced:
            return rightResult

        balanced = abs(leftResult.height - rightResult.height) <= 1
        height = max(leftResult.height, rightResult.height) + 1
        return BalancedStatus(balanced, height)
    return checkBalanced(tree).balanced
