class RBT():
    def __init__(self, root):
        self.root = root
        self.nil = None
        self.right = None
        self.left = None
        self.key = None
        self.p = None
        self.color = None

#T is of RBT class
def rbInsert(T,z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = red 
    rbInsertFix(T,z)

def rbInsertFix(T,z):
    while z.p.color == red:
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == red:
                z.p.color = black 
                y.color = black 
                z.p.p.color = red 
                z = z.p.p
            elif z == z.p.right:
                    z = z.p 
                    leftRotate(t,z)
                z.p.color = black 
                z.p.p.color = red 
                rightRotate(T,z.p.p)
        else:
            rightRotate(t,z)
            z.p.color = black 
            z.p.p.color = red 
            leftRotate(T,z.p.p)


def leftRotate(T,x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.P
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y 
    else:
        x.p.right = y
        y.left = x
        x.p = y

def rightRotate(T, x):
    y = x.left
    x.left = y.right
    y.right.p = x
    y.p = x.p 
    if x.p == T.nil:
        T.root = y
    else:
         if x == x.p.left:
            x.p.left = y
         else:
            x.p.right = y
    y.right = x
    x.p = y