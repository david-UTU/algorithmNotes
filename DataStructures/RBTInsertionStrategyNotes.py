#Strategy
#Inset the node and color it red
#Recolor and rotate nodes to fix any violations
#4 potential violations
#   1. Inserted node Z should be black, fix by coloring black
#   2. Z.uncle = red -> color Z.parent and Z.uncle black. Z.grandparent is red
#   3. Z.parent & Z should be red but Z.uncle and Z.grandparent should be black
#      fix by rotating Z and Z.parent so that Z is in the parent position.
#   4. Z & Z.parent are red, Z.grandparent & Z.uncle are black
#      fix by rotating Z.grandparent such that Z.parent moves to Z.grandparent position 
#      and Z moves to Z.parent position. If Z has a Z.sibling,
#      move this sibling to the new Z.child position