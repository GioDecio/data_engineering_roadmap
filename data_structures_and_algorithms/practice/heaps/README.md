# Heaps
Heaps are complete trees, no gaps! 
The descendants must be equal or greater (or smaller if it is a minheap) than the parent.
You can have duplicates

Max heap vs Min heaps
The first has the max value at the top.
Not good for searches. They are used to keep track of the item at the top and remove it.
It is created with list, no node class.
If the following tree: 

is stored like this:
[x|99|72|61|58|55|27|18], then, left_child = 2*parent_index, and right_child = left_child + 1
 .
 What about parent?
 you divde the index of the child by 2

 Usually they are encoded liske this though:
 [99|72|61|58|55|27|18]

 ## Priority queues
 Hepas are preferred because of big O (log n).