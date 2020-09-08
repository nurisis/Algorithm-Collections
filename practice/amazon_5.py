"""
Given the root of a binary tree, display the node values at each level.
Node values for all levels should be displayed on separate lines.
Let’s take a look at the below binary tree.
"""

from collections import deque


def level_order_traversal(root):
    result = ""

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result += str(node.data) + " "

            queue.append(node.left)
            queue.append(node.right)

    return result
