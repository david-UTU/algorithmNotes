#Red Black Trees are specific types of balanced search Trees
#Balanced search trees have a height of O(log n) for n items
#RBTs have red or black nodes
#Root and leaves (NIL nodes) are black
#All Paths from a node to its NIL descendents contain the same # of black nodes
#Nodes require one storage bit to keep track of color
#Longest path is no more than 2(shortest path)
#Used like binary search trees, but insert and remove work differently than in BSTs
#     B
#    / \
#   D   A
#      /  \
#     Z     Y
# In relation to Z, A is the parent, B is the grandparent, D is the uncle