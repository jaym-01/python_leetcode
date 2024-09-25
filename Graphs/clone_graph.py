"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        head = Node(node.val)
        all_nodes = {}
        all_nodes[node.val] = head
        queue = [node]

        while len(queue) > 0:
            top = queue.pop(0)
            new_node = all_nodes[top.val]

            if len(top.neighbors) > 0:
                for neighbor in top.neighbors:
                    if neighbor.val not in all_nodes:
                        all_nodes[neighbor.val] = Node(neighbor.val)
                        new_node.neighbors.append(all_nodes[neighbor.val])
                        queue.append(neighbor)
                    else:
                        new_node.neighbors.append(all_nodes[neighbor.val])
        
        return head


