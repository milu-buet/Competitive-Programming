


# AVL tree
# All operations O(logn)
# depth: 1.44*log(N)
# need to save height


# Red-black Tree
# All operations O(logn)
# depth: 2*log(N)
# only one bit for color for each node



# the AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and deletion.
# Use red-black: when frequent insertions and deletions happens.
# Use AVL: When frequent search operation happens.



# Splay tree
# keep doing rotations to move up a node
# insert, delete: worst O(n), amortized O(logn) 
# it's a caching tree# why use: in practice most of the time 20% of the data are accessed 80% of the time.