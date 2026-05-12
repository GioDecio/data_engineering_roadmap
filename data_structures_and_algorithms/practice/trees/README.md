# BINARY TREE

Full tree: either node point to 0 pr 2 nodes
Perfect tree: any level has two nodes
At tree can be full but not perfect
Complete: no gaps from left to right
There are parents, child, and siblings.
A node can only have ONE parent
A node without children is called leaf


# BINARY SEARCH TREE

start compare with parent node.

# Big O

Best case: O(log n): Divide and conquer
Worst case: O(n)
We treat as if the big O is O(log n)


# Balanced Tree
A balanced is not necessarily perferct nor complete.
It is a binary tree where the height difference between the left and right subtrees of any node is at most 1. 
This balance property must be maintained recursively for all nodes in the tree.
Example of an unbalanced tree:
     A
   /   \
  B     C
 /     /
D     E
     /
    F

Here's a simple example of a balanced tree:
     A
   /   \
  B     C
 /     / \
D     E   F




The importance of balanced trees:
They ensure optimal performance for operations like search, insert, and delete
They maintain O(log n) time complexity instead of degrading to O(n)
They prevent the tree from becoming skewed or linear-like in structure
Common types of self-balancing trees include:
* AVL Trees
* Red-Black Trees
The balancing property is crucial because it prevents the tree from becoming inefficient. 
For example, if a binary search tree becomes completely unbalanced (like a linked list), 
operations that should take O(log n) time would degrade to O(n) time, 
losing the primary advantage of using a tree structure.
To maintain balance, these trees use various rotation operations and balance factors to restructure 
themselves automatically when nodes are inserted or deleted.


# Insert
1. create a new node
2. compare with root: if <left else > right
3. If None, insert the new node, else move to next
4. repeat 2 and 3
We need to iterate with a while loop with a temp variable that starts from root.
Edge cases: 
* The tree is emptyif root==None then root = new_node
* The node already exists: inside the while loop: if new_node == temp, return False